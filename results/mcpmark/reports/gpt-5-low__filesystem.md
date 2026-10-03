# Noise floor — MCPMark gpt-5-low__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 116, 'budget_exhausted': 4}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 30 | 13 | 43.3333 |
| 2 | 30 | 18 | 60.0 |
| 3 | 30 | 18 | 60.0 |
| 4 | 30 | 16 | 53.3333 |

Complete rounds: mean 54.1667 %, sd 7.8764 pp, observed range 16.6667 pp.

## Headline

- single-run sd **5.428 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **15.0454 pp** before the gap is outside noise; 21.506 pp for 80% power
- 12 of 30 tasks flipped; mean flip rate 0.2278 (max possible at n=4: 0.6667)
- re-run (plugin) sd 5.428 pp, (posterior) 6.905 pp; bootstrap precision of this estimate 2.6594 pp
- leave-one-round-out keeps MDD in 13.0702–15.286 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [10210.5, 9719.5, 8488.0, 8922.5]
strongest single step: after round 2 (9965.0 → 8705.25, -12.64%, variance explained 0.8807). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| desktop__project_management | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| desktop_template__contact_information | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| student_database__gradebased_score | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| votenet__dataset_comparison | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| votenet__debugging | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| file_context__file_splitting | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| file_context__pattern_matching | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| file_context__uppercase | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| papers__organize_legacy_papers | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| student_database__duplicate_name | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| threestudio__output_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| threestudio__requirements_completion | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
