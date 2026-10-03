# Noise floor — tau2-bench claude-3-7-sonnet_airline

200 manifests, 50 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 200}; verifier versions ['c30d59aaa71c65f9b9eb6a8f8636b48945028fcf']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 50 | 27 | 54.0 |
| 2 | 50 | 25 | 50.0 |
| 3 | 50 | 25 | 50.0 |
| 4 | 50 | 23 | 46.0 |

Complete rounds: mean 50.0 %, sd 3.266 pp, observed range 8.0 pp.

## Headline

- single-run sd **3.6693 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **10.1706 pp** before the gap is outside noise; 14.5379 pp for 80% power
- 16 of 50 tasks flipped; mean flip rate 0.18 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.6693 pp, (posterior) 5.1401 pp; bootstrap precision of this estimate 1.83 pp
- leave-one-round-out keeps MDD in 9.0888–10.1692 pp

## Adjudicability

0 of 200 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 200}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 200}): [128.29, 132.88, 136.11, 132.09]
strongest single step: after round 2 (130.583 → 134.1, 2.69%, variance explained 0.3992). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 0 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 10 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 29 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 38 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 47 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 48 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 16 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 20 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 21 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 22 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 24 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 27 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 34 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 36 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 49 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
