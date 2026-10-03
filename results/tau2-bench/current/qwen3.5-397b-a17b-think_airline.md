# Noise floor — tau2-bench leaderboard qwen3.5-397b-a17b-think_airline

200 manifests, 50 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 200}; verifier versions ['unknown']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 50 | 40 | 80.0 |
| 2 | 50 | 42 | 84.0 |
| 3 | 50 | 39 | 78.0 |
| 4 | 50 | 42 | 84.0 |

Complete rounds: mean 81.5 %, sd 3.0 pp, observed range 6.0 pp.

## Headline

- single-run sd **2.9137 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.0762 pp** before the gap is outside noise; 11.5442 pp for 80% power
- 11 of 50 tasks flipped; mean flip rate 0.1167 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.9137 pp, (posterior) 4.8718 pp; bootstrap precision of this estimate 1.491 pp
- leave-one-round-out keeps MDD in 6.9218–8.5945 pp

## Adjudicability

0 of 200 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 200}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 200}): [599.08, 606.83, 530.58, 707.14]
strongest single step: after round 2 (602.954 → 618.86, 2.64%, variance explained 0.0159). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 12 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 9 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 19 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 24 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 31 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 32 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 33 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 35 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 47 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 6 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 8 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
