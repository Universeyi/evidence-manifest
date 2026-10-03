# Noise floor — MCPMark deepseek-chat__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 107, 'error': 3, 'budget_exhausted': 2}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 27 | 5 | 18.5185 |
| 2 | 27 | 3 | 11.1111 |
| 3 | 27 | 3 | 11.1111 |
| 4 | 28 | 3 | 10.7143 |

Complete rounds: mean 12.8637 %, sd 3.7745 pp, observed range 7.8042 pp.

## Headline

- single-run sd **4.1486 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **11.4991 pp** before the gap is outside noise; 16.4369 pp for 80% power
- 7 of 28 tasks flipped; mean flip rate 0.131 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.1486 pp, (posterior) 6.6072 pp; bootstrap precision of this estimate 2.1241 pp
- leave-one-round-out keeps MDD in 8.0987–12.5327 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [2073.5, 1997.5, 2090.0, 2148.5]
strongest single step: after round 2 (2035.5 → 2119.25, 4.11%, variance explained 0.604). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| toronto_guide__change_color | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| computer_science_student_dashboard__code_snippets_go | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| it_trouble_shooting_hub__security_audit_ticket | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| online_resume__skills_development_tracker | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| self_assessment__faq_column_layout | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| standard_operating_procedure__deployment_process_sop | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| team_projects__swap_tasks | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
