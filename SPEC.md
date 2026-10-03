# evidence-manifest

A small, structured record of *what produced a benchmark number*.

Every required field below corresponds to a specific gap: a case where a
published agent-benchmark score could not be interpreted because the field
was absent. The spec is the structured form of those gaps and nothing more.
A field that cannot point at a concrete gap does not get to be required.

## Required fields (11)

| field | type | the gap it closes |
|---|---|---|
| `task_id` | string | The task this run attempted, as the benchmark names it. Every figure the consumer produces is per task before it is per suite; a run that cannot be joined to its repetitions cannot enter any of them. |
| `serving.provider` | string | The serving endpoint behind a model id is not pinnable through any API flag and is not recorded anywhere. Two entries with the same model id can be different weights on different hardware. |
| `serving.observed_provider` | string | Declared and served can differ — routing layers silently reroute, and merge-vs-assign bugs drop the caller's pin. Read back off the response or a call-time log, never copied from the request; `"unrecorded"` when not read back. |
| `serving.observed_provider_source` | enum | `response` / `log` / `unrecorded`. Without this, a correct pin and a copied value look identical — both make observed equal declared. Added after the first adapter for this spec did exactly that. |
| `env.image_digest` | string (sha256) | Tags move. `:latest` was the oldest build in one case. Only a digest identifies an environment. A benchmark whose environment is not an image writes the literal `not_containerized`; a released record that simply lacks the digest writes `unrecorded`; what it must not write is a tag. |
| `env.taskset_commit` | string | Verifier fixes land after leaderboard entries are made. Entries from different dates were scored by different verifiers and nothing recorded which. `unrecorded` when the released record lacks it; the literal is the finding. |
| `run.repetition_index` / `run.total_repetitions` | int / int | 37 of 40 leaderboard entries were single runs with no interval. A number with no repetition count cannot be given one later. |
| `step[].completion_tokens` | int | The only cheap signal that exposed a mid-run serving change: reasoning volume per action stepped down 20% while aggregate token counts moved 8%. One integer per request. |
| `verdict.criteria_version` | string | Which verifier scored this. Distinct from `taskset_commit` when verifiers are versioned separately. |
| `outcome.reason` | enum | `completed` / `budget_exhausted` / `error` / `unknown`. One in five published runs ended at a round cap and was recorded indistinguishably from getting the task wrong. |
| `artefacts.observations` | enum | `per_step` / `final_only` / `none` — what a person can still look at. A disputed verdict can be re-adjudicated only if the observation the agent acted on was kept next to the actions. In the audit the runs that needed adjudication were the minority-outcome ones; screenshots for 40 candidate runs were kept and 13,350 others were discarded as not needed for any claim, after which those runs could not be adjudicated by anyone. Published bundles carry actions and a verdict; one pass in three carries no verifier reason. |

`outcome.reason = unknown` is permitted and **is excluded from the denominator**
by any conforming consumer. A run that could not be judged is not a failure.

## Optional fields

`run.started_at`, `run.ended_at` (ISO 8601, UTC) — lets a consumer locate a
shift in wall-clock time. `serving.quantization`. `sampling.temperature`,
`sampling.seed` — recorded, not trusted: `temperature=0` with a seed was
measured not to produce determinism on two endpoints that advertised seed
support. `step[].latency_ms`. `harness.silent_retries` — count of internal
restarts absorbed before a verdict. `artefacts.location` — where the retained
observations are (a path or URL); a claim of `per_step` with nowhere to look is
just a claim.

## Semantic rules — what the schema cannot say

A schema checks that fields exist with the right types. It cannot check that
`observed_provider` was actually observed. The first adapter written for this
spec produced schema-valid manifests whose `observed_provider` had been filled
from the declared provider — a claim formatted as an observation — and
`validate.py` passed every one of them. So there is a second checker.

`reference/check_spec_compliance.py` enforces rules a schema cannot express.
Each rule is written against a named failure; a rule that cannot name one is
not added:

| rule | catches |
|---|---|
| observed provider must carry read-back provenance | the adapter above |
| `budget_exhausted` cannot coexist with a pass; `completed` cannot lack a score | one in five published runs ended at a budget and was recorded as a wrong answer |
| `repetition_index ≤ total_repetitions` | a record that makes an interval impossible |
| `ended_at ≥ started_at` | a verdict that predates its run |
| token usage recorded once, per-step *or* run-level with a stated reason | double counting through the fallback |
| a verdict with `observations: none` and no verifier reason is unadjudicable | 384 of 1,144 published passes carry no reason, and the screenshots behind most of the audit's own runs no longer exist: for such a run a person has nothing to look at and nothing explained, so it can be neither confirmed nor refuted |

One rule belongs to consumers rather than manifests and is stated here as a
contract: **`outcome.reason = unknown` is excluded from every denominator.**
The reference analyser will carry a test for it.

A second consumer contract: **a checker analysis — hunting false positives and false
negatives by opening runs — excludes unadjudicable runs from its denominator.**
They are not wrong; they are unexaminable, and a rate computed over them would
be a rate over runs nobody could open.

A spec that can only be followed on trust is not a spec. Both checkers run on
the examples in this repository, and the examples were regenerated after the
adapter was fixed.

## Consumers

The reference implementation under `reference/` consumes this format directly:

- `validate.py` — schema check
- `analyze.py` — per-task pass rates with Wilson intervals, flip rate,
  per-round suite scores, re-run distribution, minimum detectable difference,
  leave-one-round-out, adjudicability, and the drift screen, from a directory
  of manifests. On the audit's own 314 manifests it reproduces the paper's
  figures to the last decimal (`tests/test_regression.py`).
- `detect_drift.py` — screens a `completion_tokens` series for a step change

A benchmark that emits this format gets that analysis for free. That is the
point: the spec exists to be consumed, and the consumer exists.
