# Noise floor — MCPMark grok-code-fast-1__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 115, 'error': 5}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 28 | 10 | 35.7143 |
| 2 | 29 | 6 | 20.6897 |
| 3 | 29 | 4 | 13.7931 |
| 4 | 29 | 8 | 27.5862 |

Complete rounds: mean 24.4458 %, sd 9.3885 pp, observed range 21.9212 pp.

## Headline

- single-run sd **4.6052 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **12.7647 pp** before the gap is outside noise; 18.246 pp for 80% power
- 9 of 29 tasks flipped; mean flip rate 0.1609 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.6052 pp, (posterior) 6.6953 pp; bootstrap precision of this estimate 2.2855 pp
- leave-one-round-out keeps MDD in 11.1324–12.8252 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [1591.5, 1400.0, 1636.5, 1327.0]
strongest single step: after round 2 (1495.75 → 1481.75, -0.94%, variance explained 0.003). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| file_context__file_merging | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| desktop_template__file_arrangement | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_context__uppercase | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_property__size_classification | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| folder_structure__structure_mirror | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| legal_document__dispute_review | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| student_database__duplicate_name | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| student_database__english_talent | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| threestudio__requirements_completion | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
