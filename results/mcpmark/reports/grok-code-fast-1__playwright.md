# Noise floor — MCPMark grok-code-fast-1__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 84, 'error': 16}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 22 | 7 | 31.8182 |
| 2 | 19 | 6 | 31.5789 |
| 3 | 21 | 6 | 28.5714 |
| 4 | 22 | 6 | 27.2727 |

Complete rounds: mean 29.8103 %, sd 2.246 pp, observed range 4.5455 pp.

## Headline

- single-run sd **5.0648 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **14.0387 pp** before the gap is outside noise; 20.0669 pp for 80% power
- 6 of 22 tasks flipped; mean flip rate 0.1515 (max possible at n=4: 0.6667)
- re-run (plugin) sd 5.0648 pp, (posterior) 7.6295 pp; bootstrap precision of this estimate 2.5479 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 10.2704–14.6163 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [4464.0, 4731.0, 4825.0, 4802.0]
strongest single step: after round 2 (4597.5 → 4813.5, 4.7%, variance explained 0.5651). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| shopping__gaming_accessories_analysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| shopping__health_routine_optimization | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| reddit__ai_data_analyst | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| shopping_admin__customer_segmentation_setup | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| shopping_admin__search_filtering_operations | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| web_search__r1_arxiv | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
