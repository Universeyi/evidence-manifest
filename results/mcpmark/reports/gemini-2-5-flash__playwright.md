# Noise floor — MCPMark gemini-2-5-flash__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 93, 'error': 2, 'budget_exhausted': 5}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 23 | 1 | 4.3478 |
| 2 | 25 | 2 | 8.0 |
| 3 | 25 | 1 | 4.0 |
| 4 | 25 | 2 | 8.0 |

Complete rounds: mean 6.0869 %, sd 2.2136 pp, observed range 4.0 pp.

## Headline

- single-run sd **3.4095 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **9.4505 pp** before the gap is outside noise; 13.5086 pp for 80% power
- 3 of 25 tasks flipped; mean flip rate 0.08 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.4095 pp, (posterior) 6.5441 pp; bootstrap precision of this estimate 1.7896 pp
- leave-one-round-out keeps MDD in 7.4412–9.2747 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [3553.0, 4577.0, 6876.0, 1752.0]
strongest single step: after round 2 (4065.0 → 4314.0, 6.13%, variance explained 0.0045). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| reddit__budget_europe_travel | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| reddit__routine_tracker_forum | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| shopping_admin__customer_segmentation_setup | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
