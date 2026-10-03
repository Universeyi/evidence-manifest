# Noise floor — tau2-bench leaderboard gpt-5-2-none_airline

200 manifests, 50 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 200}; verifier versions ['7324fb57cb6819e77937c79964db916f5b068e31']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 50 | 40 | 80.0 |
| 2 | 50 | 41 | 82.0 |
| 3 | 50 | 42 | 84.0 |
| 4 | 50 | 38 | 76.0 |

Complete rounds: mean 80.5 %, sd 3.4157 pp, observed range 8.0 pp.

## Headline

- single-run sd **3.7477 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **10.3879 pp** before the gap is outside noise; 14.8485 pp for 80% power
- 17 of 50 tasks flipped; mean flip rate 0.19 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.7477 pp, (posterior) 5.2494 pp; bootstrap precision of this estimate 1.9134 pp
- leave-one-round-out keeps MDD in 9.4322–10.4505 pp

## Adjudicability

0 of 200 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 200}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 200}): [270.58, 299.69, 310.11, 338.5]
strongest single step: after round 2 (285.137 → 324.305, 13.74%, variance explained 0.6498). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 14 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 17 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 18 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 23 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 33 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 35 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 21 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 24 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 28 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 29 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 3 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 31 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 37 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 39 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 45 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
