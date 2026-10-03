# Noise floor — MCPMark deepseek-chat__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 41, 'budget_exhausted': 58, 'error': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 25 | 3 | 12.0 |
| 2 | 25 | 2 | 8.0 |
| 3 | 25 | 1 | 4.0 |
| 4 | 24 | 1 | 4.1667 |

Complete rounds: mean 7.0417 %, sd 3.7868 pp, observed range 8.0 pp.

## Headline

- single-run sd **3.6447 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **10.1024 pp** before the gap is outside noise; 14.4404 pp for 80% power
- 4 of 25 tasks flipped; mean flip rate 0.0867 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.6447 pp, (posterior) 6.5875 pp; bootstrap precision of this estimate 1.8052 pp
- leave-one-round-out keeps MDD in 9.0475–10.4627 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [1664.0, 1365.0, 1351.0, 1110.0]
strongest single step: after round 2 (1514.5 → 1230.5, -18.75%, variance explained 0.5224). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| shopping_admin__marketing_customer_analysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| reddit__budget_europe_travel | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| shopping_admin__customer_segmentation_setup | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| shopping_admin__search_filtering_operations | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
