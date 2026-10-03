# tau2-bench leaderboard submissions: the noise floor under the current instrument

The June 2025 baseline files (../README.md) were scored by an evaluator that predates NL assertions.
The leaderboard's own submissions are the current instrument: tau2-bench 1.0.x, user simulator gpt-5.2,
four trials per configuration, trajectories on the public bucket `sierra-tau-bench-public`. Eight text
submissions publish airline and retail; converted with the same adapter and analysed with the same
command. Zero compute.

| domain | submission | tasks | per-round score % | range pp | single-run sd pp | MDD95 pp | tasks flipped | mean flip rate | leave-one-out MDD | evaluator commit |
|---|---|---|---|---|---|---|---|---|---|---|
| airline | claude-opus-4-5 | 50 | [80.0, 86.0, 88.0, 82.0] | 8.0 | 3.11 | **8.6** | 12/50 | 0.127 | 7.8-8.2 | `7324fb57` |
| airline | claude-sonnet-4-5 | 50 | [74.0, 72.0, 72.0, 70.0] | 4.0 | 3.87 | **10.7** | 19/50 | 0.200 | 9.4-10.5 | `7324fb57` |
| airline | gemini-3-flash | 50 | [68.0, 66.0, 68.0, 66.0] | 2.0 | 2.00 | **5.5** | 5/50 | 0.053 | 4.6-5.8 | `5a629d14` |
| airline | gemini-3-pro | 50 | [80.9, 82.0, 84.0, 80.0] | 4.0 | 2.71 | **7.5** | 9/50 | 0.097 | 6.4-7.9 | `ef9454a8` |
| airline | glm-5-think | 50 | [88.0, 86.0, 78.0, 78.0] | 10.0 | 3.16 | **8.7** | 11/50 | 0.130 | 7.9-8.7 | `not recorded` |
| airline | gpt-5-2 | 50 | [82.0, 84.0, 80.0, 86.0] | 6.0 | 2.62 | **7.3** | 9/50 | 0.093 | 6.4-7.3 | `7324fb57` |
| airline | gpt-5-2-none | 50 | [80.0, 82.0, 84.0, 76.0] | 8.0 | 3.75 | **10.4** | 17/50 | 0.190 | 9.4-10.5 | `7324fb57` |
| airline | qwen3.5-397b-a17b-think | 50 | [80.0, 84.0, 78.0, 84.0] | 6.0 | 2.91 | **8.1** | 11/50 | 0.117 | 6.9-8.6 | `not recorded` |
| retail | claude-opus-4-5 | 114 | [80.7, 78.9, 82.5, 76.3] | 6.1 | 2.84 | **7.9** | 52/114 | 0.244 | 7.2-8.0 | `7324fb57` |
| retail | claude-sonnet-4-5 | 114 | [76.3, 77.2, 71.9, 64.0] | 13.2 | 3.14 | **8.7** | 63/114 | 0.298 | 7.8-8.6 | `7324fb57` |
| retail | gemini-3-flash | 114 | [76.3, 75.4, 78.1, 77.2] | 2.6 | 2.67 | **7.4** | 45/114 | 0.216 | 6.7-7.2 | `ef9454a8` |
| retail | gemini-3-pro | 114 | [84.2, 73.3, 76.7, 82.5] | 10.9 | 2.54 | **7.0** | 41/114 | 0.202 | 6.0-7.4 | `ef9454a8` |
| retail | glm-5-think | 114 | [73.9, 77.0, 73.7, 72.8] | 4.2 | 2.93 | **8.1** | 54/114 | 0.257 | 7.5-7.8 | `not recorded` |
| retail | gpt-5-2 | 114 | [86.8, 80.7, 85.1, 73.7] | 13.2 | 2.79 | **7.7** | 51/114 | 0.240 | 6.7-7.9 | `7324fb57` |
| retail | gpt-5-2-none | 114 | [74.6, 74.6, 78.4, 77.3] | 3.8 | 2.81 | **7.8** | 48/114 | 0.254 | 7.0-7.5 | `7324fb57` |
| retail | qwen3.5-397b-a17b-think | 114 | [84.2, 85.1, 84.2, 84.2] | 0.9 | 2.57 | **7.1** | 43/114 | 0.200 | 6.4-7.1 | `not recorded` |

## Does the kind of verifier show up in the instability?

Retail tasks come in three kinds under the current evaluator: 2 scored on the database state alone, 72 declared
`DB+NL_ASSERTION` where no assertion was evaluated in these runs, and 40 where an LLM-judged natural-language
assertion was actually evaluated (`:nl`). Mean flip rate by kind, per submission:

| submission | DB+NL_ASSERTION, no assertion evaluated (72 tasks) | LLM assertion evaluated (40 tasks) |
|---|---|---|
| claude-opus-4-5 | 31/72 flipped, 0.2292 | 19/40 flipped, 0.2583 |
| claude-sonnet-4-5 | 43/72 flipped, 0.3218 | 20/40 flipped, 0.2708 |
| gemini-3-flash | 26/72 flipped, 0.2037 | 18/40 flipped, 0.2375 |
| gemini-3-pro | 28/72 flipped, 0.2153 | 13/40 flipped, 0.1875 |
| glm-5-think | 34/72 flipped, 0.2616 | 18/40 flipped, 0.2375 |
| gpt-5-2 | 29/72 flipped, 0.2153 | 20/40 flipped, 0.2708 |
| gpt-5-2-none | 28/72 flipped, 0.2407 | 18/40 flipped, 0.2667 |
| qwen3.5-397b-a17b-think | 30/72 flipped, 0.2222 | 12/40 flipped, 0.1583 |
| **mean over 8** | **0.239** | **0.236** |

On this data the tasks whose verdict passed through an LLM judge are not visibly less stable than the rest;
if anything the opposite, and the difference is within what eight configurations of 40 and 72 tasks can
resolve. A null, reported as one. It says nothing about the judge's *accuracy*, which four repetitions
cannot see; it says the judge did not add run-to-run noise on top of what the conversation already carries.

## Notes

- **This is an indication of scale, not a re-scoring.** Four trials per configuration; gaps below the MDD
  warrant a second run before citation, not a claim that two systems are equal.
- **The leaderboard already reports pass^1 to pass^4**, which is a consistency measure. What it does not
  report is an interval on pass^1, which is what the gap between two entries needs.
- **Two submissions carry no evaluator commit** in their result files (`git_commit: unknown`), so the
  manifest's `criteria_version` is `unknown` for them; the others record it, and three different commits
  appear across the eight, so the board mixes evaluator versions. That is exactly the field the spec exists for.
- **The NL-assertion judge's model id is not in the result files.** The submission metadata names the user
  simulator (gpt-5.2); nothing names the model that evaluated the assertions. A verdict that passed through
  an LLM should say which one.
- **The noise includes the user simulator** (gpt-5.2, reasoning effort low), as before.
- Telecom and banking_knowledge are also published for these submissions (larger files) and were not run here.
