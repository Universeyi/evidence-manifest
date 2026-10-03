# Noise floor — MCPMark gemini-2-5-pro__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 99, 'error': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 25 | 4 | 16.0 |
| 2 | 24 | 3 | 12.5 |
| 3 | 25 | 4 | 16.0 |
| 4 | 25 | 4 | 16.0 |

Complete rounds: mean 15.125 %, sd 1.75 pp, observed range 3.5 pp.

## Headline

- single-run sd **4.7801 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **13.2495 pp** before the gap is outside noise; 18.9389 pp for 80% power
- 7 of 25 tasks flipped; mean flip rate 0.1533 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.7801 pp, (posterior) 7.128 pp; bootstrap precision of this estimate 2.384 pp
- leave-one-round-out keeps MDD in 10.409–13.9466 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [3652.0, 4496.0, 3413.0, 3217.0]
strongest single step: after round 2 (4074.0 → 3315.0, -18.63%, variance explained 0.6055). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| shopping__advanced_product_analysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| shopping_admin__customer_segmentation_setup | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| reddit__ai_data_analyst | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| reddit__budget_europe_travel | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| shopping__health_routine_optimization | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| shopping__printer_keyboard_search | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| shopping_admin__search_filtering_operations | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
