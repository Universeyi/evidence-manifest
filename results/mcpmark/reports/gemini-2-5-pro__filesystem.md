# Noise floor — MCPMark gemini-2-5-pro__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 119, 'error': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 29 | 7 | 24.1379 |
| 2 | 30 | 7 | 23.3333 |
| 3 | 30 | 9 | 30.0 |
| 4 | 30 | 6 | 20.0 |

Complete rounds: mean 24.3678 %, sd 4.1602 pp, observed range 10.0 pp.

## Headline

- single-run sd **4.6453 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **12.8759 pp** before the gap is outside noise; 18.4049 pp for 80% power
- 10 of 30 tasks flipped; mean flip rate 0.1722 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.6453 pp, (posterior) 6.6256 pp; bootstrap precision of this estimate 2.2888 pp
- leave-one-round-out keeps MDD in 10.5786–13.7296 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [5397.5, 5188.5, 5842.5, 5731.0]
strongest single step: after round 2 (5293.0 → 5786.75, 9.33%, variance explained 0.8968). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| student_database__english_talent | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| desktop__music_report | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| desktop__timeline_extraction | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| desktop_template__contact_information | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_property__time_classification | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| legal_document__dispute_review | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| legal_document__individual_comments | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| papers__organize_legacy_papers | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| student_database__duplicate_name | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| votenet__debugging | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
