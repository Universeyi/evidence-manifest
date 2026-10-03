# Noise floor — tau2-bench leaderboard claude-sonnet-4-5_airline

200 manifests, 50 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 200}; verifier versions ['7324fb57cb6819e77937c79964db916f5b068e31']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 50 | 37 | 74.0 |
| 2 | 50 | 36 | 72.0 |
| 3 | 50 | 36 | 72.0 |
| 4 | 50 | 35 | 70.0 |

Complete rounds: mean 72.0 %, sd 1.633 pp, observed range 4.0 pp.

## Headline

- single-run sd **3.8727 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **10.7344 pp** before the gap is outside noise; 15.3438 pp for 80% power
- 19 of 50 tasks flipped; mean flip rate 0.2 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.8727 pp, (posterior) 5.2096 pp; bootstrap precision of this estimate 1.9419 pp
- leave-one-round-out keeps MDD in 9.4369–10.5478 pp

## Adjudicability

0 of 200 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 200}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 200}): [141.6, 143.78, 159.3, 152.75]
strongest single step: after round 2 (142.688 → 156.023, 9.35%, variance explained 0.8817). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 17 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 20 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 43 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 1 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 11 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 15 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 16 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 18 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 22 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 23 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 30 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 33 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 37 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 39 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 41 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
