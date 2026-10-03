# Noise floor — MCPMark kimi-k2-0711__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 101, 'error': 8, 'budget_exhausted': 3}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 26 | 3 | 11.5385 |
| 2 | 27 | 6 | 22.2222 |
| 3 | 26 | 3 | 11.5385 |
| 4 | 25 | 4 | 16.0 |

Complete rounds: mean 15.3248 %, sd 5.0564 pp, observed range 10.6837 pp.

## Headline

- single-run sd **4.3404 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **12.0308 pp** before the gap is outside noise; 17.1968 pp for 80% power
- 7 of 28 tasks flipped; mean flip rate 0.1548 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.3404 pp, (posterior) 6.7427 pp; bootstrap precision of this estimate 2.3992 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 9.3687–12.5635 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [2284.0, 2037.5, 2431.0, 2110.0]
strongest single step: after round 2 (2160.75 → 2270.5, 5.08%, variance explained 0.1282). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| computer_science_student_dashboard__code_snippets_go | 1/2 | 0.5 | 0.0945–0.9055 | 1.0 |
| company_in_a_box__employee_onboarding | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| it_trouble_shooting_hub__security_audit_ticket | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| company_in_a_box__goals_restructure | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| standard_operating_procedure__deployment_process_sop | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| team_projects__swap_tasks | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| toronto_guide__weekend_adventure_planner | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
