#!/usr/bin/env python3
"""Compare the published thresholds in results/ with the exact value.

    python3 results/check_exact.py

The tables in results/ were computed before reference/analyze.py switched its
threshold from a 10,000-draw simulated SD to the exact Bernoulli SD. For every
result file that stores per-task pass counts (and no strata), this recomputes
the exact 95% threshold and prints the difference. Result sets that store only
summaries (Terminal-Bench 2.0, MCPMark, METR) cannot be checked this way.
"""
import glob, json, math, sys
from pathlib import Path

Z95 = 1.959963984540054
ROOT = Path(__file__).resolve().parent


def main() -> int:
    rows = []
    for f in sorted(glob.glob(str(ROOT / "**" / "*.json"), recursive=True)):
        try:
            d = json.loads(Path(f).read_text())
        except (ValueError, OSError):
            continue
        a = d.get("analysis") if isinstance(d, dict) else None
        if not a or not a.get("tasks") or a.get("suite_extrapolation"):
            continue
        dd = a.get("detectable_difference") or {}
        if "mdd95_pp" not in dd or "plugin" not in str(dd.get("basis", "plugin")):
            continue
        ps = [t["passes"] / t["n_scored"] for t in a["tasks"] if t.get("n_scored")]
        exact = Z95 * math.sqrt(2) * 100 * math.sqrt(sum(p * (1 - p) for p in ps)) / len(ps)
        rows.append((Path(f).relative_to(ROOT).as_posix(), dd["mdd95_pp"], exact))
    if not rows:
        print("no checkable result files")
        return 1
    print(f"{'result':60s} {'published':>9s} {'exact':>7s} {'diff':>6s}")
    for name, pub, ex in rows:
        print(f"{name:60s} {pub:9.2f} {ex:7.2f} {pub - ex:+6.2f}")
    diffs = sorted(abs(p - e) for _, p, e in rows)
    print(f"\n{len(rows)} result files; |published - exact| max {diffs[-1]:.2f}, median {diffs[len(diffs) // 2]:.2f} points")
    return 0


if __name__ == "__main__":
    sys.exit(main())
