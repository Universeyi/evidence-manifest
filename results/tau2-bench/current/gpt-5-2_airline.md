# Noise floor — tau2-bench leaderboard gpt-5-2_airline

200 manifests, 50 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 200}; verifier versions ['7324fb57cb6819e77937c79964db916f5b068e31']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 50 | 41 | 82.0 |
| 2 | 50 | 42 | 84.0 |
| 3 | 50 | 40 | 80.0 |
| 4 | 50 | 43 | 86.0 |

Complete rounds: mean 83.0 %, sd 2.582 pp, observed range 6.0 pp.

## Headline

- single-run sd **2.617 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.2538 pp** before the gap is outside noise; 10.3687 pp for 80% power
- 9 of 50 tasks flipped; mean flip rate 0.0933 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.617 pp, (posterior) 4.7249 pp; bootstrap precision of this estimate 1.3167 pp
- leave-one-round-out keeps MDD in 6.3757–7.3167 pp

## Adjudicability

0 of 200 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 200}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 200}): [534.16, 557.11, 553.14, 501.92]
strongest single step: after round 2 (545.638 → 527.531, -3.32%, variance explained 0.1723). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 45 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 18 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 19 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 24 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 31 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 32 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 37 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 42 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 6 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
