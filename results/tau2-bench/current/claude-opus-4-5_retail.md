# Noise floor — tau2-bench leaderboard claude-opus-4-5_retail

456 manifests, 114 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 456}; verifier versions ['7324fb57cb6819e77937c79964db916f5b068e31']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 114 | 92 | 80.7018 |
| 2 | 114 | 90 | 78.9474 |
| 3 | 114 | 94 | 82.4561 |
| 4 | 114 | 87 | 76.3158 |

Complete rounds: mean 79.6053 %, sd 2.6194 pp, observed range 6.1403 pp.

## Headline

- single-run sd **2.8407 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.8739 pp** before the gap is outside noise; 11.255 pp for 80% power
- 52 of 114 tasks flipped; mean flip rate 0.2442 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.8407 pp, (posterior) 3.6293 pp; bootstrap precision of this estimate 1.4124 pp
- flips by verdict basis: DB: 2/2 flipped, mean flip rate 0.5; DB+NL_ASSERTION: 31/72 flipped, mean flip rate 0.2292; DB+NL_ASSERTION:nl: 19/40 flipped, mean flip rate 0.2583
- leave-one-round-out keeps MDD in 7.2364–7.9678 pp

## Adjudicability

0 of 456 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 456}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 456}): [224.57, 234.42, 228.11, 230.04]
strongest single step: after round 2 (229.497 → 229.078, -0.18%, variance explained 0.0035). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 10 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 103 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 104 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 105 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 109 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 12 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 72 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 91 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 92 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 95 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 98 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 1 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 100 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 110 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 111 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
