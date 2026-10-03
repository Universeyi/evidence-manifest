#!/usr/bin/env python3
"""ASSERT-KTH "On Randomness in Agentic Evals" artefacts -> evidence-manifest.

Bjarnason, Silva and Monperrus (arXiv 2602.07150) ran two scaffolds
(nano-agent, R2E-Gym) x three open models x two temperatures on SWE-bench
Verified, ten independent runs per setting, and published everything as
`ASSERT-KTH/agentic-evals-artifacts` (CC-BY-4.0). Each run carries the
standard SWE-bench harness results JSON: resolved_ids, unresolved_ids,
empty_patch_ids, error_ids, incomplete_ids over the 500 instances.

This adapter reads those results files only (2.8 MB for all 120 runs); the
trajectories (3.4 GB, with per-message token usage and exit reasons) exist and
are referenced as the retained observation, but are not needed for the noise
floor and are not fetched here.

A note on the record: inside the DeepSWE directories the results files carry
names from other configurations (an r2e "temp_0.0" name inside the nano-agent
temperature-1.0 directory, nano-agent "preds" names inside the r2e
temperature-0 directory). The directory labels, not the file names, match the
paper's Table 1 means run for run (31.4 / 34.4 / 20.4 / 19.2), so directories
are trusted and file names are not.

What maps where:
  task_id                      instance_id
  run.repetition_index         run_N + 1, total 10
  verdict.score                1.0 resolved / 0.0 unresolved or empty patch
  verdict.reason               'resolved' / 'unresolved' / 'empty_patch'
  outcome.reason               completed for the three above; 'error' for
                               error_ids (the harness could not evaluate the
                               instance: no verdict, excluded from denominators);
                               'unknown' for incomplete_ids
  verdict.criteria_version     'swebench-harness-schema-v2' -- the harness
                               version is not in the file; the schema version is
  env.image_digest             'unrecorded' (SWE-bench builds one image per
                               instance; digests are not in the results)
  serving                      self-hosted vLLM per the file names; not read back
  sampling.temperature         0.0 for '__temp0' / '-temp0' directories; otherwise the model's
                               default per the paper's Table 1: Qwen3-32B 0.6, DeepSWE 1.0, Devstral 0.2
                               (the dataset README says 0.6 for all; the paper's table is more specific)
  usage                        null with reason: usage lives in the trajectories

    python3 adapters/kth_agentic_evals.py index.json --out manifests/kth/
      index.json: [{"config": <top-level directory>, "run": <int>, "file": <local results json>}, ...]
      built from the dataset tree by classifying files on content ('resolved_ids' present);
      directory names are the configuration labels, file names are not trusted (see notes)
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

SRC = "https://huggingface.co/datasets/ASSERT-KTH/agentic-evals-artifacts"
MODELS = {"Qwen_Qwen3-32B": "Qwen/Qwen3-32B", "mistral_devstral-2512": "mistralai/Devstral-2-123B (devstral-2512)",
          "agentica-org_DeepSWE-Preview": "agentica-org/DeepSWE-Preview", "agentica-org__DeepSWE-preview": "agentica-org/DeepSWE-Preview"}


def parse_config(name: str) -> dict:
    temp0 = name.endswith("__temp0") or name.endswith("-temp0")
    base = re.sub(r"(__temp0|-temp0)$", "", name)
    scaffold = "nano-agent" if base.startswith("nano-agent-") else "r2e-gym"
    model_key = base[len(scaffold) + 1:]
    default_temp = 1.0 if "DeepSWE" in model_key or "deepswe" in model_key.lower() else 0.2 if "devstral" in model_key.lower() else 0.6
    return {"config": name, "scaffold": scaffold, "model": MODELS.get(model_key, model_key),
            "temperature": 0.0 if temp0 else default_temp}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("index")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    runs: dict[str, dict[int, Path]] = defaultdict(dict)
    base = Path(a.index).resolve().parent
    for e in json.loads(Path(a.index).read_text()):
        f = Path(e["file"])
        runs[e["config"]][int(e["run"])] = f if f.is_absolute() else base / f
    out = Path(a.out)
    total = 0
    for cfg, byrun in sorted(runs.items()):
        meta = parse_config(cfg)
        d = out / cfg
        d.mkdir(parents=True, exist_ok=True)
        n_runs = len(byrun)
        for run_idx, path in sorted(byrun.items()):
            r = json.loads(path.read_text())
            verdicts = {}
            for iid in r.get("resolved_ids", []):
                verdicts[iid] = (1.0, "resolved", "completed")
            for iid in r.get("unresolved_ids", []):
                verdicts.setdefault(iid, (0.0, "unresolved", "completed"))
            for iid in r.get("empty_patch_ids", []):
                verdicts.setdefault(iid, (0.0, "empty_patch", "completed"))
            for iid in r.get("error_ids", []):
                verdicts.setdefault(iid, (None, "harness_error", "error"))
            for iid in r.get("incomplete_ids", []):
                verdicts.setdefault(iid, (None, None, "unknown"))
            for iid in r.get("submitted_ids", []) or r.get("completed_ids", []):
                verdicts.setdefault(iid, (None, None, "unknown"))
            for iid, (score, reason, outcome) in verdicts.items():
                m = {
                    "task_id": iid,
                    "serving": {"provider": "self-hosted vLLM (from file names)", "observed_provider": "unrecorded",
                                "observed_provider_source": "unrecorded"},
                    "env": {"image_digest": "unrecorded", "taskset_commit": "unrecorded"},
                    "run": {"repetition_index": run_idx + 1, "total_repetitions": n_runs},
                    "sampling": {"temperature": meta["temperature"]},
                    "steps": [],
                    "verdict": {"criteria_version": f"swebench-harness-schema-v{r.get('schema_version', '?')}",
                                "score": score, "reason": reason, "basis": "test_suite (FAIL_TO_PASS + PASS_TO_PASS)"},
                    "outcome": {"reason": outcome},
                    "harness": {"silent_retries": 0},
                    "artefacts": {"observations": "per_step", "location": f"{SRC}/tree/main/{cfg}"},
                    "usage": {"completion_tokens": None, "prompt_tokens": None,
                              "per_step_unavailable_reason": "token usage is in the trajectory files, not fetched here"},
                    "scaffold": meta["scaffold"], "model": meta["model"], "config": cfg,
                }
                (d / f"{iid}__r{run_idx + 1:02d}.json").write_text(json.dumps(m) + "\n")
                total += 1
    print(f"wrote {total} manifest(s) for {len(runs)} configuration(s) to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
