# Noise floor — MCPMark claude-sonnet-4__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 112, 'budget_exhausted': 8}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 30 | 7 | 23.3333 |
| 2 | 30 | 9 | 30.0 |
| 3 | 30 | 9 | 30.0 |
| 4 | 30 | 8 | 26.6667 |

Complete rounds: mean 27.5 %, sd 3.1914 pp, observed range 6.6667 pp.

## Headline

- single-run sd **5.4563 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **15.1238 pp** before the gap is outside noise; 21.6181 pp for 80% power
- 13 of 30 tasks flipped; mean flip rate 0.2389 (max possible at n=4: 0.6667)
- re-run (plugin) sd 5.4563 pp, (posterior) 6.9779 pp; bootstrap precision of this estimate 2.7267 pp
- leave-one-round-out keeps MDD in 12.3972–15.7028 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [2879.5, 2646.0, 2620.0, 2931.5]
strongest single step: after round 2 (2762.75 → 2775.75, 0.47%, variance explained 0.0022). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| desktop__project_management | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| file_context__duplicates_searching | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| file_property__time_classification | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| legal_document__dispute_review | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| desktop__music_report | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| desktop_template__contact_information | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| desktop_template__file_arrangement | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_context__file_merging | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| folder_structure__structure_mirror | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| papers__find_math_paper | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| student_database__duplicate_name | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| threestudio__output_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| threestudio__requirements_completion | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
