# Noise floor — tau2-bench leaderboard claude-opus-4-5_airline

200 manifests, 50 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 200}; verifier versions ['7324fb57cb6819e77937c79964db916f5b068e31']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 50 | 40 | 80.0 |
| 2 | 50 | 43 | 86.0 |
| 3 | 50 | 44 | 88.0 |
| 4 | 50 | 41 | 82.0 |

Complete rounds: mean 84.0 %, sd 3.6515 pp, observed range 8.0 pp.

## Headline

- single-run sd **3.1075 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.6134 pp** before the gap is outside noise; 12.312 pp for 80% power
- 12 of 50 tasks flipped; mean flip rate 0.1267 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.1075 pp, (posterior) 4.9522 pp; bootstrap precision of this estimate 1.548 pp
- leave-one-round-out keeps MDD in 7.7918–8.2057 pp

## Adjudicability

0 of 200 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 200}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 200}): [341.1, 370.1, 359.25, 353.85]
strongest single step: after round 2 (355.599 → 356.55, 0.27%, variance explained 0.0021). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 31 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 35 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 14 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 15 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 18 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 21 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 29 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 32 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 33 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 6 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 7 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 8 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
