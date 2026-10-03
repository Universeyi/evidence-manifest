# Noise floor — MCPMark claude-sonnet-4__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'budget_exhausted': 31, 'completed': 61}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 23 | 5 | 21.7391 |
| 2 | 23 | 3 | 13.0435 |
| 3 | 23 | 5 | 21.7391 |
| 4 | 23 | 2 | 8.6957 |

Complete rounds: mean 16.3043 %, sd 6.5217 pp, observed range 13.0434 pp.

## Headline

- single-run sd **4.1698 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **11.5579 pp** before the gap is outside noise; 16.5209 pp for 80% power
- 5 of 23 tasks flipped; mean flip rate 0.1087 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.1698 pp, (posterior) 7.1336 pp; bootstrap precision of this estimate 2.1106 pp
- leave-one-round-out keeps MDD in 9.6431–12.5128 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [3887.0, 3550.0, 3560.0, 3571.0]
strongest single step: after round 2 (3718.5 → 3565.5, -4.11%, variance explained 0.2917). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| claude-code__critical_issue_hotfix_workflow | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| harmony__issue_pr_commit_workflow | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| harmony__release_management_workflow | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| mcpmark-cicd__linting_ci_workflow | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| missing-semester__find_legacy_name | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
