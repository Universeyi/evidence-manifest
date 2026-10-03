# Noise floor — MCPMark o4-mini__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'budget_exhausted': 14, 'completed': 78}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 23 | 1 | 4.3478 |
| 2 | 23 | 4 | 17.3913 |
| 3 | 23 | 3 | 13.0435 |
| 4 | 23 | 5 | 21.7391 |

Complete rounds: mean 14.1304 %, sd 7.4253 pp, observed range 17.3913 pp.

## Headline

- single-run sd **4.4777 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **12.4113 pp** before the gap is outside noise; 17.7408 pp for 80% power
- 5 of 23 tasks flipped; mean flip rate 0.1232 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.4777 pp, (posterior) 7.1861 pp; bootstrap precision of this estimate 2.2298 pp
- leave-one-round-out keeps MDD in 11.2458–12.7936 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [7541.0, 6376.0, 7445.0, 8388.0]
strongest single step: after round 2 (6958.5 → 7916.5, 13.77%, variance explained 0.4497). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| claude-code__automated_changelog_generation | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| easyr1__advanced_branch_strategy | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| build_your_own_x__find_rag_commit | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| harmony__fix_conflict | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| mcpmark-cicd__linting_ci_workflow | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
