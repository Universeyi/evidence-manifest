# METR time-horizon runs: the noise floor of the raw success rate

METR publishes the per-run records behind its time-horizon reports (`METR/eval-analysis-public`,
`reports/time-horizon-1-x/data/raw/runs.jsonl`): one row per agent, task and run on HCAST, RE-Bench and
SWAA, with a binarized score, tokens, timestamps, the task version and whether the run hit a usage limit.
Report 1.1 has 20 agents on 228 tasks, report 1.0 has 33 on 170; most cells hold 4 to 8 runs. Converted
by `adapters/metr_time_horizon.py`, analysed per agent with `--measured-is-suite --min-trials-per-task 4`
(tasks with fewer than four scored runs are left out of that agent's suite). Zero compute.

> **Scope.** The suite score here is the unweighted per-task success rate over the tasks the agent ran.
> METR's headline number is the 50% time horizon, which weights tasks by family and by human time; this
> is a noise floor for the raw rate, not for the horizon. The SWAA tasks (seconds-long) are a third of
> the rows and pull the rate up and the floor down.

## Report 1.1 (2026): 20 of 20 agents with at least three complete rounds

| | min | median | max |
|---|---|---|---|
| MDD95, points between two single runs (228 tasks) | 2.3 | **3.2** | 4.5 |
| share of tasks that flipped | 0.08 | 0.14 | 0.33 |
| observed range across complete rounds, pp | | 3.1 | 6.2 |

| agent | tasks | rounds | per-round score % | range | sd | MDD95 | flipped | budget-limited runs | leave-one-out MDD |
|---|---|---|---|---|---|---|---|---|---|
| Claude Opus 4.6 (Inspect) | 228 | 5 | [83.8, 84.6, 84.6, 85.1, 82.0] | 3.1 | 0.97 | 2.7 | 29/228 | 18 | 2.593-2.7363 |
| GPT-5.2 | 228 | 4 | [83.8, 82.0, 82.0, 82.9] | 1.8 | 0.85 | 2.4 | 20/228 | 97 | 1.9386-2.3746 |
| GPT-5.3-Codex | 228 | 6 | [82.9, 82.0, 82.0, 81.1, 81.1, 79.4] | 3.5 | 1.04 | 2.9 | 31/228 | 105 | 2.7984-2.9182 |
| Claude Opus 4.5 (Inspect) | 228 | 4 | [78.9, 80.3, 81.1, 80.7] | 2.2 | 0.84 | 2.3 | 19/228 | 11 | 1.9769-2.3386 |
| GPT-5.1-Codex-Max (Inspect) | 228 | 6 | [79.8, 79.4, 80.7, 79.4, 78.1, 77.6] | 3.1 | 1.08 | 3.0 | 32/228 | 125 | 2.8996-3.0199 |
| Gemini 3 Pro | 228 | 4 | [79.8, 78.9, 76.8, 78.9] | 3.1 | 1.02 | 2.8 | 25/228 | 12 | 2.4902-2.8891 |
| GPT-5 (Inspect) | 228 | 4 | [78.5, 77.6, 76.3, 77.6] | 2.2 | 1.04 | 2.9 | 28/228 | 51 | 2.5523-2.9037 |
| o3 (Inspect) | 226 | 4 | [76.5, 74.3, 73.5, 72.6] | 4.0 | 1.07 | 3.0 | 29/226 | 109 | 2.6959-2.9631 |
| Claude 4.1 Opus (Inspect) | 227 | 4 | [70.0, 70.9, 72.2, 71.8] | 2.2 | 1.07 | 3.0 | 27/227 | 0 | 2.7552-2.9536 |
| Claude 4 Opus (Inspect) | 228 | 4 | [71.9, 70.6, 70.2, 70.6] | 1.8 | 1.28 | 3.5 | 44/228 | 0 | 3.3675-3.5681 |
| Claude 3.7 Sonnet (Inspect) | 223 | 4 | [67.7, 65.5, 66.8, 67.7] | 2.2 | 1.09 | 3.0 | 29/223 | 0 | 2.5833-3.1898 |
| o1 (Inspect) | 228 | 4 | [63.6, 64.0, 65.4, 61.8] | 3.5 | 1.31 | 3.6 | 45/228 | 10 | 3.3023-3.6535 |
| o1-preview | 210 | 6 | [60.0, 58.6, 58.1, 58.1, 64.3, 58.1] | 6.2 | 1.61 | 4.5 | 69/210 | 60 | 4.2927-4.4984 |
| Claude 3.5 Sonnet  New  (Inspect) | 211 | 4 | [58.3, 58.3, 58.8, 58.3] | 0.5 | 1.38 | 3.8 | 40/211 | 3 | 3.5424-3.839 |
| Claude 3.5 Sonnet  Old  (Inspect) | 210 | 4 | [54.3, 50.5, 56.2, 54.8] | 5.7 | 1.37 | 3.8 | 43/210 | 0 | 3.4781-3.7891 |
| GPT-4o (Inspect) | 228 | 4 | [47.8, 46.1, 44.3, 45.6] | 3.5 | 1.39 | 3.8 | 50/228 | 1 | 3.5022-3.8442 |
| Claude 3 Opus (Inspect) | 211 | 4 | [48.3, 46.0, 45.5, 43.6] | 4.7 | 1.40 | 3.9 | 43/211 | 4 | 3.4614-3.8678 |
| GPT-4 1106 (Inspect) | 217 | 4 | [45.2, 41.9, 43.8, 44.2] | 3.2 | 1.25 | 3.5 | 37/217 | 17 | 3.0786-3.4797 |
| GPT-4 0314 | 213 | 5 | [44.6, 43.2, 43.7, 43.2, 42.7] | 1.9 | 1.34 | 3.7 | 43/213 | 364 | 3.4717-3.7461 |
| GPT-4 Turbo (Inspect) | 216 | 4 | [41.7, 43.5, 41.2, 41.7] | 2.3 | 1.14 | 3.2 | 30/216 | 7 | 2.8455-3.2876 |

## Report 1.0 (2025): 33 of 33 agents with at least three complete rounds

| | min | median | max |
|---|---|---|---|
| MDD95, points between two single runs (168 tasks) | 2.5 | **4.0** | 7.7 |
| share of tasks that flipped | 0.06 | 0.19 | 0.33 |
| observed range across complete rounds, pp | | 3.6 | 9.1 |

| agent | tasks | rounds | per-round score % | range | sd | MDD95 | flipped | budget-limited runs | leave-one-out MDD |
|---|---|---|---|---|---|---|---|---|---|
| Claude Opus 4.5 | 163 | 4 | [84.7, 85.3, 85.9, 82.2] | 3.7 | 1.17 | 3.2 | 16/163 | 20 | 2.901-3.2505 |
| GPT-5.1-Codex-Max | 158 | 4 | [85.4, 84.2, 84.8, 82.3] | 3.2 | 0.90 | 2.5 | 10/158 | 28 | 2.0353-2.6238 |
| o3 | 164 | 4 | [78.0, 80.5, 79.3, 77.4] | 3.0 | 1.21 | 3.3 | 22/164 | 93 | 3.263-3.3528 |
| GPT-5 | 168 | 4 | [76.8, 79.2, 78.6, 80.4] | 3.6 | 1.16 | 3.2 | 21/168 | 88 | 2.9705-3.2899 |
| Claude Sonnet 4.5 | 170 | 4 | [77.6, 77.1, 78.2, 77.6] | 1.2 | 1.11 | 3.1 | 20/170 | 45 | 2.9755-3.1072 |
| Claude 4.1 Opus | 169 | 5 | [78.7, 77.5, 77.5, 76.9, 76.2] | 2.5 | 1.30 | 3.6 | 25/169 | 40 | 3.4168-3.6297 |
| o4-mini | 166 | 5 | [76.5, 74.7, 76.5, 75.9, 74.1] | 2.4 | 1.14 | 3.2 | 22/166 | 138 | 3.0473-3.2699 |
| Claude 4 Opus | 169 | 4 | [75.7, 74.6, 74.4, 76.2] | 1.8 | 1.19 | 3.3 | 20/169 | 48 | 3.1022-3.3539 |
| Claude 4 Sonnet | 168 | 5 | [74.4, 75.6, 75.6, 74.4, 73.8] | 1.8 | 1.08 | 3.0 | 21/168 | 47 | 2.7652-3.1917 |
| Grok 4 | 168 | 4 | [73.8, 72.6, 75.6, 75.6] | 3.0 | 1.39 | 3.9 | 31/168 | 194 | 3.758-3.8767 |
| Claude 3.7 Sonnet | 168 | 6 | [73.2, 72.6, 72.0, 72.6, 73.8, 75.6] | 3.6 | 1.16 | 3.2 | 21/168 | 88 | 3.1371-3.2948 |
| Kimi K2 Thinking | 168 | 4 | [72.0, 71.4, 72.0, 72.6] | 1.2 | 1.23 | 3.4 | 24/168 | 70 | 3.1928-3.5099 |
| o1 | 166 | 6 | [69.9, 73.3, 72.3, 70.5, 69.7, 72.3] | 3.6 | 1.45 | 4.0 | 36/166 | 30 | 3.9188-4.0626 |
| gpt-oss-120b | 168 | 5 | [69.0, 67.9, 72.6, 69.5, 70.8] | 4.8 | 1.61 | 4.5 | 42/168 | 121 | 4.1915-4.5122 |
| Gemini 2.5 Pro Preview | 169 | 7 | [67.5, 69.8, 68.0, 69.2, 66.3, 70.4, 68.6] | 4.1 | 1.26 | 3.5 | 27/169 | 299 | 3.3356-3.508 |
| DeepSeek-R1-0528 | 169 | 6 | [66.3, 64.5, 67.5, 66.9, 68.0, 69.2] | 4.7 | 1.74 | 4.8 | 53/169 | 110 | 4.6356-4.8496 |
| DeepSeek-R1 | 168 | 5 | [67.3, 66.7, 64.9, 61.3, 66.7] | 6.0 | 1.64 | 4.5 | 47/168 | 180 | 4.2403-4.5591 |
| Claude 3.5 Sonnet  New | 170 | 8 | [64.7, 65.3, 64.7, 64.7, 66.5, 64.7, 64.7, 67.1] | 2.4 | 1.52 | 4.2 | 37/170 | 74 | 4.0965-4.2398 |
| DeepSeek-V3-0324 | 167 | 7 | [65.9, 66.5, 64.1, 67.1, 63.5, 65.3, 63.5] | 3.6 | 1.43 | 4.0 | 34/167 | 51 | 3.7819-4.0022 |
| o1-preview | 168 | 5 | [66.1, 63.1, 63.7, 65.5, 64.3] | 3.0 | 1.57 | 4.4 | 42/168 | 54 | 4.2137-4.3778 |
| DeepSeek-V3 | 168 | 5 | [62.5, 61.9, 61.9, 63.1, 63.1] | 1.2 | 1.46 | 4.0 | 38/168 | 116 | 3.8755-4.1466 |
| Claude 3.5 Sonnet  Old | 170 | 7 | [60.6, 60.6, 58.2, 62.1, 60.6, 63.3, 62.9] | 5.1 | 1.63 | 4.5 | 41/170 | 74 | 4.4424-4.5363 |
| GPT-4o | 169 | 4 | [56.2, 56.8, 53.3, 55.0] | 3.6 | 1.48 | 4.1 | 34/169 | 63 | 3.9623-4.1358 |
| Qwen2-72B | 140 | 4 | [57.1, 54.3, 54.3, 53.6] | 3.6 | 1.56 | 4.3 | 27/140 | 137 | 4.1547-4.3842 |
| GPT-4 1106 | 170 | 7 | [54.1, 53.8, 54.1, 57.1, 55.6, 52.4, 54.7] | 4.7 | 1.69 | 4.7 | 44/170 | 129 | 4.4033-4.7337 |
| Claude 3 Opus | 169 | 7 | [52.1, 51.2, 52.7, 52.4, 56.0, 55.0, 50.9] | 5.1 | 1.54 | 4.3 | 37/169 | 62 | 4.0615-4.3459 |
| GPT-4 Turbo | 170 | 6 | [53.5, 51.2, 50.9, 53.8, 48.8, 54.4] | 5.6 | 1.38 | 3.8 | 29/170 | 64 | 3.7062-3.8997 |
| GPT-4 0314 | 170 | 5 | [50.0, 53.3, 51.8, 54.2, 49.7] | 4.5 | 1.59 | 4.4 | 39/170 | 253 | 4.2034-4.4257 |
| Qwen2.5-72B | 168 | 4 | [50.9, 50.9, 50.6, 53.3] | 2.7 | 1.58 | 4.4 | 40/168 | 382 | 4.1937-4.4219 |
| GPT-4 0125 | 170 | 7 | [50.0, 50.9, 50.6, 50.9, 50.9, 48.2, 50.0] | 2.7 | 1.41 | 3.9 | 32/170 | 76 | 3.7866-3.9551 |
| gpt-3.5-turbo-instruct | 141 | 4 | [44.7, 44.0, 44.7, 43.3] | 1.4 | 1.05 | 2.9 | 15/141 | 12 | 2.6559-3.0454 |
| GPT-2 | 66 | 10 | [40.9, 43.9, 37.9, 37.9, 42.4, 34.8, 40.9, 40.9, 39.4, 39.4] | 9.1 | 2.76 | 7.7 | 21/66 | 0 | 7.3844-7.8401 |
| davinci-002  GPT-3 | 150 | 4 | [27.3, 26.0, 28.7, 31.5] | 5.5 | 2.01 | 5.6 | 50/150 | 557 | 5.4596-5.5686 |

† fewer than three complete rounds after the per-task filter; report in `reports/`, not in the summary.

## How to read it

- **Two to five points on 170-228 tasks.** In line with the 1/sqrt(n) reading of the other suites: the floor
  here sits between SWE-bench Verified's 3-4 (500 tasks) and Terminal-Bench's 7-9 (89 tasks).
- **A tenth to a third of tasks flip**, lower than on the conversational and terminal suites; the SWAA
  tasks are near-deterministic for capable models and dilute the share.
- **This is an indication of scale, not a re-scoring.** Repetitions per task are uneven (4, 6 or 8); the
  per-round series uses only rounds attempted for every task, and the drift screen only tasks present in
  every listed round -- a design point forced by this dataset, since a round that holds only the tasks
  repeated more often is a different suite.
- **Usage limits did visible work**: 994 of 23014 runs in report 1.1 and 3743 of 40415 in report 1.0 ended
  at a usage limit (`fatal_error_from: usageLimits`), recorded here as `budget_exhausted` with score 0, which
  is how METR scores them too. The record says so; most benchmarks' records do not.
- **The record is the best in this collection for the drift screen**: every run has tokens and timestamps.
  The screen over per-round median tokens on the common task set found no step explaining 80% or more of
  the variance with a shift of 15% or more in either report.

## The record

- Present: task version per run (`criteria_version`), start and end timestamps, tokens per run, the
  usage-limit flag. Absent: transcripts (`artefacts.observations: none`, so no verdict is adjudicable
  from the release), image digests, the harness commit, and any served-provider read-back.
