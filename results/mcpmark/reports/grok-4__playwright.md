# Noise floor — MCPMark grok-4__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 79, 'error': 21}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 19 | 8 | 42.1053 |
| 2 | 20 | 12 | 60.0 |
| 3 | 21 | 7 | 33.3333 |
| 4 | 19 | 8 | 42.1053 |

Complete rounds: mean 44.386 %, sd 11.2006 pp, observed range 26.6667 pp.

## Headline

- single-run sd **5.0294 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **13.9405 pp** before the gap is outside noise; 19.9267 pp for 80% power
- 6 of 21 tasks flipped; mean flip rate 0.1667 (max possible at n=4: 0.6667)
- re-run (plugin) sd 5.0294 pp, (posterior) 7.7923 pp; bootstrap precision of this estimate 2.7592 pp
- **not reportable:** a task has only 1 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 12.0474–14.9705 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [4240.0, 5232.0, 5057.0, 6151.0]
strongest single step: after round 2 (4736.0 → 5604.0, 18.33%, variance explained 0.4086). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| eval_web__cloudflare_turnstile_challenge | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| reddit__ai_data_analyst | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| shopping__printer_keyboard_search | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| shopping__health_routine_optimization | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| shopping_admin__customer_segmentation_setup | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| shopping_admin__search_filtering_operations | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
