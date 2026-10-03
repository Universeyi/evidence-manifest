# Noise floor — MCPMark qwen-3-coder-plus__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'error': 19, 'completed': 93}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 3 | 14.2857 |
| 2 | 25 | 6 | 24.0 |
| 3 | 23 | 8 | 34.7826 |
| 4 | 24 | 5 | 20.8333 |

Complete rounds: mean 23.4754 %, sd 8.5549 pp, observed range 20.4969 pp.

## Headline

- single-run sd **5.0411 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **13.973 pp** before the gap is outside noise; 19.973 pp for 80% power
- 8 of 26 tasks flipped; mean flip rate 0.1923 (max possible at n=4: 0.6667)
- re-run (plugin) sd 5.0411 pp, (posterior) 7.3834 pp; bootstrap precision of this estimate 2.6294 pp
- **not reportable:** a task has only 1 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 11.9731–13.8219 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [2268.5, 2099.5, 2546.0, 2191.0]
strongest single step: after round 2 (2184.0 → 2368.5, 8.45%, variance explained 0.3058). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| computer_science_student_dashboard__code_snippets_go | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| it_trouble_shooting_hub__security_audit_ticket | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| online_resume__skills_development_tracker | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| self_assessment__faq_column_layout | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| standard_operating_procedure__deployment_process_sop | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| team_projects__swap_tasks | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| company_in_a_box__goals_restructure | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| japan_travel_planner__restaurant_expenses_sync | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
