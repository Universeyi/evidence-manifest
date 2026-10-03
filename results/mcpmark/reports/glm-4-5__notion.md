# Noise floor — MCPMark glm-4-5__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 110, 'budget_exhausted': 2}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 28 | 6 | 21.4286 |
| 2 | 28 | 6 | 21.4286 |
| 3 | 28 | 7 | 25.0 |
| 4 | 28 | 5 | 17.8571 |

Complete rounds: mean 21.4286 %, sd 2.9161 pp, observed range 7.1429 pp.

## Headline

- single-run sd **3.9857 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **11.0476 pp** before the gap is outside noise; 15.7915 pp for 80% power
- 6 of 28 tasks flipped; mean flip rate 0.1191 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.9857 pp, (posterior) 6.4902 pp; bootstrap precision of this estimate 2.0047 pp
- leave-one-round-out keeps MDD in 9.3704–11.4024 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [4024.0, 4678.5, 4641.5, 4183.5]
strongest single step: after round 2 (4351.25 → 4412.5, 1.41%, variance explained 0.0116). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| online_resume__skills_development_tracker | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| self_assessment__faq_column_layout | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| computer_science_student_dashboard__code_snippets_go | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| japan_travel_planner__remove_osaka_itinerary | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| team_projects__swap_tasks | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| toronto_guide__weekend_adventure_planner | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
