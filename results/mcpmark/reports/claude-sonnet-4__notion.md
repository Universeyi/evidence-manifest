# Noise floor — MCPMark claude-sonnet-4__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 112}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 28 | 4 | 14.2857 |
| 2 | 28 | 8 | 28.5714 |
| 3 | 28 | 6 | 21.4286 |
| 4 | 28 | 6 | 21.4286 |

Complete rounds: mean 21.4286 %, sd 5.8321 pp, observed range 14.2857 pp.

## Headline

- single-run sd **4.8866 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **13.5447 pp** before the gap is outside noise; 19.3609 pp for 80% power
- 9 of 28 tasks flipped; mean flip rate 0.1786 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.8866 pp, (posterior) 6.9061 pp; bootstrap precision of this estimate 2.4637 pp
- leave-one-round-out keeps MDD in 11.3863–14.0082 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [3985.5, 3923.5, 3904.0, 3842.5]
strongest single step: after round 2 (3954.5 → 3873.25, -2.05%, variance explained 0.6339). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| python_roadmap__expert_level_lessons | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| toronto_guide__change_color | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| toronto_guide__weekend_adventure_planner | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| company_in_a_box__goals_restructure | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| computer_science_student_dashboard__code_snippets_go | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| online_resume__projects_section_update | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| self_assessment__faq_column_layout | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| standard_operating_procedure__deployment_process_sop | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| team_projects__swap_tasks | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
