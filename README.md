# evidence-manifest

A small structured record of **what produced a benchmark number**: the eleven
fields whose absence made a published agent-benchmark score impossible to
interpret. A JSON Schema, two checkers, and a reference analyser that turns a
directory of these records into a noise floor.

## What two single runs have to differ by

The analyser, run on the repeated runs that benchmarks publish themselves. The
number is the gap two single runs of the same configuration must exceed before
it is outside what repetition alone produces (95%).

| Benchmark | Source of the repeated runs | Tasks | Gap |
|---|---|---|---|
| MobileWorld, GUI-only | [our audit](https://github.com/Universeyi/instrument-moves), 10 rounds | 117 (reweighted from 29) | 8.1 (8.6 with the round that had an outage) |
| τ²-bench, airline | Sierra's June 2025 baselines, 4 models × 4 trials | 50 | 10–11 |
| τ²-bench, retail | same | 114 | 7–8 |
| τ-bench v1 | Sierra's historical trajectories, 2 models | 50 / 115 | 13 / 8 |
| Terminal-Bench 2.0 | leaderboard, 95 configurations × 5 trials | 89 | median 7.6 (3.8–9.1) |
| MCPMark v1 | published logs, 67 configurations × 4 trials | 21–30 per service | median 11.5 |
| METR time horizon 1.1 | published runs, 20 agents | 228 | median 3.2 (2.3–4.5) |
| SWE-bench Verified | ASSERT-KTH randomness artefacts, 12 configurations × 10 runs | 500 | 2.7–4.1 |

On suites of 50 to 115 tasks, a single-run gap under about 7 to 13 points is
inside noise; on suites of 230 to 500 tasks, under about 2 to 4.5. Most leaderboards
report single runs. Each row links to its table, caveats and source in
[`results/`](results/README.md), which also maps which benchmarks publish
repeated runs at all.

## Five minutes

Python 3.10 or later. Everything runs on the standard library except `validate.py`, which needs `pip install jsonschema`.

```bash
git clone https://github.com/Universeyi/evidence-manifest && cd evidence-manifest
python3 reference/validate.py examples/*.json                 # schema
python3 reference/check_spec_compliance.py examples/*.json    # rules the schema cannot express
python3 reference/analyze.py examples/mobileworld-audit --rounds 4-10 \
    --strata tests/mobileworld-audit.strata.json --md audit.md
python3 tests/test_regression.py                              # 16/16 paper figures reproduce
```

To get a noise floor for your own runs, write one manifest per run (task,
trial, verdict, configuration; `SPEC.md` lists the fields) or adapt an existing
log with one of the adapters, then point `reference/analyze.py` at the
directory.

```
SPEC.md                      the fields, each with the gap it closes
schema/manifest.schema.json  JSON Schema, draft 2020-12
reference/validate.py        schema check
reference/check_spec_compliance.py
                             semantic rules the schema cannot express
reference/analyze.py         the consumer: noise floor, threshold, flips, leave-one-out,
                             adjudicability, drift screen, from a directory of manifests
reference/detect_drift.py    screen a per-round series for a step change
adapters/                    MobileWorld, tau2-bench, tau-bench v1, Terminal-Bench 2.0,
                             MCPMark, METR time horizon, ASSERT-KTH agentic evals
examples/mobileworld-audit/  the 314 manifests of the MobileWorld stability audit
examples/*.json              five of them, chosen to show each field doing work
results/                     the noise floors above, with tables and caveats
tests/test_regression.py     analyze.py must reproduce the audit paper's figures
```

## Why these fields

Every required field points at a specific case where a score could not be
read: an endpoint that changed under a pinned run and left no trace; a `:latest`
tag that was the oldest build; verifier fixes that landed after leaderboard
entries; 37 of 40 entries with no repetition count; one run in five stopped by
a budget and recorded as a wrong answer; a verdict nobody can re-examine
because the screenshots were discarded and the verifier gave no reason.
`SPEC.md` has the table.

The field the spec most wants is completion tokens **per step**: it is the
cheap signal that exposed a mid-run endpoint change in the audit. The flagship
benchmark cannot emit it, because its harness records one usage total per run.
The adapter says so in the manifest rather than inventing per-step numbers,
and the schema allows a run-level fallback with a stated reason.

## Two checkers, and why

We wrote the spec, then wrote the first adapter for it, and the adapter
violated the spec: it filled `observed_provider` from the declared provider.
The schema check passed. That is why there is a second checker, and why the
spec has a provenance field the first draft lacked.

## Adjudicability

The last required field, `artefacts.observations`, came from the audit's own
aftermath: after submission, 13,350 screenshots were deleted as not needed for
any claim, and the runs behind them stopped being something a person could
open. A verdict with no retained observation and no verifier reason is not
wrong; it cannot be examined. The checker flags it, and a checker analysis
leaves such runs out of its denominator.

## Drift screen

`reference/detect_drift.py` reports where a single-step change would explain
the most variance in a per-round series. On the audit's series it points at
the round boundary where the endpoint's behaviour changed (95% of variance
explained) and at nothing on a flat series. It tells you where to look; it is
not evidence of an event.

## Status

v0.1.0. Spec, schema, both checkers, the reference analyser and seven adapters
exist and agree with each other. The threshold uses the exact Bernoulli
standard deviation since 2026-10-03; `results/README.md` says how much that
moves the published tables (at most 0.12 points). The most useful feedback is
which required fields do not earn their place, and which harness you would want
an adapter for.

Background: [The Instrument Moves: Unrecorded Serving Changes in Agent
Benchmarks](https://jingyuanyi.com/papers/instrument-moves/), poster at the
NeurIPS 2026 workshop *Who Verifies the Agents?*.

## Licence

Code (`reference/`, `adapters/`, `tests/`, `results/check_exact.py`): MIT, see
[`LICENSE`](LICENSE). Spec, schema, examples and results: CC BY 4.0. Results are
statistics computed from third-party public data; see [`NOTICE`](NOTICE) for
each source and its licence.
