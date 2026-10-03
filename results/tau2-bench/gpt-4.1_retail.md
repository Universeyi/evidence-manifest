# Noise floor — tau2-bench gpt-4.1_retail

456 manifests, 114 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 456}; verifier versions ['c30d59aaa71c65f9b9eb6a8f8636b48945028fcf']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 114 | 84 | 73.6842 |
| 2 | 114 | 81 | 71.0526 |
| 3 | 114 | 86 | 75.4386 |
| 4 | 114 | 87 | 76.3158 |

Complete rounds: mean 74.1228 %, sd 2.3209 pp, observed range 5.2632 pp.

## Headline

- single-run sd **2.5819 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.1565 pp** before the gap is outside noise; 10.2296 pp for 80% power
- 43 of 114 tasks flipped; mean flip rate 0.1988 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.5819 pp, (posterior) 3.5079 pp; bootstrap precision of this estimate 1.2782 pp
- leave-one-round-out keeps MDD in 6.6257–6.8749 pp

## Adjudicability

0 of 456 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 456}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 456}): [67.85, 70.7, 67.08, 68.22]
strongest single step: after round 2 (69.277 → 67.651, -2.35%, variance explained 0.36). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 107 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 109 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 15 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 43 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 64 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 74 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 79 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 1 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 100 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 101 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 103 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 104 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 105 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 106 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 110 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
