# Noise floor — MCPMark gpt-oss-120b__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 90, 'error': 9, 'budget_exhausted': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 23 | 1 | 4.3478 |
| 2 | 21 | 1 | 4.7619 |
| 3 | 24 | 1 | 4.1667 |
| 4 | 23 | 0 | 0.0 |

Complete rounds: mean 3.3191 %, sd 2.2267 pp, observed range 4.7619 pp.

## Headline

- single-run sd **1.7406 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **4.8246 pp** before the gap is outside noise; 6.8963 pp for 80% power
- 1 of 24 tasks flipped; mean flip rate 0.0208 (max possible at n=4: 0.6667)
- re-run (plugin) sd 1.7406 pp, (posterior) 6.4847 pp; bootstrap precision of this estimate 0.875 pp
- **not reportable:** a task has only 1 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 0.0–5.4322 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [803.0, 689.0, 987.0, 930.0]
strongest single step: after round 2 (746.0 → 958.5, 28.49%, variance explained 0.8475). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| shopping_admin__customer_segmentation_setup | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
