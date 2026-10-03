#!/usr/bin/env python3
"""MobileWorld -> evidence-manifest.

Reads the orchestrator's runs.jsonl (one row per run) plus traj_stats.json
(per-run token usage recovered from traj.json) and emits one manifest per run.

What this adapter cannot fill, and says so:
  steps[].completion_tokens  MobileWorld records one token_usage per run, not
                             per step. The manifest carries the run total under
                             `usage` with per_step_unavailable_reason set. This
                             is the field the spec most wants and the flagship
                             benchmark cannot provide -- which is the point.
  serving.observed_provider  Only present if the agent logged it (our pinned
                             agent does; the stock agents do not).
  artefacts.observations     'per_step' only for runs listed in --retained
                             (arm/task/trial_NNN lines, e.g. produced from a
                             tar listing of the kept screenshots); 'none'
                             otherwise. The harness captured a screenshot per
                             step for every run; what was kept is what counts.
  verdict.reason             MobileWorld writes "No reason provided for <Task>"
                             when the verifier gave none. That is a placeholder,
                             not a reason, and is emitted as null.

    python3 adapters/mobileworld.py --runs runs.jsonl --traj traj_stats.json --retained screenshots_retained.txt --out examples/
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def outcome_reason(row: dict) -> str:
    if row.get("outcome") == "scored":
        steps, cap = row.get("steps"), row.get("max_round")
        if isinstance(steps, int) and isinstance(cap, int) and steps >= cap and not row.get("pass"):
            return "budget_exhausted"
        return "completed"
    if row.get("outcome") in ("env_unhealthy", "timeout"):
        return "error"
    return "unknown"


def clean_reason(r):
    if not r or str(r).strip().startswith("No reason provided"):
        return None
    return r


def to_manifest(row: dict, usage: dict | None, total_reps: int, retained: set | None = None) -> dict:
    pm = row.get("model_params") or {}
    key = f"{row.get('arm')}/{row.get('task_id')}/trial_{int(row.get('trial_index', 0)):03d}"
    kept = bool(retained) and key in retained
    m = {
        "serving": {
            "provider": pm.get("or_provider") or "unpinned",
            # Must be read back off the response. runs.jsonl does not carry it
            # (the pinned agent logs it to thread_*.log, not to the row), so
            # unless a caller has joined that in as `served_by`, it is
            # unrecorded. Never fall back to the declared provider: that would
            # turn an observation into a claim, which is the failure the spec
            # exists to prevent.
            "observed_provider": row.get("served_by") or "unrecorded",
            # runs.jsonl never carries a read-back value; a caller that joins
            # thread_*.log 'SERVED BY' lines in as `served_by` gets 'log'.
            "observed_provider_source": "log" if row.get("served_by") else "unrecorded",
            "quantization": pm.get("or_quant"),
        },
        "env": {
            "image_digest": "sha256:" + (row.get("image_digest") or ""),
            "taskset_commit": row.get("taskset_commit") or "",
        },
        "run": {
            "repetition_index": row["trial_index"],
            "total_repetitions": total_reps,
            "started_at": row.get("started_at"),
            "ended_at": row.get("ended_at"),
        },
        "sampling": {k: v for k, v in (("temperature", pm.get("temperature")), ("seed", pm.get("seed")))
                     if v is not None},
        "steps": [],
        "verdict": {
            "criteria_version": row.get("taskset_commit") or "",
            "score": row.get("score"),
            "reason": clean_reason(row.get("reason")),
        },
        "outcome": {"reason": outcome_reason(row)},
        "harness": {"silent_retries": row.get("absorbed_retries") or 0},
        "artefacts": ({"observations": "per_step", "location": f"archive/artifacts-shots.tar.gz:runs/{key}"}
                      if kept else {"observations": "none"}),
        "task_id": row["task_id"],
    }
    for k in ("temperature", "seed"):
        if k in m["sampling"]:
            try:
                m["sampling"][k] = float(m["sampling"][k]) if k == "temperature" else int(m["sampling"][k])
            except (TypeError, ValueError):
                del m["sampling"][k]
    if usage:
        m["usage"] = {
            "completion_tokens": int(usage.get("completion_tokens") or 0),
            "prompt_tokens": int(usage.get("prompt_tokens") or 0),
            "per_step_unavailable_reason": "MobileWorld's trajectory logger records one token_usage per run, not per step.",
        }
    else:
        # No token_usage was recovered for this run at all (no traj.json, or a
        # traj.json without the field). A null with a reason; never a zero.
        m["usage"] = {
            "completion_tokens": None,
            "prompt_tokens": None,
            "per_step_unavailable_reason": f"no token_usage recorded for this run (outcome: {row.get('outcome')})",
        }
    if not m["serving"]["quantization"]:
        del m["serving"]["quantization"]
    return m


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runs", required=True)
    ap.add_argument("--traj", default=None)
    ap.add_argument("--arm", default=None)
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--retained", default=None,
                    help="file of arm/task/trial_NNN lines whose per-step observations are retained")
    a = ap.parse_args()

    rows = [json.loads(l) for l in Path(a.runs).read_text().splitlines() if l.strip()]
    if a.arm:
        rows = [r for r in rows if r.get("arm") == a.arm]
    usage_by = {}
    if a.traj:
        for r in json.loads(Path(a.traj).read_text()).get("runs", []):
            if not r.get("is_backup"):
                usage_by[(r["arm"], r["task_id"], r["trial"])] = r
    retained = set()
    if a.retained:
        retained = {l.strip() for l in Path(a.retained).read_text().splitlines() if l.strip()}
    total = max((r["trial_index"] for r in rows), default=0)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    n = 0
    for r in rows[: a.limit]:
        m = to_manifest(r, usage_by.get((r["arm"], r["task_id"], r["trial_index"])), total, retained)
        (out / f"{r['arm']}__{r['task_id']}__r{r['trial_index']:02d}.json").write_text(json.dumps(m, indent=2) + "\n")
        n += 1
    print(f"wrote {n} manifest(s) to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
