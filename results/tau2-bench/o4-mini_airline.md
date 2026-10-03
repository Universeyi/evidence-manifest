# Noise floor — tau2-bench o4-mini_airline

200 manifests, 50 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 200}; verifier versions ['c30d59aaa71c65f9b9eb6a8f8636b48945028fcf']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 50 | 28 | 56.0 |
| 2 | 50 | 31 | 62.0 |
| 3 | 50 | 33 | 66.0 |
| 4 | 50 | 26 | 52.0 |

Complete rounds: mean 59.0 %, sd 6.2183 pp, observed range 14.0 pp.

## Headline

- single-run sd **4.0423 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **11.2045 pp** before the gap is outside noise; 16.0158 pp for 80% power
- 19 of 50 tasks flipped; mean flip rate 0.2133 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.0423 pp, (posterior) 5.3698 pp; bootstrap precision of this estimate 2.0032 pp
- leave-one-round-out keeps MDD in 10.1473–10.8757 pp

## Adjudicability

0 of 200 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 200}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 200}): [495.69, 463.0, 458.0, 478.85]
strongest single step: after round 2 (479.347 → 468.425, -2.28%, variance explained 0.1369). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 12 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 18 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 22 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 44 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 48 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 5 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 8 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 1 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 11 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 16 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 17 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 20 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 21 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 29 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 30 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
