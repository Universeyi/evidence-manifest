# Noise floor — MCPMark kimi-k2-0711__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 55, 'error': 45}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 12 | 3 | 25.0 |
| 2 | 13 | 2 | 15.3846 |
| 3 | 15 | 4 | 26.6667 |
| 4 | 15 | 4 | 26.6667 |

Complete rounds: mean 23.4295 %, sd 5.4205 pp, observed range 11.2821 pp.

## Headline

- single-run sd **2.8873 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.003 pp** before the gap is outside noise; 11.4396 pp for 80% power
- 1 of 15 tasks flipped; mean flip rate 0.0333 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.8873 pp, (posterior) 8.3585 pp; bootstrap precision of this estimate 1.4322 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 0.0–8.6965 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [1346.0, 1484.0, 1484.0, 1442.0]
strongest single step: after round 2 (1415.0 → 1463.0, 3.39%, variance explained 0.1813). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| shopping_admin__marketing_customer_analysis | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
