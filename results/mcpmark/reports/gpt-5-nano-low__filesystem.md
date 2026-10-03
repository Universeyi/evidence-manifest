# Noise floor — MCPMark gpt-5-nano-low__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 112, 'budget_exhausted': 8}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 30 | 4 | 13.3333 |
| 2 | 30 | 4 | 13.3333 |
| 3 | 30 | 2 | 6.6667 |
| 4 | 30 | 5 | 16.6667 |

Complete rounds: mean 12.5 %, sd 4.1943 pp, observed range 10.0 pp.

## Headline

- single-run sd **4.1427 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **11.4828 pp** before the gap is outside noise; 16.4135 pp for 80% power
- 8 of 30 tasks flipped; mean flip rate 0.1389 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.1427 pp, (posterior) 6.4863 pp; bootstrap precision of this estimate 2.0691 pp
- leave-one-round-out keeps MDD in 9.7063–11.4711 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [12188.5, 13578.0, 15901.5, 15979.5]
strongest single step: after round 2 (12883.25 → 15940.5, 23.73%, variance explained 0.9061). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| papers__find_math_paper | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| desktop__music_report | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| file_context__duplicates_searching | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_context__file_merging | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_context__pattern_matching | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_context__uppercase | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_property__size_classification | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| votenet__debugging | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
