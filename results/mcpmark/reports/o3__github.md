# Noise floor — MCPMark o3__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 88, 'error': 3, 'budget_exhausted': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 23 | 2 | 8.6957 |
| 2 | 23 | 4 | 17.3913 |
| 3 | 20 | 4 | 20.0 |
| 4 | 23 | 3 | 13.0435 |

Complete rounds: mean 14.7826 %, sd 4.97 pp, observed range 11.3043 pp.

## Headline

- single-run sd **3.9547 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **10.9617 pp** before the gap is outside noise; 15.6687 pp for 80% power
- 4 of 23 tasks flipped; mean flip rate 0.0942 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.9547 pp, (posterior) 7.0632 pp; bootstrap precision of this estimate 1.962 pp
- leave-one-round-out keeps MDD in 5.6279–11.3614 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [2618.0, 3098.0, 3004.0, 2710.0]
strongest single step: after round 2 (2858.0 → 2857.0, -0.03%, variance explained 0.0). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| easyr1__advanced_branch_strategy | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| claude-code__automated_changelog_generation | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| easyr1__performance_regression_investigation | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| harmony__issue_pr_commit_workflow | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
