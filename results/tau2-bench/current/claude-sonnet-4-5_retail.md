# Noise floor — tau2-bench leaderboard claude-sonnet-4-5_retail

456 manifests, 114 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 456}; verifier versions ['7324fb57cb6819e77937c79964db916f5b068e31']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 114 | 87 | 76.3158 |
| 2 | 114 | 88 | 77.193 |
| 3 | 114 | 82 | 71.9298 |
| 4 | 114 | 73 | 64.0351 |

Complete rounds: mean 72.3684 %, sd 6.0137 pp, observed range 13.1579 pp.

## Headline

- single-run sd **3.1373 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.696 pp** before the gap is outside noise; 12.4301 pp for 80% power
- 63 of 114 tasks flipped; mean flip rate 0.2983 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.1373 pp, (posterior) 3.7827 pp; bootstrap precision of this estimate 1.5801 pp
- flips by verdict basis: DB: 0/2 flipped, mean flip rate 0.0; DB+NL_ASSERTION: 43/72 flipped, mean flip rate 0.3218; DB+NL_ASSERTION:nl: 20/40 flipped, mean flip rate 0.2708
- leave-one-round-out keeps MDD in 7.8165–8.5519 pp

## Adjudicability

0 of 456 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 456}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 456}): [141.65, 139.38, 142.32, 144.01]
strongest single step: after round 2 (140.516 → 143.165, 1.89%, variance explained 0.6371). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 101 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 102 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 103 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 109 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 112 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 29 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 32 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 45 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 47 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 52 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 7 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 71 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 9 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 96 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 98 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
