# Noise floor — tau2-bench gpt-4.1_airline

200 manifests, 50 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 200}; verifier versions ['c30d59aaa71c65f9b9eb6a8f8636b48945028fcf']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 50 | 29 | 58.0 |
| 2 | 50 | 27 | 54.0 |
| 3 | 50 | 30 | 60.0 |
| 4 | 50 | 26 | 52.0 |

Complete rounds: mean 56.0 %, sd 3.6515 pp, observed range 8.0 pp.

## Headline

- single-run sd **3.9438 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **10.9315 pp** before the gap is outside noise; 15.6255 pp for 80% power
- 19 of 50 tasks flipped; mean flip rate 0.2067 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.9438 pp, (posterior) 5.2775 pp; bootstrap precision of this estimate 1.9796 pp
- leave-one-round-out keeps MDD in 9.695–10.8048 pp

## Adjudicability

0 of 200 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 200}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 200}): [74.39, 79.41, 74.58, 79.47]
strongest single step: after round 2 (76.904 → 77.023, 0.15%, variance explained 0.0006). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 10 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 12 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 37 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 42 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 43 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 1 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 17 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 2 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 20 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 22 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 24 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 25 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 27 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 29 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 38 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
