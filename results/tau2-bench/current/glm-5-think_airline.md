# Noise floor — tau2-bench leaderboard glm-5-think_airline

200 manifests, 50 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 200}; verifier versions ['unknown']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 50 | 44 | 88.0 |
| 2 | 50 | 43 | 86.0 |
| 3 | 50 | 39 | 78.0 |
| 4 | 50 | 39 | 78.0 |

Complete rounds: mean 82.5 %, sd 5.2599 pp, observed range 10.0 pp.

## Headline

- single-run sd **3.1554 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.7462 pp** before the gap is outside noise; 12.5018 pp for 80% power
- 11 of 50 tasks flipped; mean flip rate 0.13 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.1554 pp, (posterior) 4.8977 pp; bootstrap precision of this estimate 1.5564 pp
- leave-one-round-out keeps MDD in 7.8766–8.7367 pp

## Adjudicability

0 of 200 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 200}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 200}): [436.82, 405.51, 421.84, 403.31]
strongest single step: after round 2 (421.164 → 412.575, -2.04%, variance explained 0.1003). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 14 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 17 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 23 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 31 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 35 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 9 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 11 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 12 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 20 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 29 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 33 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
