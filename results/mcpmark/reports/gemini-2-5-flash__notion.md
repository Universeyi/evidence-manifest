# Noise floor — MCPMark gemini-2-5-flash__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 112}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 28 | 1 | 3.5714 |
| 2 | 28 | 1 | 3.5714 |
| 3 | 28 | 4 | 14.2857 |
| 4 | 28 | 1 | 3.5714 |

Complete rounds: mean 6.25 %, sd 5.3571 pp, observed range 10.7143 pp.

## Headline

- single-run sd **3.861 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **10.7019 pp** before the gap is outside noise; 15.2974 pp for 80% power
- 6 of 28 tasks flipped; mean flip rate 0.1131 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.861 pp, (posterior) 6.4433 pp; bootstrap precision of this estimate 1.9383 pp
- leave-one-round-out keeps MDD in 8.0721–11.3791 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [3884.0, 2580.0, 4093.0, 3100.5]
strongest single step: after round 2 (3232.0 → 3596.75, 11.29%, variance explained 0.0902). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| japan_travel_planner__remove_osaka_itinerary | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| computer_science_student_dashboard__code_snippets_go | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| japan_travel_planner__restaurant_expenses_sync | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| self_assessment__faq_column_layout | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| team_projects__swap_tasks | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| toronto_guide__weekend_adventure_planner | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
