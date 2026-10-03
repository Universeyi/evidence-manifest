# Noise floor — MCPMark gpt-4-1__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 119, 'budget_exhausted': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 30 | 4 | 13.3333 |
| 2 | 30 | 3 | 10.0 |
| 3 | 30 | 4 | 13.3333 |
| 4 | 30 | 4 | 13.3333 |

Complete rounds: mean 12.5 %, sd 1.6666 pp, observed range 3.3333 pp.

## Headline

- single-run sd **3.2205 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.9266 pp** before the gap is outside noise; 12.7597 pp for 80% power
- 5 of 30 tasks flipped; mean flip rate 0.0833 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.2205 pp, (posterior) 6.0394 pp; bootstrap precision of this estimate 1.6152 pp
- leave-one-round-out keeps MDD in 7.5202–9.7629 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [1433.0, 1400.0, 1684.5, 1730.5]
strongest single step: after round 2 (1416.5 → 1707.5, 20.54%, variance explained 0.9814). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| file_context__duplicates_searching | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| file_context__file_merging | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| file_property__size_classification | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| legal_document__dispute_review | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| papers__organize_legacy_papers | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
