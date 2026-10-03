# Noise floor — tau2-bench leaderboard gemini-3-pro_airline

200 manifests, 50 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 197, 'unknown': 3}; verifier versions ['ef9454a8dae83fbcedea47f2eb9955f95c2bcf5b']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 47 | 38 | 80.8511 |
| 2 | 50 | 41 | 82.0 |
| 3 | 50 | 42 | 84.0 |
| 4 | 50 | 40 | 80.0 |

Complete rounds: mean 81.7128 %, sd 1.7311 pp, observed range 4.0 pp.

## Headline

- single-run sd **2.7103 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.5124 pp** before the gap is outside noise; 10.7383 pp for 80% power
- 9 of 50 tasks flipped; mean flip rate 0.0967 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.7103 pp, (posterior) 4.8151 pp; bootstrap precision of this estimate 1.3468 pp
- leave-one-round-out keeps MDD in 6.4364–7.8863 pp

## Adjudicability

0 of 200 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 200}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 197, 'run_total': 3}): [596.04, 615.04, 652.33, 506.97]
strongest single step: after round 2 (605.54 → 579.65, -4.28%, variance explained 0.0587). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 18 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 31 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 15 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 24 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 25 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 29 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 35 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 43 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 6 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
