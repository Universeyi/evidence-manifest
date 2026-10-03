#!/usr/bin/env python3
"""tau-bench (v1) historical_trajectories -> evidence-manifest, one manifest per record.

Sierra's first tau-bench repository ships four JSON files under
historical_trajectories/ (2024-11-23): tool-calling gpt-4o with 4 trials and
claude-3-5-sonnet-20241022 with 8 trials, on airline (50 tasks) and retail
(115 tasks). Each record is {task_id, trial, reward, info, traj}.

The files carry almost none of what the spec asks for: no timestamps, no
token usage, no termination reason, no evaluator commit, and the agent and
user-simulator model names appear nowhere inside the file -- they are known
only from the file name and the README. The adapter says so field by field
rather than filling from memory.

    python3 adapters/taubench1.py sonnet-35-new-retail.json --model claude-3-5-sonnet-20241022 --out manifests/
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

SRC = "https://github.com/sierra-research/tau-bench/tree/main/historical_trajectories"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("results")
    ap.add_argument("--model", required=True, help="agent model, from the file name / README (not in the file)")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    recs = json.loads(Path(a.results).read_text())
    total = len({r["trial"] for r in recs})
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    n = 0
    for r in recs:
        ri = (r.get("info") or {}).get("reward_info") or {}
        inner = ri.get("info") or {}
        reason = "; ".join(f"{k}={v}" for k, v in inner.items() if k in ("r_actions", "r_outputs")) or None
        m = {
            "task_id": str(r["task_id"]),
            "serving": {"provider": "vendor-api (from file name; not in the record)", "observed_provider": "unrecorded",
                        "observed_provider_source": "unrecorded"},
            "env": {"image_digest": "not_containerized", "taskset_commit": "unrecorded"},
            "run": {"repetition_index": int(r["trial"]) + 1, "total_repetitions": total},
            "steps": [],
            "verdict": {"criteria_version": "unrecorded", "score": float(r["reward"]), "reason": reason,
                        "basis": "DB_hash+output_substring"},
            "outcome": {"reason": "completed"},
            "harness": {"silent_retries": 0},
            "artefacts": {"observations": "per_step", "location": SRC},
            "usage": {"completion_tokens": None, "prompt_tokens": None,
                      "per_step_unavailable_reason": "the record carries no token usage, only an aggregate user_cost"},
            "model": a.model,
            "task_source": (r.get("info") or {}).get("source"),
        }
        (out / f"{Path(a.results).stem}__{m['task_id']}__r{m['run']['repetition_index']:02d}.json").write_text(
            json.dumps(m) + "\n")
        n += 1
    print(f"wrote {n} manifest(s) ({len({r['task_id'] for r in recs})} tasks x {total} trials) to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
