# Noise floor — MCPMark claude-sonnet-4__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 68, 'budget_exhausted': 32}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 25 | 7 | 28.0 |
| 2 | 25 | 4 | 16.0 |
| 3 | 25 | 8 | 32.0 |
| 4 | 25 | 7 | 28.0 |

Complete rounds: mean 26.0 %, sd 6.9282 pp, observed range 16.0 pp.

## Headline

- single-run sd **4.9172 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **13.6295 pp** before the gap is outside noise; 19.4821 pp for 80% power
- 7 of 25 tasks flipped; mean flip rate 0.16 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.9172 pp, (posterior) 7.1014 pp; bootstrap precision of this estimate 2.4818 pp
- leave-one-round-out keeps MDD in 11.781–13.9281 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [3700.0, 3576.0, 2925.0, 3373.0]
strongest single step: after round 2 (3638.0 → 3149.0, -13.44%, variance explained 0.6888). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| reddit__llm_research_summary | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| shopping__gaming_accessories_analysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| shopping__health_routine_optimization | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| reddit__budget_europe_travel | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| shopping_admin__customer_segmentation_setup | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| shopping_admin__marketing_customer_analysis | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| shopping_admin__search_filtering_operations | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
