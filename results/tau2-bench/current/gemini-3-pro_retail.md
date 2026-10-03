# Noise floor — tau2-bench leaderboard gemini-3-pro_retail

456 manifests, 114 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 436, 'unknown': 20}; verifier versions ['ef9454a8dae83fbcedea47f2eb9955f95c2bcf5b']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 114 | 96 | 84.2105 |
| 2 | 105 | 77 | 73.3333 |
| 3 | 103 | 79 | 76.699 |
| 4 | 114 | 94 | 82.4561 |

Complete rounds: mean 79.1747 %, sd 5.0457 pp, observed range 10.8772 pp.

## Headline

- single-run sd **2.5431 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.049 pp** before the gap is outside noise; 10.0759 pp for 80% power
- 41 of 114 tasks flipped; mean flip rate 0.2018 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.5431 pp, (posterior) 3.5477 pp; bootstrap precision of this estimate 1.3026 pp
- flips by verdict basis: DB: 0/2 flipped, mean flip rate 0.0; DB+NL_ASSERTION: 28/72 flipped, mean flip rate 0.2153; DB+NL_ASSERTION:nl: 13/40 flipped, mean flip rate 0.1875
- leave-one-round-out keeps MDD in 6.0234–7.378 pp

## Adjudicability

0 of 456 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 456}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 436, 'run_total': 20}): [390.75, 378.03, 371.44, 408.64]
strongest single step: after round 2 (384.391 → 390.04, 1.47%, variance explained 0.0397). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 100 | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| 103 | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| 105 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 112 | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| 2 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 29 | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| 37 | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| 72 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 74 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 79 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 82 | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| 84 | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| 91 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 95 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 99 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
