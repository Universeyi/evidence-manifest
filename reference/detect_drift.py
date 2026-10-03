#!/usr/bin/env python3
"""Screen a per-round series for a step change.

Given per-round values of a signal (typically the median of completion tokens
per action within each repetition round), report every candidate boundary with
the size of the step relative to the spread inside the two segments it creates.

This is a screen, not a test. It does not choose a boundary and then claim
significance for it -- searching for the largest step and reporting its p-value
manufactures a finding out of noise. What it does is make a step visible so a
person can go and look for the identifiable event that explains it. A boundary
that stands out here is a place to start, not a conclusion.

    python3 detect_drift.py series.json
    python3 detect_drift.py --from-manifests runs/*.json
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path


def _ss(xs):
    m = sum(xs) / len(xs)
    return sum((x - m) ** 2 for x in xs)


def screen(series: list[float], min_segment: int = 2) -> list[dict]:
    """Binary segmentation: for every split, how much of the series' total
    variation is explained by a single step there.

    The criterion is the reduction in within-segment sum of squares, the
    standard single-change-point statistic. A median/MAD version was tried
    first and preferred an off-centre boundary, because MAD ignores the very
    outliers that a misplaced boundary leaves inside a segment. Sum of squares
    does not."""
    n = len(series)
    total = _ss(series) or 1e-9
    out = []
    for b in range(min_segment, n - min_segment + 1):
        left, right = series[:b], series[b:]
        within = _ss(left) + _ss(right)
        lm, rm = sum(left) / len(left), sum(right) / len(right)
        out.append({
            "boundary_after_round": b,
            "left_mean": round(lm, 3),
            "right_mean": round(rm, 3),
            "step": round(rm - lm, 3),
            "step_pct": round(100 * (rm - lm) / lm, 2) if lm else None,
            "variance_explained": round(1 - within / total, 4),
        })
    return sorted(out, key=lambda r: -r["variance_explained"])


def series_from_manifests(paths) -> list[float]:
    """Median completion tokens per step, per repetition round."""
    by_round: dict[int, list[float]] = {}
    for p in paths:
        m = json.loads(Path(p).read_text())
        steps = m.get("steps") or []
        if not steps:
            continue
        per = sum(s.get("completion_tokens", 0) for s in steps) / len(steps)
        by_round.setdefault(m["run"]["repetition_index"], []).append(per)
    return [statistics.median(v) for _, v in sorted(by_round.items())]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inputs", nargs="+")
    ap.add_argument("--from-manifests", action="store_true",
                    help="inputs are manifest files; build the per-round series from them")
    ap.add_argument("--top", type=int, default=3)
    a = ap.parse_args()

    if a.from_manifests:
        series = series_from_manifests(a.inputs)
    else:
        series = json.loads(Path(a.inputs[0]).read_text())
        if isinstance(series, dict):
            series = [series[k] for k in sorted(series, key=int)]
    if len(series) < 4:
        print("need at least 4 rounds", file=sys.stderr); return 2

    print("series:", [round(x, 1) for x in series])
    print(f"\n{'boundary':>9} {'left':>8} {'right':>8} {'step':>8} {'%':>7} {'var.expl':>9}")
    for r in screen(series)[: a.top]:
        print(f"after r{r['boundary_after_round']:<3} {r['left_mean']:>8} {r['right_mean']:>8} "
              f"{r['step']:>8} {r['step_pct'] if r['step_pct'] is not None else '':>7} {r['variance_explained']:>9}")
    print("\nA high value marks where to look for an identifiable event. It is not evidence of one.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
