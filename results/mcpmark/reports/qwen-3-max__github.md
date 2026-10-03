# Noise floor — MCPMark qwen-3-max__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 84, 'budget_exhausted': 8}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 23 | 2 | 8.6957 |
| 2 | 23 | 3 | 13.0435 |
| 3 | 23 | 4 | 17.3913 |
| 4 | 23 | 4 | 17.3913 |

Complete rounds: mean 14.1304 %, sd 4.1627 pp, observed range 8.6956 pp.

## Headline

- single-run sd **3.2277 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.9466 pp** before the gap is outside noise; 12.7883 pp for 80% power
- 3 of 23 tasks flipped; mean flip rate 0.0652 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.2277 pp, (posterior) 6.7573 pp; bootstrap precision of this estimate 1.623 pp
- leave-one-round-out keeps MDD in 5.644–9.7576 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [1643.0, 1938.0, 2334.0, 1970.0]
strongest single step: after round 2 (1790.5 → 2152.0, 20.19%, variance explained 0.5435). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| claude-code__critical_issue_hotfix_workflow | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| easyr1__advanced_branch_strategy | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| harmony__issue_pr_commit_workflow | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
