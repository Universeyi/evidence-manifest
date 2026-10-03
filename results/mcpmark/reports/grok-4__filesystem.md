# Noise floor — MCPMark grok-4__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 116, 'error': 3, 'budget_exhausted': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 29 | 13 | 44.8276 |
| 2 | 30 | 16 | 53.3333 |
| 3 | 29 | 14 | 48.2759 |
| 4 | 29 | 18 | 62.069 |

Complete rounds: mean 52.1264 %, sd 7.4925 pp, observed range 17.2414 pp.

## Headline

- single-run sd **5.4233 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **15.0323 pp** before the gap is outside noise; 21.4873 pp for 80% power
- 14 of 30 tasks flipped; mean flip rate 0.2389 (max possible at n=4: 0.6667)
- re-run (plugin) sd 5.4233 pp, (posterior) 7.0742 pp; bootstrap precision of this estimate 2.7318 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 13.713–15.059 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [8114.0, 7397.0, 8117.0, 9667.5]
strongest single step: after round 2 (7755.5 → 8892.25, 14.66%, variance explained 0.4697). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| desktop__music_report | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| desktop__timeline_extraction | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| desktop_template__budget_computation | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| desktop_template__file_arrangement | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_context__duplicates_searching | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| file_context__pattern_matching | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_property__time_classification | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| folder_structure__structure_mirror | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| legal_document__individual_comments | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| legal_document__solution_tracing | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| student_database__english_talent | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| threestudio__code_locating | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| threestudio__requirements_completion | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| votenet__debugging | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
