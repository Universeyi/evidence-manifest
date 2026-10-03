# Noise floor — MCPMark gpt-5-low__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 112}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 28 | 9 | 32.1429 |
| 2 | 28 | 14 | 50.0 |
| 3 | 28 | 9 | 32.1429 |
| 4 | 28 | 9 | 32.1429 |

Complete rounds: mean 36.6072 %, sd 8.9286 pp, observed range 17.8571 pp.

## Headline

- single-run sd **5.5233 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **15.3095 pp** before the gap is outside noise; 21.8835 pp for 80% power
- 11 of 28 tasks flipped; mean flip rate 0.2202 (max possible at n=4: 0.6667)
- re-run (plugin) sd 5.5233 pp, (posterior) 7.1874 pp; bootstrap precision of this estimate 2.7242 pp
- leave-one-round-out keeps MDD in 13.3099–14.9273 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [24764.5, 23851.5, 23432.0, 24518.0]
strongest single step: after round 2 (24308.0 → 23975.0, -1.37%, variance explained 0.0992). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| japan_travel_planner__packing_progress_summary | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| self_assessment__faq_column_layout | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| standard_operating_procedure__deployment_process_sop | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| toronto_guide__change_color | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| it_trouble_shooting_hub__asset_retirement_migration | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| japan_travel_planner__daily_itinerary_overview | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| japan_travel_planner__restaurant_expenses_sync | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| online_resume__projects_section_update | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| online_resume__skills_development_tracker | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| self_assessment__numbered_list_emojis | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| toronto_guide__weekend_adventure_planner | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
