# Noise floor — tau2-bench claude-3-7-sonnet_retail

456 manifests, 114 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 456}; verifier versions ['c30d59aaa71c65f9b9eb6a8f8636b48945028fcf']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 114 | 91 | 79.8246 |
| 2 | 114 | 89 | 78.0702 |
| 3 | 114 | 89 | 78.0702 |
| 4 | 114 | 90 | 78.9474 |

Complete rounds: mean 78.7281 %, sd 0.8399 pp, observed range 1.7544 pp.

## Headline

- single-run sd **2.4951 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.9159 pp** before the gap is outside noise; 9.8857 pp for 80% power
- 38 of 114 tasks flipped; mean flip rate 0.1886 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.4951 pp, (posterior) 3.5117 pp; bootstrap precision of this estimate 1.2492 pp
- leave-one-round-out keeps MDD in 6.2244–6.8461 pp

## Adjudicability

0 of 456 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 456}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 456}): [123.5, 120.91, 120.16, 121.04]
strongest single step: after round 2 (122.204 → 120.603, -1.31%, variance explained 0.4063). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 0 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 10 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 12 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 15 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 19 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 3 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 36 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 37 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 41 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 57 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 59 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 63 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 69 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 72 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 92 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
