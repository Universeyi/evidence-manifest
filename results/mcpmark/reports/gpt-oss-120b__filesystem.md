# Noise floor — MCPMark gpt-oss-120b__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 117, 'error': 3}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 29 | 3 | 10.3448 |
| 2 | 30 | 0 | 0.0 |
| 3 | 29 | 1 | 3.4483 |
| 4 | 29 | 3 | 10.3448 |

Complete rounds: mean 6.0345 %, sd 5.1724 pp, observed range 10.3448 pp.

## Headline

- single-run sd **3.4667 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **9.609 pp** before the gap is outside noise; 13.7352 pp for 80% power
- 5 of 30 tasks flipped; mean flip rate 0.0944 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.4667 pp, (posterior) 6.241 pp; bootstrap precision of this estimate 1.7384 pp
- leave-one-round-out keeps MDD in 7.4986–9.6897 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [481.0, 252.0, 226.0, 251.5]
strongest single step: after round 2 (366.5 → 238.75, -34.86%, variance explained 0.3807). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| file_context__file_merging | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| threestudio__code_locating | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| file_context__uppercase | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_property__size_classification | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| student_database__duplicate_name | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
