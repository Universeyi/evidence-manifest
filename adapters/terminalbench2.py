#!/usr/bin/env python3
"""Terminal-Bench 2.0 leaderboard trials -> evidence-manifest, one manifest per trial.

Source: the leaderboard at tbench.ai requires at least five trials per task and
publishes a per-trial result and trajectory. A complete scrape of it is on
Hugging Face as `yoonholee/terminalbench-trajectories` (Apache-2.0): one row
per trial, 52,104 rows, 109 (agent, model) configurations x 89 tasks. This
adapter reads those parquet shards (pyarrow) and groups manifests by
configuration.

What maps where, and what the scrape does not carry:
  task_id                      task_name
  run.repetition_index         1..n by started_at within (agent, model, task);
                               total_repetitions = trials in that cell
  verdict.score                reward (0/1); no reason string in the scrape
  verdict.criteria_version     'unrecorded' -- the original per-trial
                               result.json carries the task git commit and
                               checksum; the scrape dropped them
  env.image_digest             'unrecorded' -- containerized, digest not kept
  outcome.reason               'completed': the leaderboard counts every trial
                               in its denominator, and the scrape has no
                               exception field to say otherwise
  usage                        run-level output_tokens where present (per-step
                               metrics were not scraped); null with a reason
                               otherwise
  artefacts.observations       per_step where the steps column is non-null
                               (messages, tool calls and observations), else
                               none

    python3 adapters/terminalbench2.py p0.parquet p1.parquet --out manifests/tb2/
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

SRC = "https://huggingface.co/datasets/yoonholee/terminalbench-trajectories"


def slug(s: str) -> str:
    return "".join(c if c.isalnum() or c in "-._" else "_" for c in s)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("parquet", nargs="+")
    ap.add_argument("--out", required=True)
    ap.add_argument("--min-trials", type=int, default=1)
    a = ap.parse_args()
    try:
        import pyarrow.parquet as pq
    except ImportError:
        raise SystemExit("needs pyarrow:  pip install pyarrow")

    cells: dict[tuple, list[dict]] = defaultdict(list)
    cols = ["task_name", "agent", "model", "reward", "duration_seconds", "input_tokens", "output_tokens",
            "cache_tokens", "trial_id", "started_at", "ended_at", "steps"]
    for p in a.parquet:
        pf = pq.ParquetFile(p)
        for batch in pf.iter_batches(batch_size=500, columns=cols):
            rows = batch.to_pylist()
            for r in rows:
                r["has_steps"] = bool(r.get("steps")) and r["steps"] != "null"
                r.pop("steps", None)
                cells[(r["agent"], r["model"], r["task_name"])].append(r)

    out = Path(a.out)
    n = 0
    for (agent, model, task), trs in cells.items():
        if len(trs) < a.min_trials:
            continue
        trs.sort(key=lambda r: r.get("started_at") or "")
        vendor = model.split("@")[-1] if "@" in model else "vendor-api"
        d = out / f"{slug(agent)}__{slug(model)}"
        d.mkdir(parents=True, exist_ok=True)
        for i, r in enumerate(trs, 1):
            ot = r.get("output_tokens")
            m = {
                "task_id": task,
                "serving": {"provider": f"{vendor} (vendor api)", "observed_provider": "unrecorded",
                            "observed_provider_source": "unrecorded"},
                "env": {"image_digest": "unrecorded", "taskset_commit": "unrecorded"},
                "run": {"repetition_index": i, "total_repetitions": len(trs),
                        "started_at": r.get("started_at"), "ended_at": r.get("ended_at")},
                "steps": [],
                "verdict": {"criteria_version": "unrecorded", "score": float(r["reward"]) if r.get("reward") is not None else None,
                            "reason": None, "basis": "test_suite"},
                "outcome": {"reason": "completed"},
                "harness": {"silent_retries": 0},
                "artefacts": ({"observations": "per_step", "location": SRC} if r["has_steps"]
                              else {"observations": "none"}),
                "usage": ({"completion_tokens": int(ot), "prompt_tokens": int(r.get("input_tokens") or 0),
                           "per_step_unavailable_reason": "the scrape keeps run totals only"}
                          if ot is not None else
                          {"completion_tokens": None, "prompt_tokens": None,
                           "per_step_unavailable_reason": "no token usage in the released record for this trial"}),
                "agent": agent, "model": model, "trial_id": r.get("trial_id"),
                "duration_seconds": r.get("duration_seconds"),
            }
            (d / f"{slug(task)}__r{i:02d}.json").write_text(json.dumps(m) + "\n")
            n += 1
    print(f"wrote {n} manifest(s) for {len({k[:2] for k in cells})} configurations to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
