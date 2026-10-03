# Noise floor — MCPMark gpt-5-mini-low__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 90, 'budget_exhausted': 2}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 23 | 2 | 8.6957 |
| 2 | 23 | 3 | 13.0435 |
| 3 | 23 | 2 | 8.6957 |
| 4 | 23 | 1 | 4.3478 |

Complete rounds: mean 8.6957 %, sd 3.55 pp, observed range 8.6957 pp.

## Headline

- single-run sd **3.3884 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **9.392 pp** before the gap is outside noise; 13.425 pp for 80% power
- 3 of 23 tasks flipped; mean flip rate 0.0725 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.3884 pp, (posterior) 6.8171 pp; bootstrap precision of this estimate 1.7139 pp
- leave-one-round-out keeps MDD in 7.9379–9.8078 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [1596.0, 1626.0, 1591.0, 1638.0]
strongest single step: after round 2 (1611.0 → 1614.5, 0.22%, variance explained 0.0078). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| claude-code__automated_changelog_generation | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| easyr1__advanced_branch_strategy | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| easyr1__performance_regression_investigation | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
