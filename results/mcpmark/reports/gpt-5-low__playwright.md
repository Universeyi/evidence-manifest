# Noise floor — MCPMark gpt-5-low__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 79, 'budget_exhausted': 21}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 25 | 11 | 44.0 |
| 2 | 25 | 11 | 44.0 |
| 3 | 25 | 12 | 48.0 |
| 4 | 25 | 11 | 44.0 |

Complete rounds: mean 45.0 %, sd 2.0 pp, observed range 4.0 pp.

## Headline

- single-run sd **4.3208 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **11.9764 pp** before the gap is outside noise; 17.1192 pp for 80% power
- 6 of 25 tasks flipped; mean flip rate 0.1267 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.3208 pp, (posterior) 7.0503 pp; bootstrap precision of this estimate 2.1871 pp
- leave-one-round-out keeps MDD in 9.0527–12.7733 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [13826.0, 16456.0, 13346.0, 13148.0]
strongest single step: after round 2 (15141.0 → 13247.0, -12.51%, variance explained 0.5077). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| reddit__routine_tracker_forum | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| eval_web__cloudflare_turnstile_challenge | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| reddit__ai_data_analyst | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| shopping__holiday_baking_competition | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| shopping__printer_keyboard_search | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| shopping_admin__search_filtering_operations | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
