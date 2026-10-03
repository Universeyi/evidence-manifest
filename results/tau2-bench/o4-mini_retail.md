# Noise floor — tau2-bench o4-mini_retail

456 manifests, 114 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 456}; verifier versions ['c30d59aaa71c65f9b9eb6a8f8636b48945028fcf']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 114 | 79 | 69.2982 |
| 2 | 114 | 83 | 72.807 |
| 3 | 114 | 84 | 73.6842 |
| 4 | 114 | 80 | 70.1754 |

Complete rounds: mean 71.4912 %, sd 2.0882 pp, observed range 4.386 pp.

## Headline

- single-run sd **2.847 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.8913 pp** before the gap is outside noise; 11.2799 pp for 80% power
- 52 of 114 tasks flipped; mean flip rate 0.2427 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.847 pp, (posterior) 3.5984 pp; bootstrap precision of this estimate 1.4253 pp
- leave-one-round-out keeps MDD in 7.2006–7.7616 pp

## Adjudicability

0 of 456 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 456}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 456}): [363.0, 329.04, 351.31, 338.61]
strongest single step: after round 2 (346.021 → 344.963, -0.31%, variance explained 0.0017). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 0 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 104 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 27 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 38 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 45 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 66 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 69 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 8 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 82 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 94 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 102 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 103 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 105 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 106 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 107 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
