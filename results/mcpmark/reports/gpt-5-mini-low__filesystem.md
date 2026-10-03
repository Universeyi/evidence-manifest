# Noise floor — MCPMark gpt-5-mini-low__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 116, 'budget_exhausted': 3, 'error': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 30 | 6 | 20.0 |
| 2 | 30 | 3 | 10.0 |
| 3 | 29 | 2 | 6.8966 |
| 4 | 30 | 4 | 13.3333 |

Complete rounds: mean 12.5575 %, sd 5.6148 pp, observed range 13.1034 pp.

## Headline

- single-run sd **4.4491 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **12.332 pp** before the gap is outside noise; 17.6275 pp for 80% power
- 9 of 30 tasks flipped; mean flip rate 0.1611 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.4491 pp, (posterior) 6.6217 pp; bootstrap precision of this estimate 2.2497 pp
- leave-one-round-out keeps MDD in 9.8–12.9324 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [1576.0, 486.5, 901.0, 1569.0]
strongest single step: after round 2 (1031.25 → 1235.0, 19.76%, variance explained 0.0484). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| student_database__duplicate_name | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| votenet__dataset_comparison | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| desktop__music_report | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| desktop__timeline_extraction | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_context__file_merging | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_context__pattern_matching | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_property__size_classification | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| legal_document__dispute_review | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| legal_document__individual_comments | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
