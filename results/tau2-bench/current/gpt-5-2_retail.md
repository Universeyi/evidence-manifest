# Noise floor — tau2-bench leaderboard gpt-5-2_retail

456 manifests, 114 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 456}; verifier versions ['7324fb57cb6819e77937c79964db916f5b068e31']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 114 | 99 | 86.8421 |
| 2 | 114 | 92 | 80.7018 |
| 3 | 114 | 97 | 85.0877 |
| 4 | 114 | 84 | 73.6842 |

Complete rounds: mean 81.579 %, sd 5.8626 pp, observed range 13.1579 pp.

## Headline

- single-run sd **2.789 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.7306 pp** before the gap is outside noise; 11.0501 pp for 80% power
- 51 of 114 tasks flipped; mean flip rate 0.2398 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.789 pp, (posterior) 3.5772 pp; bootstrap precision of this estimate 1.4055 pp
- flips by verdict basis: DB: 2/2 flipped, mean flip rate 0.5; DB+NL_ASSERTION: 29/72 flipped, mean flip rate 0.2153; DB+NL_ASSERTION:nl: 20/40 flipped, mean flip rate 0.2708
- leave-one-round-out keeps MDD in 6.7114–7.8814 pp

## Adjudicability

0 of 456 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 456}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 456}): [261.15, 251.76, 249.98, 246.42]
strongest single step: after round 2 (256.457 → 248.199, -3.22%, variance explained 0.575). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 100 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 103 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 110 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 27 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 31 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 32 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 37 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 41 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 60 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 79 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 95 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 102 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 104 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 105 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 107 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
