#!/usr/bin/env python3
"""The consumer. Read a directory of manifests, report the noise floor.

    python3 reference/analyze.py manifests/ --out analysis.json --md analysis.md
    python3 reference/analyze.py manifests/ --rounds 4-10 --exclude-rounds 6 \\
        --strata strata.json                      # the audit's own settings
    python3 reference/analyze.py manifests/ --measured-is-suite
                                                  # every task of the suite was run

What comes out, and where each number comes from:

  per task        pass rate with a Wilson 95% interval; flip rate = discordant
                  trial pairs / all pairs
  per round       the suite score of each repetition -- the assumption-free
                  measurement; if round 3 scored 48 and round 7 scored 55,
                  that happened on identical inputs
  re-run          where an independent re-run of the suite would land:
                  Bernoulli at the measured rate per task (plugin), and with
                  the rate itself drawn from its Jeffreys posterior
  estimate        bootstrap precision of this experiment's own number
  MDD             how far apart two single runs must be before the gap is
                  outside noise (95%), and for 80% power
  leave-one-out   every figure above with each round dropped in turn
  adjudicability  how many verdicts a person could still re-examine
  drift screen    per-round median completion tokens, binary segmentation

Denominators follow the spec's consumer contract: a manifest whose
outcome.reason is `unknown` is never counted; `error` has no verdict and is
not counted; `completed` and `budget_exhausted` are. A pass is
verdict.score > --pass-threshold.

The resampling is seeded and the port is exact: on the 314 manifests of the
MobileWorld audit, with the audit's settings, this file reproduces the paper's
figures to the last decimal (see tests/test_regression.py).
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import random
import statistics
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from detect_drift import screen as drift_screen  # noqa: E402

Z95 = 1.959963984540054
Z80_POWER = 0.8416212335729143
MIN_TASKS_FOR_CLAIMS = 5
MIN_TRIALS_FOR_CLAIMS = 3
SCORED_OUTCOMES = ("completed", "budget_exhausted")


# ------------------------------------------------------------------ statistics

def wilson(k: int, n: int, z: float = Z95) -> tuple[float, float]:
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    denom = 1.0 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (max(0.0, centre - half), min(1.0, centre + half))


def flip_rate(k: int, n: int) -> float | None:
    if n < 2:
        return None
    return k * (n - k) / (n * (n - 1) / 2)


def flip_rate_max(n: int) -> float | None:
    if n < 2:
        return None
    return (n // 2) * ((n + 1) // 2) / (n * (n - 1) / 2)


def pct(xs: list[float], q: float) -> float:
    if not xs:
        return float("nan")
    s = sorted(xs)
    if len(s) == 1:
        return s[0]
    pos = q * (len(s) - 1)
    lo, hi = math.floor(pos), math.ceil(pos)
    if lo == hi:
        return s[lo]
    return s[lo] + (s[hi] - s[lo]) * (pos - lo)


def summarize(xs: list[float]) -> dict:
    xs = [x for x in xs if x is not None]
    if not xs:
        return {"n": 0}
    return {"n": len(xs), "mean": round(statistics.fmean(xs), 4),
            "sd": round(statistics.stdev(xs), 4) if len(xs) > 1 else 0.0,
            "min": round(min(xs), 4), "p05": round(pct(xs, 0.05), 4),
            "median": round(pct(xs, 0.5), 4), "p95": round(pct(xs, 0.95), 4),
            "max": round(max(xs), 4)}


# ------------------------------------------------------------------- manifests

def load_manifests(inputs: list[str]) -> list[dict]:
    paths: list[Path] = []
    for inp in inputs:
        p = Path(inp)
        if p.is_dir():
            paths += sorted(p.glob("*.json"))
        else:
            paths += [Path(x) for x in sorted(glob.glob(inp))]
    out = []
    for p in paths:
        m = json.loads(p.read_text())
        m["_path"] = str(p)
        out.append(m)
    return out


def row_of(m: dict, threshold: float) -> dict:
    """Flatten one manifest to what the analysis needs."""
    reason = (m.get("outcome") or {}).get("reason")
    score = (m.get("verdict") or {}).get("score")
    scored = reason in SCORED_OUTCOMES and isinstance(score, (int, float))
    steps = m.get("steps") or []
    usage = m.get("usage") or {}
    if steps:
        per_step = sum(s.get("completion_tokens", 0) for s in steps) / len(steps)
        tokens_basis = "per_step_mean"
    elif usage.get("completion_tokens") is not None:
        per_step = float(usage["completion_tokens"])
        tokens_basis = "run_total"
    else:
        per_step, tokens_basis = None, None
    af = m.get("artefacts") or {}
    vreason = (m.get("verdict") or {}).get("reason")
    return {
        "task_id": m.get("task_id"),
        "round": (m.get("run") or {}).get("repetition_index"),
        "outcome": reason,
        "score": score,
        "scored": scored,
        "pass": bool(scored and score > threshold),
        "steps_n": len(steps) or None,
        "completion_tokens": per_step,
        "tokens_basis": tokens_basis,
        "silent_retries": (m.get("harness") or {}).get("silent_retries") or 0,
        "adjudicable": not (af.get("observations") == "none" and not (vreason or "").strip()),
        "observations": af.get("observations"),
        "criteria_version": (m.get("verdict") or {}).get("criteria_version"),
        "basis": (m.get("verdict") or {}).get("basis"),
        "path": m.get("_path"),
    }


# ---------------------------------------------------------------- per task/round

def per_task(rows: list[dict], strata_of: dict[str, str]) -> list[dict]:
    by_task: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_task[r["task_id"]].append(r)
    out = []
    for task_id, trs in sorted(by_task.items()):
        trs.sort(key=lambda r: r["round"] or 0)
        scored = [r for r in trs if r["scored"]]
        k = sum(1 for r in scored if r["pass"])
        n = len(scored)
        lo, hi = wilson(k, n)
        bases = Counter(r["basis"] for r in trs if r.get("basis"))
        out.append({
            "task_id": task_id,
            "stratum": strata_of.get(task_id),
            "basis": bases.most_common(1)[0][0] if bases else None,
            "n_runs": len(trs),
            "n_scored": n,
            "n_unscored": len(trs) - n,
            "unscored_outcomes": dict(Counter(r["outcome"] for r in trs if not r["scored"])),
            "passes": k,
            "pass_rate": round(k / n, 4) if n else None,
            "wilson95": [round(lo, 4), round(hi, 4)],
            "wilson95_width": round(hi - lo, 4),
            "flipped": bool(n >= 2 and 0 < k < n),
            "flip_rate": round(flip_rate(k, n), 4) if flip_rate(k, n) is not None else None,
            "flip_rate_max": round(flip_rate_max(n), 4) if flip_rate_max(n) is not None else None,
            "n_unadjudicable": sum(1 for r in trs if not r["adjudicable"]),
            "silent_retries": sum(r["silent_retries"] for r in trs),
            "trial_outcomes": [{"round": r["round"], "outcome": r["outcome"], "score": r["score"],
                                "pass": r["pass"] if r["scored"] else None} for r in trs],
        })
    return out


def per_round_suite_scores(rows: list[dict]) -> dict:
    by_round: dict[int, list[dict]] = defaultdict(list)
    for r in rows:
        by_round[r["round"]].append(r)
    per = []
    for rd in sorted(by_round):
        trs = by_round[rd]
        scored = [r for r in trs if r["scored"]]
        if not scored:
            continue
        k = sum(1 for r in scored if r["pass"])
        per.append({"round": rd, "n_tasks_attempted": len(trs), "n_tasks_scored": len(scored),
                    "n_passed": k, "score_pct": round(100 * k / len(scored), 4)})
    attempted = max((p["n_tasks_attempted"] for p in per), default=0)
    for p in per:
        p["complete"] = p["n_tasks_attempted"] == attempted
        p["reduced_denominator"] = p["complete"] and p["n_tasks_scored"] < p["n_tasks_attempted"]
    complete = [p for p in per if p["complete"]]
    scores = [p["score_pct"] for p in complete]
    gaps = [abs(x - y) for i, x in enumerate(scores) for y in scores[i + 1:]]
    return {"per_round": per, "n_rounds_complete": len(complete),
            "n_rounds_partial": len(per) - len(complete),
            "tasks_per_complete_round": attempted,
            "summary": summarize(scores),
            "observed_range_pp": round(max(scores) - min(scores), 4) if scores else None,
            "pairwise_abs_difference_pp": summarize(gaps),
            "note": "Rounds that attempted fewer tasks than the fullest round are still in "
                    "progress and are excluded; rounds that attempted every task but scored "
                    "fewer are kept and flagged."}


# ------------------------------------------------------------------- resampling

def _bernoulli_suite(rng, ps, n):
    hist: Counter = Counter()
    for _ in range(n):
        hist[sum(1 for p in ps if rng.random() < p)] += 1
    return hist


def _hist_stats(hist: Counter, n_slots: int) -> dict:
    total = sum(hist.values())
    xs = []
    for c, cnt in sorted(hist.items()):
        xs += [100.0 * c / n_slots] * cnt
    lo, hi = pct(xs, 0.025), pct(xs, 0.975)
    return {"n_slots": n_slots, "n_resamples": total,
            "mean_pct": round(statistics.fmean(xs), 4),
            "sd_pp": round(statistics.stdev(xs), 4) if len(xs) > 1 else 0.0,
            "ci95_pct": [round(lo, 4), round(hi, 4)], "ci95_width_pp": round(hi - lo, 4),
            "counts_hist": {str(c): n for c, n in sorted(hist.items())}}


def rerun_distributions(tasks, n_resamples, seed):
    usable = [t for t in tasks if t["n_scored"] > 0]
    ks = [t["passes"] for t in usable]
    ns = [t["n_scored"] for t in usable]
    n_slots = len(usable)
    rng = random.Random(seed)
    plugin = _bernoulli_suite(rng, [k / n for k, n in zip(ks, ns)], n_resamples)
    rng = random.Random(seed + 1)
    post: Counter = Counter()
    for _ in range(n_resamples):
        c = 0
        for k, n in zip(ks, ns):
            p = rng.betavariate(k + 0.5, n - k + 0.5)
            if rng.random() < p:
                c += 1
        post[c] += 1
    return {"plugin": {**_hist_stats(plugin, n_slots),
                       "definition": "Bernoulli(p_hat) per task: noise only, the rate taken as exact."},
            "posterior": {**_hist_stats(post, n_slots),
                          "definition": "p drawn from Jeffreys Beta(k+0.5, n-k+0.5) then Bernoulli(p): "
                                        "includes that p itself is only estimated."}}


def estimate_bootstrap(tasks, n_resamples, seed):
    rng = random.Random(seed + 2)
    outcomes = [[1 if o["pass"] else 0 for o in t["trial_outcomes"] if o["pass"] is not None]
                for t in tasks if t["n_scored"] > 0]
    if not outcomes:
        return {"n_resamples": 0}
    xs = []
    for _ in range(n_resamples):
        acc = 0.0
        for obs in outcomes:
            acc += statistics.fmean(rng.choices(obs, k=len(obs)))
        xs.append(100.0 * acc / len(outcomes))
    lo, hi = pct(xs, 0.025), pct(xs, 0.975)
    return {"n_resamples": n_resamples, "mean_pct": round(statistics.fmean(xs), 4),
            "sd_pp": round(statistics.stdev(xs), 4), "ci95_pct": [round(lo, 4), round(hi, 4)],
            "ci95_width_pp": round(hi - lo, 4),
            "definition": "Trials resampled within each task: the precision of this experiment's "
                          "own estimate, not the spread of a future run."}


def _fill_slots(ps, n_slots):
    return [ps[i % len(ps)] for i in range(n_slots)] if ps else []


def exact_sd_pp(ps) -> float:
    """SD of a suite score (in points) when tasks are independent Bernoullis with rates ps.

    No simulation needed; the simulated SDs elsewhere carry Monte Carlo noise of a few
    hundredths of a point at 10,000 draws, which is why the threshold uses this value.
    """
    ps = list(ps)
    return 100.0 * math.sqrt(sum(p * (1 - p) for p in ps)) / len(ps) if ps else float("nan")


def suite_extrapolation(tasks, sizes: dict[str, int], n_resamples, seed):
    by_bucket: dict[str, list[float]] = defaultdict(list)
    for t in tasks:
        if t["n_scored"] > 0 and t["stratum"]:
            by_bucket[t["stratum"]].append(t["pass_rate"])
    if not by_bucket or not sizes or any(b not in by_bucket for b in sizes):
        return None
    total = sum(sizes.values())
    fixed_ps: list[float] = []
    for b, size in sorted(sizes.items()):
        fixed_ps += _fill_slots(sorted(by_bucket[b]), size)
    rng = random.Random(seed + 3)
    fixed = _bernoulli_suite(rng, fixed_ps, n_resamples)
    rng = random.Random(seed + 4)
    resampled: Counter = Counter()
    for _ in range(n_resamples):
        c = 0
        for b, size in sorted(sizes.items()):
            pool = by_bucket[b]
            ps = pool[:size] if len(pool) >= size else rng.choices(pool, k=size)
            c += sum(1 for p in ps if rng.random() < p)
        resampled[c] += 1
    return {"strata_sizes": sizes,
            "strata_measured": {b: len(v) for b, v in sorted(by_bucket.items())},
            "total_slots": total,
            "fixed_taskset": {**_hist_stats(fixed, total),
                              "sd_pp_exact": round(exact_sd_pp(fixed_ps), 4),
                              "definition": "Stratum rates carried to their real sizes; Bernoulli noise only. "
                                            "This is the width to compare with a leaderboard gap."},
            "resampled_tasks": {**_hist_stats(resampled, total),
                                "definition": "Also resamples which tasks of an under-measured stratum are in "
                                              "the suite; wider, about generalisation not noise."}}


def detectable_difference(sd_pp: float) -> dict:
    diff_sd = sd_pp * math.sqrt(2)
    return {"single_run_sd_pp": round(sd_pp, 4), "difference_sd_pp": round(diff_sd, 4),
            "mdd95_pp": round(Z95 * diff_sd, 4), "mdd95_power80_pp": round((Z95 + Z80_POWER) * diff_sd, 4),
            "definition": {"mdd95_pp": "A gap between two single runs smaller than this is within what noise "
                                       "alone produces 95% of the time when the two are in fact equal.",
                           "mdd95_power80_pp": "The gap needed for a single-run comparison to come out "
                                               "significant 80% of the time."}}


def power_check(tasks) -> dict:
    usable = [t for t in tasks if t["n_scored"] > 0]
    min_trials = min((t["n_scored"] for t in usable), default=0)
    reasons = []
    if len(usable) < MIN_TASKS_FOR_CLAIMS:
        reasons.append(f"only {len(usable)} task(s) produced a score (need {MIN_TASKS_FOR_CLAIMS})")
    if min_trials < MIN_TRIALS_FOR_CLAIMS:
        reasons.append(f"a task has only {min_trials} scored trial(s) (need {MIN_TRIALS_FOR_CLAIMS})")
    return {"sufficient": not reasons, "reasons": reasons, "n_tasks_scored": len(usable),
            "min_scored_trials_per_task": min_trials}


# -------------------------------------------------------------------- drift

def drift(rows: list[dict]) -> dict:
    """Per-round median of completion tokens over the SAME task set in every
    round. Rounds are compared only over tasks present in all of them: when
    repetitions per task are uneven, later rounds contain only the tasks that
    were repeated more, and a median over a different task mix is not a
    series. Found on METR's runs, where round 6 held only the short tasks."""
    by_task_round: dict[str, dict[int, float]] = defaultdict(dict)
    bases = Counter()
    for r in rows:
        if r["completion_tokens"] is not None:
            by_task_round[r["task_id"]][r["round"]] = r["completion_tokens"]
            bases[r["tokens_basis"]] += 1
    all_rounds = sorted({rd for d in by_task_round.values() for rd in d})
    # the largest set of rounds shared by at least half the tasks with data
    rounds: list[int] = []
    for rd in all_rounds:
        have = sum(1 for d in by_task_round.values() if rd in d)
        if have >= max(1, len(by_task_round) // 2):
            rounds.append(rd)
    common = [t for t, d in by_task_round.items() if all(rd in d for rd in rounds)]
    series = [statistics.median(by_task_round[t][rd] for t in common) for rd in rounds] if common else []
    out = {"rounds": rounds, "n_tasks_in_series": len(common), "series": [round(x, 2) for x in series],
           "basis": dict(bases),
           "note": "Median completion tokens per round over the tasks present in every listed round; "
                   "per-step mean where steps[] exists, run total otherwise. A step here is the "
                   "signature of the serving endpoint changing; the screen says where to look, not "
                   "that it happened."}
    if len(series) >= 4:
        top = drift_screen(series)[:3]
        for t in top:
            t["boundary_after_round"] = rounds[t["boundary_after_round"] - 1]
        out["screen_top"] = top
    else:
        out["screen_top"] = []
        out["note"] += " Fewer than 4 rounds: no screen."
    return out


# ------------------------------------------------------------------- analysis

def analyse(rows: list[dict], strata: dict | None, n_resamples: int, seed: int,
            measured_is_suite: bool) -> dict:
    strata_of = (strata or {}).get("tasks", {})
    sizes = (strata or {}).get("sizes", {})
    tasks = per_task(rows, strata_of)
    usable = [t for t in tasks if t["n_scored"] > 0]
    power = power_check(tasks)
    rerun = rerun_distributions(tasks, n_resamples, seed)
    extrap = suite_extrapolation(tasks, sizes, n_resamples, seed) if sizes else None
    # The threshold uses exact SDs (exact_sd_pp); the simulated ones stay for the intervals.
    if extrap:
        sd, basis = extrap["fixed_taskset"]["sd_pp_exact"], "suite_extrapolation.fixed_taskset (exact)"
    elif measured_is_suite:
        sd = round(exact_sd_pp(t["passes"] / t["n_scored"] for t in usable), 4)
        basis = "rerun.plugin, exact (the measured tasks are the whole suite)"
    else:
        sd = round(exact_sd_pp((t["passes"] + 0.5) / (t["n_scored"] + 1) for t in usable), 4)
        basis = ("rerun.posterior, exact (a subset of the suite, no strata: "
                 "overstates the width of the full suite)")
    mdd = {**detectable_difference(sd), "basis": basis}
    if not power["sufficient"]:
        mdd["not_reportable"] = "; ".join(power["reasons"]) + " -- arithmetic, not evidence"
    flips = sorted((t for t in tasks if t["flip_rate"] is not None),
                   key=lambda t: (-t["flip_rate"], t["task_id"]))
    counts = Counter(t["n_scored"] for t in tasks if t["n_scored"] >= 2)
    typical_n = counts.most_common(1)[0][0] if counts else None
    n_unadj = sum(1 for r in rows if not r["adjudicable"])
    by_basis = defaultdict(list)
    for t in usable:
        by_basis[t["basis"] or "unrecorded"].append(t)
    flips_by_basis = {b: {"n_tasks": len(ts), "n_flipped": sum(1 for t in ts if t["flipped"]),
                          "mean_pass_rate": round(statistics.fmean([t["pass_rate"] for t in ts]), 4),
                          "mean_flip_rate": round(statistics.fmean([t["flip_rate"] for t in ts if t["flip_rate"] is not None]), 4)
                          if any(t["flip_rate"] is not None for t in ts) else None}
                      for b, ts in sorted(by_basis.items())}
    return {
        "n_manifests": len(rows),
        "n_tasks": len(tasks),
        "rounds": sorted({r["round"] for r in rows}),
        "outcomes": dict(Counter(r["outcome"] for r in rows)),
        "outcomes_by_round": {str(k): dict(Counter(r["outcome"] for r in rows if r["round"] == k))
                              for k in sorted({r["round"] for r in rows})},
        "criteria_versions": dict(Counter(r["criteria_version"] for r in rows)),
        "per_round_suite_score": per_round_suite_scores(rows),
        "tasks": tasks,
        "flips": {"n_tasks_with_2plus_scored": sum(1 for t in tasks if t["n_scored"] >= 2),
                  "n_flipped": sum(1 for t in tasks if t["flipped"]),
                  "flipped_task_ids": [t["task_id"] for t in tasks if t["flipped"]],
                  "mean_flip_rate": round(statistics.fmean([t["flip_rate"] for t in flips]), 4) if flips else None,
                  "by_basis": flips_by_basis,
                  "n_trials_typical": typical_n,
                  "flip_rate_max_typical": round(flip_rate_max(typical_n), 4) if typical_n else None,
                  "ranked_by_instability": [{k: t[k] for k in ("task_id", "stratum", "passes", "n_scored",
                                                                "pass_rate", "flip_rate", "wilson95")}
                                            for t in flips if t["flipped"]]},
        "rerun": rerun,
        "estimate": estimate_bootstrap(tasks, n_resamples, seed),
        "suite_extrapolation": extrap,
        "detectable_difference": mdd,
        "statistical_power": power,
        "adjudicability": {"n_unadjudicable": n_unadj, "n_manifests": len(rows),
                           "observations": dict(Counter(r["observations"] for r in rows)),
                           "note": "A verdict with no retained observation and no verifier reason cannot be "
                                   "re-examined by anyone. Such runs count in every rate above; they are "
                                   "excluded from any false-positive / false-negative analysis."},
        "silent_retries": {"total": sum(r["silent_retries"] for r in rows),
                           "by_round": {str(k): sum(r["silent_retries"] for r in rows if r["round"] == k)
                                        for k in sorted({r["round"] for r in rows})}},
        "drift": drift(rows),
    }


def leave_one_out(rows, strata, n_resamples, seed, measured_is_suite) -> dict:
    rounds = sorted({r["round"] for r in rows})
    variants = []
    for rd in rounds:
        kept = [r for r in rows if r["round"] != rd]
        if len({r["round"] for r in kept}) < 2:
            continue
        a = analyse(kept, strata, n_resamples, seed, measured_is_suite)
        e = a.get("suite_extrapolation") or {}
        variants.append({"dropped_round": rd, "n_rounds_left": len({r["round"] for r in kept}),
                         "observed_range_pp": a["per_round_suite_score"]["observed_range_pp"],
                         "mdd95_pp": a["detectable_difference"]["mdd95_pp"],
                         "ci95_width_pp": (e.get("fixed_taskset") or {}).get("ci95_width_pp"),
                         "n_flipped": a["flips"]["n_flipped"]})
    mdds = [v["mdd95_pp"] for v in variants]
    rngs = [v["observed_range_pp"] for v in variants if v["observed_range_pp"] is not None]
    return {"method": "Each round dropped in turn; every figure recomputed on what is left.",
            "variants": variants,
            "mdd95_pp_min": round(min(mdds), 4) if mdds else None,
            "mdd95_pp_max": round(max(mdds), 4) if mdds else None,
            "observed_range_pp_min": round(min(rngs), 4) if rngs else None,
            "observed_range_pp_max": round(max(rngs), 4) if rngs else None}


# ------------------------------------------------------------------- report

def to_markdown(a: dict, settings: dict) -> str:
    prs, mdd, fl = a["per_round_suite_score"], a["detectable_difference"], a["flips"]
    lines = [f"# Noise floor — {settings.get('label') or 'manifests'}", "",
             f"{a['n_manifests']} manifests, {a['n_tasks']} tasks, rounds {a['rounds']}; "
             f"outcomes {a['outcomes']}; verifier versions {list(a['criteria_versions'])}", "",
             "## Per round (the assumption-free measurement)", "",
             "| round | scored | passed | score % |", "|---|---|---|---|"]
    for p in prs["per_round"]:
        flag = "" if p["complete"] else " (partial)"
        lines.append(f"| {p['round']}{flag} | {p['n_tasks_scored']} | {p['n_passed']} | {p['score_pct']} |")
    s = prs["summary"]
    lines += ["", f"Complete rounds: mean {s.get('mean')} %, sd {s.get('sd')} pp, "
                  f"observed range {prs['observed_range_pp']} pp.", "",
              "## Headline", "",
              f"- single-run sd **{mdd['single_run_sd_pp']} pp** (basis: {mdd['basis']})",
              f"- two single runs must differ by **{mdd['mdd95_pp']} pp** before the gap is outside noise; "
              f"{mdd['mdd95_power80_pp']} pp for 80% power",
              f"- {fl['n_flipped']} of {fl['n_tasks_with_2plus_scored']} tasks flipped; mean flip rate "
              f"{fl['mean_flip_rate']} (max possible at n={fl['n_trials_typical']}: {fl['flip_rate_max_typical']})",
              f"- re-run (plugin) sd {a['rerun']['plugin']['sd_pp']} pp, (posterior) {a['rerun']['posterior']['sd_pp']} pp; "
              f"bootstrap precision of this estimate {a['estimate'].get('sd_pp')} pp"]
    if mdd.get("not_reportable"):
        lines.append(f"- **not reportable:** {mdd['not_reportable']}")
    if len(fl.get("by_basis", {})) > 1:
        lines.append("- flips by verdict basis: " + "; ".join(
            f"{b}: {v['n_flipped']}/{v['n_tasks']} flipped, mean flip rate {v['mean_flip_rate']}"
            for b, v in fl["by_basis"].items()))
    loo = a.get("leave_one_out")
    if loo:
        lines.append(f"- leave-one-round-out keeps MDD in {loo['mdd95_pp_min']}–{loo['mdd95_pp_max']} pp")
    adj = a["adjudicability"]
    lines += ["", "## Adjudicability", "",
              f"{adj['n_unadjudicable']} of {adj['n_manifests']} verdicts have neither a retained observation "
              f"nor a verifier reason; observations retained: {adj['observations']}.", "",
              "## Drift screen", "", f"series (median completion tokens per round, {a['drift']['basis']}): "
              f"{a['drift']['series']}"]
    for t in a["drift"]["screen_top"][:1]:
        lines.append(f"strongest single step: after round {t['boundary_after_round']} "
                     f"({t['left_mean']} → {t['right_mean']}, {t['step_pct']}%, variance explained "
                     f"{t['variance_explained']}). A place to look, not evidence of an event.")
    lines += ["", "## Least stable tasks", "", "| task | passes/n | pass rate | Wilson 95% | flip rate |",
              "|---|---|---|---|---|"]
    for t in fl["ranked_by_instability"][:15]:
        lines.append(f"| {t['task_id']} | {t['passes']}/{t['n_scored']} | {t['pass_rate']} | "
                     f"{t['wilson95'][0]}–{t['wilson95'][1]} | {t['flip_rate']} |")
    return "\n".join(lines) + "\n"


def parse_rounds(spec: str | None) -> set[int] | None:
    if not spec:
        return None
    out: set[int] = set()
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            out |= set(range(int(a), int(b) + 1))
        else:
            out.add(int(part))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inputs", nargs="+", help="manifest directories or globs")
    ap.add_argument("--out", default=None, help="write the full analysis JSON here")
    ap.add_argument("--md", default=None, help="write a short markdown report here")
    ap.add_argument("--label", default=None)
    ap.add_argument("--rounds", default=None, help="e.g. 4-10 or 1,2,3")
    ap.add_argument("--exclude-rounds", default=None)
    ap.add_argument("--strata", default=None,
                    help='JSON {"sizes": {stratum: n}, "tasks": {task_id: stratum}} to carry a pilot to a suite')
    ap.add_argument("--measured-is-suite", action="store_true",
                    help="the tasks in the manifests are the whole suite; MDD then uses the plugin re-run sd")
    ap.add_argument("--pass-threshold", type=float, default=0.99)
    ap.add_argument("--min-trials-per-task", type=int, default=None,
                    help="drop tasks with fewer scored trials than this before analysing (uneven repetition designs)")
    ap.add_argument("--resamples", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=20260824)
    ap.add_argument("--no-loo", action="store_true")
    a = ap.parse_args()

    ms = load_manifests(a.inputs)
    rows = [row_of(m, a.pass_threshold) for m in ms]
    missing = [r["path"] for r in rows if not r["task_id"] or r["round"] is None]
    if missing:
        sys.exit(f"{len(missing)} manifest(s) lack task_id or run.repetition_index, e.g. {missing[0]}")
    keep = parse_rounds(a.rounds)
    drop = parse_rounds(a.exclude_rounds) or set()
    rows = [r for r in rows if (keep is None or r["round"] in keep) and r["round"] not in drop]
    if not rows:
        sys.exit("no manifests left after round filters")
    dropped_tasks: list[str] = []
    if a.min_trials_per_task:
        per = Counter(r["task_id"] for r in rows if r["scored"])
        dropped_tasks = sorted(t for t in {r["task_id"] for r in rows} if per.get(t, 0) < a.min_trials_per_task)
        rows = [r for r in rows if r["task_id"] not in dropped_tasks]
        if not rows:
            sys.exit("no manifests left after --min-trials-per-task")
    strata = json.loads(Path(a.strata).read_text()) if a.strata else None

    result = analyse(rows, strata, a.resamples, a.seed, a.measured_is_suite)
    if not a.no_loo:
        result["leave_one_out"] = leave_one_out(rows, strata, a.resamples, a.seed, a.measured_is_suite)
    settings = {"label": a.label, "inputs": a.inputs, "rounds": a.rounds, "exclude_rounds": a.exclude_rounds,
                "strata": a.strata, "measured_is_suite": a.measured_is_suite,
                "min_trials_per_task": a.min_trials_per_task, "tasks_dropped_for_min_trials": dropped_tasks,
                "pass_threshold": a.pass_threshold, "resamples": a.resamples, "seed": a.seed}
    out = {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "generator": "evidence-manifest/reference/analyze.py", "settings": settings, "analysis": result}
    if a.out:
        Path(a.out).write_text(json.dumps(out, indent=1) + "\n")
    md = to_markdown(result, settings)
    if a.md:
        Path(a.md).write_text(md)
    print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
