# Where the noise floor can be computed from public data

**A note on the thresholds below.** These tables were computed while `reference/analyze.py`
derived the threshold from a 10,000-draw simulated standard deviation. It now uses the exact
Bernoulli value. `python3 results/check_exact.py` recomputes the exact threshold for every
result here that stores per-task counts (40 configurations): the published values differ from
it by at most 0.12 points, median 0.03, which changes no conclusion. Terminal-Bench 2.0, MCPMark
and METR store summaries only and are expected to differ by the same order.

The analysis in `reference/analyze.py` needs one thing the schema cannot
conjure: the same agent configuration run more than once on the same tasks,
with the per-task, per-trial verdict published. Most leaderboards do not have
it. This is the map of who does, as of 2026-09-05, checked source by source
(the full audit with URLs is in [`repeats_survey.md`](repeats_survey.md)).

## Computed here

| benchmark | trials × configurations × tasks | what the record carries | result |
|---|---|---|---|
| MobileWorld (our own audit) | 10 × 1 × 29 | everything the spec asks, by construction | the paper; `examples/mobileworld-audit/` |
| tau2-bench, June 2025 baselines | 4 × 4 × (50, 114) | timestamps, per-message tokens, termination, evaluator commit | [tau2-bench/](tau2-bench/README.md) |
| tau2-bench, leaderboard (current instrument) | 4 × 8 × (50, 114) | as above; two entries lack the commit | [tau2-bench/current-instrument.md](tau2-bench/current-instrument.md) |
| tau-bench v1, historical trajectories | 4–8 × 2 × (50, 115) | verdict and conversation only | [tau-bench-v1/](tau-bench-v1/README.md) |
| Terminal-Bench 2.0, leaderboard scrape | 5 (some 10–12) × 108 × 89 | verdict, run-level tokens, timestamps; digest and commit not kept by the scrape | [terminal-bench-2/](terminal-bench-2/README.md) |
| SWE-bench Verified, KTH randomness artefacts | 10 × 12 × 500 | verdicts per harness results; trajectories with tokens exist, not used | [kth-agentic-evals/](kth-agentic-evals/README.md); reconciles with the paper's Table 1 row for row |
| METR time-horizon runs (reports 1.0 and 1.1) | 4–8 × 53 × (170, 228) | verdict, tokens, timestamps, task version, usage-limit flag; no transcripts | [metr-time-horizon/](metr-time-horizon/README.md) |
| MCPMark v1-0905 logs | 4 × 110 × (21–30 per service) | verdict, timestamps, tokens, turns, errors, model id read back from the response | [mcpmark/](mcpmark/README.md) |

## Public and computable, not yet run

| source | trials × configurations × tasks | notes |
|---|---|---|
| Terminal-Bench 2.0 raw leaderboard (HF `harborframework/…`) | 5 × 76 × 89 | the unscraped originals: ATIF per-step tokens, task git commit and checksum, exception info |
| Terminal-Bench 1.0 run logs | 5 × 22 × 80 | no licence file |
| You.com stochastic-agent-evals | 64 × ~6 × 165 (GAIA) | model + search, not a multi-step scaffold |
| SkillsBench | 3 × ~5 × 60–87 | Apache-2.0 |
| rails/ai-evals | 3 × 18 × 22 | MIT; ATIF |
| Mercor ApexAgents TB2.1 traces | 3 × 4 × 89 | MIT |
| BALROG submissions | 3–10 × 26 × 58 | each repeat is a fresh procedural seed: same task-config, different instance |
| mlfoundations OSWorld trajectories | 3 × 1 × 361 | no licence stated |
| SeerRay AndroidWorld rollouts | 4 × 1 × 116 | an RL checkpoint at temperature 1, not a leaderboard agent |

## Repeats were run, per-run data not published

HAL Reliability Dashboard (K=3–5, 15 agents, GAIA and tau-bench airline;
per-task success fractions only), AgentBench FC (± from four repeats),
Vending-Bench 2 (mean of five), SWE-bench Pro (mean of five claimed; one run
published), MLE-bench (three seeds; grading reports only, seeds unlabelled),
Gaia2/ARE (three runs required; results dataset not listable).

## Single run per configuration by policy or practice

SWE-bench Verified (pass@1 rule, 182 submissions), TheAgentCompany (19
configurations), OSWorld and OSWorld-Verified leaderboards, WebArena and
VisualWebArena, AndroidWorld leaderboard (49 rows, trials = 1), AppWorld (24
configurations, encrypted bundles), GAIA leaderboard, ARC-AGI, AndroidDaily
(no trajectories at all).

## What the map says

Three things, none of them about any one benchmark.

- Where repeats exist, the minimum detectable difference between two single
  runs follows suite size: **11 to 15 points** on MCPMark's 21–30-task
  services, **7 to 13** on suites of 50–115 tasks, **2 to 5** on METR's
  170–228 and **3 to 4** on the 500-task SWE-bench Verified. On every suite
  a tenth to a half of tasks change verdict between identical runs.
- The benchmarks that publish repeats are the ones that can afford to be
  measured; the ones that report a ± from repeats they do not publish cannot
  be checked, and the ones with a pass@1 rule cannot be measured at all
  from the outside.
- Every column of "what the record carries" is a field of the spec, and every
  `unrecorded` in an adapter is a place where a number on a board cannot be
  interpreted after the fact.
