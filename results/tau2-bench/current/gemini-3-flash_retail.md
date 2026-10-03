# Noise floor — tau2-bench leaderboard gemini-3-flash_retail

456 manifests, 114 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 456}; verifier versions ['ef9454a8dae83fbcedea47f2eb9955f95c2bcf5b']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 114 | 87 | 76.3158 |
| 2 | 114 | 86 | 75.4386 |
| 3 | 114 | 89 | 78.0702 |
| 4 | 114 | 88 | 77.193 |

Complete rounds: mean 76.7544 %, sd 1.1325 pp, observed range 2.6316 pp.

## Headline

- single-run sd **2.6721 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.4065 pp** before the gap is outside noise; 10.587 pp for 80% power
- 45 of 114 tasks flipped; mean flip rate 0.2164 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.6721 pp, (posterior) 3.5339 pp; bootstrap precision of this estimate 1.3349 pp
- flips by verdict basis: DB: 1/2 flipped, mean flip rate 0.25; DB+NL_ASSERTION: 26/72 flipped, mean flip rate 0.2037; DB+NL_ASSERTION:nl: 18/40 flipped, mean flip rate 0.2375
- leave-one-round-out keeps MDD in 6.7155–7.202 pp

## Adjudicability

0 of 456 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 456}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 456}): [322.9, 308.94, 332.54, 338.82]
strongest single step: after round 2 (315.919 → 335.678, 6.25%, variance explained 0.7692). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 101 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 103 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 112 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 27 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 30 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 46 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 56 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 59 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 6 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 79 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 9 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 90 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 91 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 100 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 102 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
