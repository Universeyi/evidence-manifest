# Noise floor — MCPMark gpt-oss-120b__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 103, 'error': 9}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 26 | 1 | 3.8462 |
| 2 | 26 | 0 | 0.0 |
| 3 | 25 | 1 | 4.0 |
| 4 | 26 | 2 | 7.6923 |

Complete rounds: mean 3.8846 %, sd 3.1413 pp, observed range 7.6923 pp.

## Headline

- single-run sd **3.1246 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.6608 pp** before the gap is outside noise; 12.3798 pp for 80% power
- 4 of 28 tasks flipped; mean flip rate 0.0714 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.1246 pp, (posterior) 6.4503 pp; bootstrap precision of this estimate 1.5241 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 6.6327–9.4197 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [720.5, 953.0, 998.5, 1392.5]
strongest single step: after round 2 (836.75 → 1195.5, 42.87%, variance explained 0.5515). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| company_in_a_box__employee_onboarding | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| computer_science_student_dashboard__code_snippets_go | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| japan_travel_planner__remove_osaka_itinerary | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| toronto_guide__weekend_adventure_planner | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
