# Noise floor — tau2-bench leaderboard gemini-3-flash_airline

200 manifests, 50 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 200}; verifier versions ['5a629d14503111171dc7166a3cf8bf3870b73a79']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 50 | 34 | 68.0 |
| 2 | 50 | 33 | 66.0 |
| 3 | 50 | 34 | 68.0 |
| 4 | 50 | 33 | 66.0 |

Complete rounds: mean 67.0 %, sd 1.1547 pp, observed range 2.0 pp.

## Headline

- single-run sd **1.9989 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **5.5406 pp** before the gap is outside noise; 7.9197 pp for 80% power
- 5 of 50 tasks flipped; mean flip rate 0.0533 (max possible at n=4: 0.6667)
- re-run (plugin) sd 1.9989 pp, (posterior) 4.5671 pp; bootstrap precision of this estimate 0.9912 pp
- leave-one-round-out keeps MDD in 4.5574–5.8233 pp

## Adjudicability

0 of 200 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 200}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 200}): [547.98, 501.24, 492.91, 496.19]
strongest single step: after round 2 (524.609 → 494.549, -5.73%, variance explained 0.4515). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 34 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 31 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 32 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 5 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 8 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
