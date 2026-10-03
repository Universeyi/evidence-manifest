# Noise floor — MCPMark gpt-5-low__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'budget_exhausted': 16, 'completed': 76}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 23 | 6 | 26.087 |
| 2 | 23 | 6 | 26.087 |
| 3 | 23 | 7 | 30.4348 |
| 4 | 23 | 6 | 26.087 |

Complete rounds: mean 27.1739 %, sd 2.1739 pp, observed range 4.3478 pp.

## Headline

- single-run sd **4.4637 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **12.3725 pp** before the gap is outside noise; 17.6854 pp for 80% power
- 5 of 23 tasks flipped; mean flip rate 0.1232 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.4637 pp, (posterior) 7.1512 pp; bootstrap precision of this estimate 2.2503 pp
- leave-one-round-out keeps MDD in 9.8474–12.6938 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [9027.0, 9797.0, 7839.0, 7571.0]
strongest single step: after round 2 (9412.0 → 7705.0, -18.14%, variance explained 0.8976). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build_your_own_x__find_rag_commit | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| missing-semester__find_legacy_name | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| easyr1__config_parameter_audit | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| harmony__fix_conflict | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| harmony__issue_pr_commit_workflow | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
