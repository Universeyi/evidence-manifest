# Noise floor — MCPMark qwen-3-max__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'budget_exhausted': 4, 'completed': 43, 'error': 53}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 12 | 2 | 16.6667 |
| 2 | 10 | 2 | 20.0 |
| 3 | 12 | 2 | 16.6667 |
| 4 | 13 | 2 | 15.3846 |

Complete rounds: mean 17.1795 %, sd 1.9751 pp, observed range 4.6154 pp.

## Headline

- single-run sd **4.7465 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **13.1564 pp** before the gap is outside noise; 18.8058 pp for 80% power
- 2 of 14 tasks flipped; mean flip rate 0.1071 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.7465 pp, (posterior) 9.2987 pp; bootstrap precision of this estimate 2.9655 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 0.0–13.6049 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [940.0, 851.0, 974.0, 930.0]
strongest single step: after round 2 (895.5 → 952.0, 6.31%, variance explained 0.3931). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| shopping_admin__marketing_customer_analysis | 1/2 | 0.5 | 0.0945–0.9055 | 1.0 |
| reddit__budget_europe_travel | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
