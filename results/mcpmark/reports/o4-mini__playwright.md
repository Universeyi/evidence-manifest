# Noise floor — MCPMark o4-mini__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 77, 'budget_exhausted': 18, 'error': 5}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 25 | 3 | 12.0 |
| 2 | 25 | 3 | 12.0 |
| 3 | 25 | 2 | 8.0 |
| 4 | 20 | 4 | 20.0 |

Complete rounds: mean 13.0 %, sd 5.0332 pp, observed range 12.0 pp.

## Headline

- single-run sd **4.9484 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **13.716 pp** before the gap is outside noise; 19.6058 pp for 80% power
- 7 of 25 tasks flipped; mean flip rate 0.1667 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.9484 pp, (posterior) 7.2398 pp; bootstrap precision of this estimate 2.5229 pp
- leave-one-round-out keeps MDD in 11.8805–14.0583 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [13233.0, 12534.0, 17968.0, 18553.0]
strongest single step: after round 2 (12883.5 → 18260.5, 41.74%, variance explained 0.9858). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| reddit__budget_europe_travel | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| reddit__routine_tracker_forum | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| shopping__gaming_accessories_analysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| shopping_admin__search_filtering_operations | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| shopping__running_shoes_purchase | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| shopping_admin__customer_segmentation_setup | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| shopping_admin__marketing_customer_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
