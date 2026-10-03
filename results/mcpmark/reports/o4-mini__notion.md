# Noise floor — MCPMark o4-mini__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 112}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 28 | 7 | 25.0 |
| 2 | 28 | 6 | 21.4286 |
| 3 | 28 | 3 | 10.7143 |
| 4 | 28 | 7 | 25.0 |

Complete rounds: mean 20.5357 %, sd 6.7606 pp, observed range 14.2857 pp.

## Headline

- single-run sd **5.0075 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **13.8798 pp** before the gap is outside noise; 19.8399 pp for 80% power
- 10 of 28 tasks flipped; mean flip rate 0.1845 (max possible at n=4: 0.6667)
- re-run (plugin) sd 5.0075 pp, (posterior) 6.8953 pp; bootstrap precision of this estimate 2.4353 pp
- leave-one-round-out keeps MDD in 10.4159–14.2573 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [18327.0, 20014.5, 15756.0, 18756.5]
strongest single step: after round 2 (19170.75 → 17256.25, -9.99%, variance explained 0.3822). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| computer_science_student_dashboard__code_snippets_go | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| company_in_a_box__employee_onboarding | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| it_trouble_shooting_hub__asset_retirement_migration | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| japan_travel_planner__remove_osaka_itinerary | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| japan_travel_planner__restaurant_expenses_sync | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| python_roadmap__expert_level_lessons | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| self_assessment__faq_column_layout | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| standard_operating_procedure__deployment_process_sop | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| team_projects__priority_tasks_table | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| toronto_guide__weekend_adventure_planner | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
