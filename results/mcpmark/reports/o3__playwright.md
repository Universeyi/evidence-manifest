# Noise floor — MCPMark o3__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 90, 'budget_exhausted': 9, 'error': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 25 | 5 | 20.0 |
| 2 | 24 | 3 | 12.5 |
| 3 | 25 | 5 | 20.0 |
| 4 | 25 | 2 | 8.0 |

Complete rounds: mean 15.125 %, sd 5.9214 pp, observed range 12.0 pp.

## Headline

- single-run sd **4.3361 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **12.0188 pp** before the gap is outside noise; 17.1798 pp for 80% power
- 6 of 25 tasks flipped; mean flip rate 0.1267 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.3361 pp, (posterior) 6.9557 pp; bootstrap precision of this estimate 2.1495 pp
- leave-one-round-out keeps MDD in 10.3652–12.8044 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [2677.0, 2591.0, 2841.0, 2614.0]
strongest single step: after round 2 (2634.0 → 2727.5, 3.55%, variance explained 0.2288). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| shopping__advanced_product_analysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| eval_web__cloudflare_turnstile_challenge | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| eval_web__extraction_table | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| reddit__routine_tracker_forum | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| shopping_admin__search_filtering_operations | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| web_search__birth_of_arvinxu | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
