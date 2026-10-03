#!/usr/bin/env python3
"""analyze.py must reproduce the audit paper's figures from the audit's own
manifests, to the last decimal. No pytest needed:

    python3 tests/test_regression.py
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    exp = json.loads((ROOT / "tests" / "expected_mobileworld_audit.json").read_text())
    st = exp["settings"]
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "a.json"
        subprocess.run([sys.executable, str(ROOT / "reference" / "analyze.py"),
                        str(ROOT / "examples" / "mobileworld-audit"), "--rounds", st["rounds"],
                        "--strata", str(ROOT / st["strata"]), "--seed", str(st["seed"]),
                        "--resamples", str(st["resamples"]), "--out", str(out)],
                       check=True, capture_output=True)
        a = json.loads(out.read_text())["analysis"]
    got = {
        "per_round_scores": [p["score_pct"] for p in a["per_round_suite_score"]["per_round"]],
        "observed_range_pp": a["per_round_suite_score"]["observed_range_pp"],
        "n_flipped": a["flips"]["n_flipped"],
        "flipped_task_ids": a["flips"]["flipped_task_ids"],
        "mean_flip_rate": a["flips"]["mean_flip_rate"],
        "rerun_plugin_sd": a["rerun"]["plugin"]["sd_pp"],
        "rerun_posterior_sd": a["rerun"]["posterior"]["sd_pp"],
        "bootstrap_sd": a["estimate"]["sd_pp"],
        "fixed_taskset_sd": a["suite_extrapolation"]["fixed_taskset"]["sd_pp"],
        "fixed_taskset_ci95_width": a["suite_extrapolation"]["fixed_taskset"]["ci95_width_pp"],
        "resampled_tasks_sd": a["suite_extrapolation"]["resampled_tasks"]["sd_pp"],
        "mdd95_pp": a["detectable_difference"]["mdd95_pp"],
        "mdd95_power80_pp": a["detectable_difference"]["mdd95_power80_pp"],
        "loo_mdd_min": a["leave_one_out"]["mdd95_pp_min"],
        "loo_mdd_max": a["leave_one_out"]["mdd95_pp_max"],
        "loo_n_flipped": [v["n_flipped"] for v in a["leave_one_out"]["variants"]],
    }
    bad = [(k, got[k], v) for k, v in exp["expected"].items() if got.get(k) != v]
    for k, g, e in bad:
        print(f"DIFF {k}: got {g}, expected {e}")
    print(f"{len(exp['expected']) - len(bad)}/{len(exp['expected'])} figures reproduce the paper")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
