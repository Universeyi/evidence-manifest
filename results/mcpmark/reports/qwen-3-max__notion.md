# Noise floor — MCPMark qwen-3-max__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 105, 'budget_exhausted': 7}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 28 | 3 | 10.7143 |
| 2 | 28 | 6 | 21.4286 |
| 3 | 28 | 4 | 14.2857 |
| 4 | 28 | 6 | 21.4286 |

Complete rounds: mean 16.9643 %, sd 5.3572 pp, observed range 10.7143 pp.

## Headline

- single-run sd **3.8775 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **10.7477 pp** before the gap is outside noise; 15.3628 pp for 80% power
- 6 of 28 tasks flipped; mean flip rate 0.1131 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.8775 pp, (posterior) 6.5258 pp; bootstrap precision of this estimate 1.9406 pp
- leave-one-round-out keeps MDD in 9.3363–11.5717 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [1881.5, 2157.0, 2030.0, 2055.0]
strongest single step: after round 2 (2019.25 → 2042.5, 1.15%, variance explained 0.0139). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| it_trouble_shooting_hub__asset_retirement_migration | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| computer_science_student_dashboard__code_snippets_go | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| it_trouble_shooting_hub__security_audit_ticket | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| japan_travel_planner__remove_osaka_itinerary | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| japan_travel_planner__restaurant_expenses_sync | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| standard_operating_procedure__deployment_process_sop | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
