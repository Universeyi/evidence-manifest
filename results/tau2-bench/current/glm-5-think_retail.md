# Noise floor — tau2-bench leaderboard glm-5-think_retail

456 manifests, 114 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 452, 'unknown': 4}; verifier versions ['unknown']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 111 | 82 | 73.8739 |
| 2 | 113 | 87 | 76.9912 |
| 3 | 114 | 84 | 73.6842 |
| 4 | 114 | 83 | 72.807 |

Complete rounds: mean 74.3391 %, sd 1.8281 pp, observed range 4.1842 pp.

## Headline

- single-run sd **2.9319 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.1267 pp** before the gap is outside noise; 11.6163 pp for 80% power
- 54 of 114 tasks flipped; mean flip rate 0.2573 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.9319 pp, (posterior) 3.6264 pp; bootstrap precision of this estimate 1.4549 pp
- flips by verdict basis: DB: 2/2 flipped, mean flip rate 0.5; DB+NL_ASSERTION: 34/72 flipped, mean flip rate 0.2616; DB+NL_ASSERTION:nl: 18/40 flipped, mean flip rate 0.2375
- leave-one-round-out keeps MDD in 7.5127–7.7575 pp

## Adjudicability

0 of 456 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 456}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 452, 'run_total': 4}): [259.43, 257.45, 253.71, 257.06]
strongest single step: after round 2 (258.44 → 255.385, -1.18%, variance explained 0.5526). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 0 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 100 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 108 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 30 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 42 | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| 46 | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| 52 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 6 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 71 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 72 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 74 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 76 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 91 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 98 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 101 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
