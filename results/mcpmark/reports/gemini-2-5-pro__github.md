# Noise floor — MCPMark gemini-2-5-pro__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 92}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 23 | 2 | 8.6957 |
| 2 | 23 | 2 | 8.6957 |
| 3 | 23 | 2 | 8.6957 |
| 4 | 23 | 3 | 13.0435 |

Complete rounds: mean 9.7827 %, sd 2.1739 pp, observed range 4.3478 pp.

## Headline

- single-run sd **4.4397 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **12.306 pp** before the gap is outside noise; 17.5903 pp for 80% power
- 5 of 23 tasks flipped; mean flip rate 0.1232 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.4397 pp, (posterior) 7.1976 pp; bootstrap precision of this estimate 2.2379 pp
- leave-one-round-out keeps MDD in 11.2341–12.5153 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [4747.0, 4428.0, 4762.0, 4277.0]
strongest single step: after round 2 (4587.5 → 4519.5, -1.48%, variance explained 0.0267). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| claude-code__critical_issue_hotfix_workflow | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| harmony__issue_pr_commit_workflow | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| easyr1__advanced_branch_strategy | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| missing-semester__find_legacy_name | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| missing-semester__find_salient_file | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
