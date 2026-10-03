# Noise floor — tau2-bench leaderboard qwen3.5-397b-a17b-think_retail

456 manifests, 114 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 456}; verifier versions ['unknown']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 114 | 96 | 84.2105 |
| 2 | 114 | 97 | 85.0877 |
| 3 | 114 | 96 | 84.2105 |
| 4 | 114 | 96 | 84.2105 |

Complete rounds: mean 84.4298 %, sd 0.4386 pp, observed range 0.8772 pp.

## Headline

- single-run sd **2.572 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.1291 pp** before the gap is outside noise; 10.1904 pp for 80% power
- 43 of 114 tasks flipped; mean flip rate 0.2003 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.572 pp, (posterior) 3.4616 pp; bootstrap precision of this estimate 1.2977 pp
- flips by verdict basis: DB: 1/2 flipped, mean flip rate 0.25; DB+NL_ASSERTION: 30/72 flipped, mean flip rate 0.2222; DB+NL_ASSERTION:nl: 12/40 flipped, mean flip rate 0.1583
- leave-one-round-out keeps MDD in 6.3724–7.0534 pp

## Adjudicability

0 of 456 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 456}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 456}): [296.52, 330.56, 297.01, 333.51]
strongest single step: after round 2 (313.539 → 315.263, 0.55%, variance explained 0.0024). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 101 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 110 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 12 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 21 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 31 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 79 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 82 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 93 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 100 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 104 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 11 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 112 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 13 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 18 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 2 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
