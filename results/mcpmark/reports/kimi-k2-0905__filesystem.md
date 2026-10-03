# Noise floor — MCPMark kimi-k2-0905__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 116, 'budget_exhausted': 3, 'error': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 29 | 5 | 17.2414 |
| 2 | 30 | 4 | 13.3333 |
| 3 | 30 | 4 | 13.3333 |
| 4 | 30 | 4 | 13.3333 |

Complete rounds: mean 14.3103 %, sd 1.954 pp, observed range 3.9081 pp.

## Headline

- single-run sd **3.4084 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **9.4474 pp** before the gap is outside noise; 13.5042 pp for 80% power
- 5 of 30 tasks flipped; mean flip rate 0.0944 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.4084 pp, (posterior) 6.1432 pp; bootstrap precision of this estimate 1.7068 pp
- leave-one-round-out keeps MDD in 7.5302–9.7557 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [2056.5, 2229.0, 2171.0, 1943.5]
strongest single step: after round 2 (2142.75 → 2057.25, -3.99%, variance explained 0.1521). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| desktop__project_management | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| folder_structure__structure_mirror | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| file_property__size_classification | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| papers__organize_legacy_papers | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| votenet__requirements_writing | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
