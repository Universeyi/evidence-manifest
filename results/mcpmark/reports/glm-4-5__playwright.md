# Noise floor — MCPMark glm-4-5__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 75, 'budget_exhausted': 23, 'error': 2}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 24 | 4 | 16.6667 |
| 2 | 24 | 4 | 16.6667 |
| 3 | 25 | 3 | 12.0 |
| 4 | 25 | 2 | 8.0 |

Complete rounds: mean 13.3333 %, sd 4.1811 pp, observed range 8.6667 pp.

## Headline

- single-run sd **3.6233 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **10.0431 pp** before the gap is outside noise; 14.3557 pp for 80% power
- 4 of 25 tasks flipped; mean flip rate 0.0867 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.6233 pp, (posterior) 6.6643 pp; bootstrap precision of this estimate 1.8069 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 7.363–10.5029 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [2358.0, 2351.0, 2353.0, 2346.0]
strongest single step: after round 2 (2354.5 → 2349.5, -0.21%, variance explained 0.3378). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| shopping_admin__marketing_customer_analysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| eval_web__extraction_table | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| reddit__budget_europe_travel | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| shopping_admin__search_filtering_operations | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
