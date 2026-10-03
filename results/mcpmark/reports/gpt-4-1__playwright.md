# Noise floor — MCPMark gpt-4-1__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 100}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 25 | 3 | 12.0 |
| 2 | 25 | 2 | 8.0 |
| 3 | 25 | 2 | 8.0 |
| 4 | 25 | 1 | 4.0 |

Complete rounds: mean 8.0 %, sd 3.266 pp, observed range 8.0 pp.

## Headline

- single-run sd **2.4499 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.7907 pp** before the gap is outside noise; 9.7066 pp for 80% power
- 2 of 25 tasks flipped; mean flip rate 0.04 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.4499 pp, (posterior) 6.3345 pp; bootstrap precision of this estimate 1.2281 pp
- leave-one-round-out keeps MDD in 5.2287–7.3955 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [972.0, 585.0, 857.0, 787.0]
strongest single step: after round 2 (778.5 → 822.0, 5.59%, variance explained 0.0239). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| reddit__budget_europe_travel | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| shopping_admin__customer_segmentation_setup | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
