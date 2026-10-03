# Noise floor — MCPMark deepseek-chat__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 112, 'budget_exhausted': 4, 'error': 4}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 29 | 5 | 17.2414 |
| 2 | 29 | 5 | 17.2414 |
| 3 | 29 | 5 | 17.2414 |
| 4 | 29 | 4 | 13.7931 |

Complete rounds: mean 16.3793 %, sd 1.7241 pp, observed range 3.4483 pp.

## Headline

- single-run sd **3.9611 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **10.9794 pp** before the gap is outside noise; 15.694 pp for 80% power
- 6 of 29 tasks flipped; mean flip rate 0.1207 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.9611 pp, (posterior) 6.3741 pp; bootstrap precision of this estimate 1.9683 pp
- leave-one-round-out keeps MDD in 9.9857–11.0124 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [2324.5, 2328.0, 2473.0, 2207.5]
strongest single step: after round 2 (2326.25 → 2340.25, 0.6%, variance explained 0.0055). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| file_property__size_classification | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| papers__find_math_paper | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| votenet__debugging | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| desktop__project_management | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_context__file_merging | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| papers__organize_legacy_papers | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
