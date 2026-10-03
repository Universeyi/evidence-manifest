# Noise floor — MCPMark gpt-4-1-mini__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 92}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 23 | 0 | 0.0 |
| 2 | 23 | 4 | 17.3913 |
| 3 | 23 | 1 | 4.3478 |
| 4 | 23 | 1 | 4.3478 |

Complete rounds: mean 6.5217 %, sd 7.5307 pp, observed range 17.3913 pp.

## Headline

- single-run sd **3.6915 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **10.2321 pp** before the gap is outside noise; 14.6259 pp for 80% power
- 4 of 23 tasks flipped; mean flip rate 0.087 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.6915 pp, (posterior) 6.9603 pp; bootstrap precision of this estimate 1.8805 pp
- leave-one-round-out keeps MDD in 5.6279–11.1416 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [1399.0, 1134.0, 1458.0, 1389.0]
strongest single step: after round 2 (1266.5 → 1423.5, 12.4%, variance explained 0.3967). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build_your_own_x__find_rag_commit | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| claude-code__automated_changelog_generation | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| easyr1__advanced_branch_strategy | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| harmony__issue_pr_commit_workflow | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
