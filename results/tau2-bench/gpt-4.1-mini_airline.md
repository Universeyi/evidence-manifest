# Noise floor — tau2-bench gpt-4.1-mini_airline

200 manifests, 50 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 200}; verifier versions ['ade39493be54aad326a4c65295f77fe09780329b']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 50 | 25 | 50.0 |
| 2 | 50 | 26 | 52.0 |
| 3 | 50 | 25 | 50.0 |
| 4 | 50 | 25 | 50.0 |

Complete rounds: mean 50.5 %, sd 1.0 pp, observed range 2.0 pp.

## Headline

- single-run sd **4.1273 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **11.4401 pp** before the gap is outside noise; 16.3525 pp for 80% power
- 21 of 50 tasks flipped; mean flip rate 0.2233 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.1273 pp, (posterior) 5.3048 pp; bootstrap precision of this estimate 2.0223 pp
- leave-one-round-out keeps MDD in 9.8399–11.4287 pp

## Adjudicability

0 of 200 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 200}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 200}): [79.06, 73.28, 79.02, 83.97]
strongest single step: after round 2 (76.168 → 81.492, 6.99%, variance explained 0.4948). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 20 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 28 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 45 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 9 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 11 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 12 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 17 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 19 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 26 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 27 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 3 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 30 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 31 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 33 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 34 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
