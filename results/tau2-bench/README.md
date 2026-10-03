# tau2-bench: the noise floor of its own baseline runs

Any benchmark that puts a language model in the evaluation loop, as tau2 does
with an LLM playing the user, will vary between runs. That is the cost of
evaluating interactive agents rather than static outputs, and it is a cost worth
paying. What has been missing is a number for it.

This analysis exists only because Sierra publishes complete per-run baseline
files. Very few benchmarks do. Nothing here required re-running anything.

> **Scope.** These are the June 2025 baseline files (evaluator commit
> `c30d59aa`, 2025-06-05). The retail suite on `main` today attaches NL
> assertions to 112 of 114 tasks; these runs predate that and were scored on
> DB + COMMUNICATE only. A run under the current verifier is a different
> instrument. The manifests record which one scored each run.

**Update 2026-09-05.** The leaderboard's own submissions are the current instrument, and eight of them
publish four-trial airline and retail trajectories on the public bucket. The same adapter and command
run on those: [current-instrument.md](current-instrument.md). The June table below is kept as the
first pass.

Computed by `reference/analyze.py` from the eight baseline result files Sierra publishes in
`data/tau2/results/final` (4 agent models x retail and airline x 4 trials each), converted by
`adapters/tau2bench.py`. Zero compute: nothing was re-run. The analysis JSON and a short report per
configuration are in this directory.

```bash
F=gpt-4.1-2025-04-14_retail_default_gpt-4.1-2025-04-14_4trials.json
curl -sSLO https://raw.githubusercontent.com/sierra-research/tau2-bench/main/data/tau2/results/final/$F
python3 adapters/tau2bench.py $F --out manifests/gpt-4.1_retail/ \
    --source-url https://github.com/sierra-research/tau2-bench/blob/main/data/tau2/results/final/$F
python3 reference/analyze.py manifests/gpt-4.1_retail/ --measured-is-suite \
    --out results/tau2-bench/gpt-4.1_retail.json --md results/tau2-bench/gpt-4.1_retail.md
```

| domain | agent | tasks | per-round score % | range pp | single-run sd pp | MDD95 pp | tasks flipped | mean flip rate | leave-one-out MDD |
|---|---|---|---|---|---|---|---|---|---|
| airline | claude-3-7-sonnet | 50 | [54.0, 50.0, 50.0, 46.0] | 8.0 | 3.67 | **10.2** | 16/50 | 0.180 | 9.1-10.2 |
| airline | gpt-4.1 | 50 | [58.0, 54.0, 60.0, 52.0] | 8.0 | 3.94 | **10.9** | 19/50 | 0.207 | 9.7-10.8 |
| airline | gpt-4.1-mini | 50 | [50.0, 52.0, 50.0, 50.0] | 2.0 | 4.13 | **11.4** | 21/50 | 0.223 | 9.8-11.4 |
| airline | o4-mini | 50 | [56.0, 62.0, 66.0, 52.0] | 14.0 | 4.04 | **11.2** | 19/50 | 0.213 | 10.1-10.9 |
| retail | claude-3-7-sonnet | 114 | [79.8, 78.1, 78.1, 78.9] | 1.8 | 2.50 | **6.9** | 38/114 | 0.189 | 6.2-6.8 |
| retail | gpt-4.1 | 114 | [73.7, 71.1, 75.4, 76.3] | 5.3 | 2.58 | **7.2** | 43/114 | 0.199 | 6.6-6.9 |
| retail | gpt-4.1-mini | 114 | [68.4, 67.5, 60.5, 67.5] | 7.9 | 2.95 | **8.2** | 53/114 | 0.262 | 7.5-7.9 |
| retail | o4-mini | 114 | [69.3, 72.8, 73.7, 70.2] | 4.4 | 2.85 | **7.9** | 52/114 | 0.243 | 7.2-7.8 |

MDD95 is the gap two single runs must show before it is outside what noise alone produces 95% of
the time; the basis is the Bernoulli re-run distribution over the measured suite (`--measured-is-suite`:
every task of the domain was run). Flip rate = discordant trial pairs / all pairs; at n=4 its maximum is 0.667.

## How to read it

- **Airline (50 tasks): two single runs must differ by 10-11 points.** Retail (114 tasks): 7-8 points.
  The published leaderboard reports one number per model with no interval; adjacent entries a few
  points apart are inside this.
- **This is an indication of scale, not a re-scoring.** Four trials per configuration puts a wide
  interval on each per-task rate, and the numbers are computed for these four agents on these files.
  The appropriate reading of a gap below the MDD is that it warrants a second run before citation,
  not that two systems are equal.
- **One task in three to one in two flips** between identical runs at temperature 0 (agent and
  simulated user both at 0.0). The widest single-configuration range in the table is 14 points across
  four rounds of the same 50 tasks.
- **The noise includes the user simulator.** tau2's user is an LLM (gpt-4.1 at temperature 0) whose
  sampling is part of every run; the manifest records sampling for the agent only. This is a floor for
  the benchmark as published, not for the agent alone.
- **Every run completed** (`termination_reason: user_stop` for all 3,080). No round budget truncated
  a run, so none of the zeros here are a run being stopped rather than failing.
- **Every verdict is adjudicable**: the conversation is the observation and each verdict carries a
  reason string assembled from the checks.

## What the manifests could not carry

- `serving.observed_provider` is `unrecorded`: the agent called the vendor API directly and nothing
  in the results reads a served-by value back. For a first-party API the field is still honest.
- `env.image_digest` is `not_containerized`: a tool-calling text environment. The literal was added
  to the schema for this adapter.
- Per-step tokens exist (one per assistant message that carries usage), so the drift screen runs on a
  real per-step series here, the first adapter for which that is true.

## Who is best placed to do this

The data needed for this was already public; the only thing added was a format
and a script. If a benchmark publishes per-run trajectories, anyone can compute
this, including the maintainers, who are better placed to do it than an outsider
is. The adapter is about 120 lines. We would rather see this reported alongside
the scores than computed after the fact by someone else.
