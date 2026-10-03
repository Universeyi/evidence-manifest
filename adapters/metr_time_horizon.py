#!/usr/bin/env python3
"""METR time-horizon raw runs -> evidence-manifest, one manifest per run.

METR publishes the per-run records behind its time-horizon reports
(github.com/METR/eval-analysis-public, reports/time-horizon-1-x/data/raw/runs.jsonl):
one row per (agent alias, task, run) with a binarized score, a continuous
score, tokens, start and end timestamps, the task version, and whether the run
hit a usage limit. That is enough for a noise floor per agent, and the only
public multi-run set that also carries tokens and timestamps for every run.

What maps where:
  task_id                      task_id (family/name); task_source kept as a field
  run.repetition_index         order of started_at within (alias, task); total = runs in the cell
  verdict.score                score_binarized (0/1); score_cont kept as a field
  verdict.criteria_version     task_version (per task, as METR records it)
  outcome.reason               fatal_error_from: None -> completed; usageLimits ->
                               budget_exhausted; serverOrTask -> error; else unknown
  serving                      model id from the alias; not read back -> unrecorded
  env.image_digest             'unrecorded' (METR runs tasks in containers; digests are not in the file)
  usage                        tokens_count as a run total (completion vs prompt not split)
  artefacts.observations       'none' -- transcripts are not published

Suite score here is the UNWEIGHTED per-task success rate over the tasks the
agent ran; METR's headline (the 50% time horizon) weights tasks by family and
human time. This is a noise floor for the raw success rate, not for the horizon.

    python3 adapters/metr_time_horizon.py runs.jsonl --out manifests/metr-1-1/
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

SRC = "https://github.com/METR/eval-analysis-public"
FATAL = {None: "completed", "None": "completed", "usageLimits": "budget_exhausted", "serverOrTask": "error"}


def ts(ms):
    try:
        return datetime.fromtimestamp(float(ms) / 1000, tz=timezone.utc).isoformat(timespec="seconds")
    except (TypeError, ValueError):
        return None


def slug(s: str) -> str:
    return "".join(c if c.isalnum() or c in "-._" else "_" for c in s)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("runs_jsonl")
    ap.add_argument("--out", required=True)
    ap.add_argument("--report", default="time-horizon", help="label for artefacts.location")
    a = ap.parse_args()
    cells: dict[tuple, list[dict]] = defaultdict(list)
    for line in Path(a.runs_jsonl).read_text().splitlines():
        if line.strip():
            r = json.loads(line)
            cells[(r["alias"], r["task_id"])].append(r)
    out = Path(a.out)
    n = 0
    for (alias, task), rs in cells.items():
        rs.sort(key=lambda r: float(r.get("started_at") or 0))
        d = out / slug(alias)
        d.mkdir(parents=True, exist_ok=True)
        for i, r in enumerate(rs, 1):
            fatal = r.get("fatal_error_from")
            outcome = FATAL.get(fatal, "unknown")
            sb = r.get("score_binarized")
            score = float(sb) if sb is not None and outcome != "error" else None
            tokens = r.get("tokens_count")
            m = {
                "task_id": task,
                "serving": {"provider": "vendor api (from alias; not in the record)", "observed_provider": "unrecorded",
                            "observed_provider_source": "unrecorded"},
                "env": {"image_digest": "unrecorded", "taskset_commit": "unrecorded"},
                "run": {"repetition_index": i, "total_repetitions": len(rs),
                        "started_at": ts(r.get("started_at")), "ended_at": ts(r.get("completed_at"))},
                "steps": [],
                "verdict": {"criteria_version": str(r.get("task_version") or "unrecorded"), "score": score,
                            "reason": None, "basis": "task_scorer"},
                "outcome": {"reason": outcome},
                "harness": {"silent_retries": 0},
                "artefacts": {"observations": "none"},
                "usage": ({"completion_tokens": int(float(tokens)), "prompt_tokens": None,
                           "per_step_unavailable_reason": "METR records one tokens_count per run; prompt/completion not split"}
                          if tokens not in (None, "", "None") else
                          {"completion_tokens": None, "prompt_tokens": None,
                           "per_step_unavailable_reason": "no tokens_count in the record"}),
                "alias": alias, "model": r.get("model"), "scaffold": r.get("scaffold"),
                "task_source": r.get("task_source"), "task_family": r.get("task_family"),
                "score_cont": r.get("score_cont"), "human_minutes": r.get("human_minutes"),
                "fatal_error_from": fatal, "run_id": r.get("run_id"),
                "artefacts_note": f"{SRC} reports/{a.report}/data/raw/runs.jsonl",
            }
            (d / f"{slug(task)}__r{i:02d}.json").write_text(json.dumps(m) + "\n")
            n += 1
    print(f"wrote {n} manifest(s) for {len({k[0] for k in cells})} agent(s) to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
