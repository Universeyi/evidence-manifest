# Noise floor — MCPMark o3__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 112}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 28 | 7 | 25.0 |
| 2 | 28 | 5 | 17.8571 |
| 3 | 28 | 8 | 28.5714 |
| 4 | 28 | 7 | 25.0 |

Complete rounds: mean 24.1071 %, sd 4.494 pp, observed range 10.7143 pp.

## Headline

- single-run sd **5.4209 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **15.0257 pp** before the gap is outside noise; 21.4778 pp for 80% power
- 11 of 28 tasks flipped; mean flip rate 0.2202 (max possible at n=4: 0.6667)
- re-run (plugin) sd 5.4209 pp, (posterior) 7.1406 pp; bootstrap precision of this estimate 2.7114 pp
- leave-one-round-out keeps MDD in 11.4248–15.5235 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [7436.0, 6975.0, 6947.5, 6080.0]
strongest single step: after round 2 (7205.5 → 6513.75, -9.6%, variance explained 0.4979). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| japan_travel_planner__restaurant_expenses_sync | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| online_resume__projects_section_update | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| online_resume__skills_development_tracker | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| python_roadmap__expert_level_lessons | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| company_in_a_box__employee_onboarding | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| company_in_a_box__goals_restructure | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| it_trouble_shooting_hub__asset_retirement_migration | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| japan_travel_planner__remove_osaka_itinerary | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| self_assessment__faq_column_layout | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| team_projects__priority_tasks_table | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| toronto_guide__weekend_adventure_planner | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
