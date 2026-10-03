# Noise floor — tau2-bench leaderboard gpt-5-2-none_retail

456 manifests, 114 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 405, 'unknown': 51}; verifier versions ['7324fb57cb6819e77937c79964db916f5b068e31']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 114 | 85 | 74.5614 |
| 2 | 114 | 85 | 74.5614 |
| 3 | 111 | 87 | 78.3784 |
| 4 | 66 | 51 | 77.2727 |

Complete rounds: mean 76.1935 %, sd 1.9379 pp, observed range 3.817 pp.

## Headline

- single-run sd **2.8108 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.791 pp** before the gap is outside noise; 11.1365 pp for 80% power
- 48 of 114 tasks flipped; mean flip rate 0.2544 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.8108 pp, (posterior) 3.6009 pp; bootstrap precision of this estimate 1.5066 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- flips by verdict basis: DB: 2/2 flipped, mean flip rate 0.5; DB+NL_ASSERTION: 28/72 flipped, mean flip rate 0.2407; DB+NL_ASSERTION:nl: 18/40 flipped, mean flip rate 0.2667
- leave-one-round-out keeps MDD in 7.0157–7.4966 pp

## Adjudicability

0 of 456 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 456}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 405, 'run_total': 51}): [175.77, 176.8, 169.99, 108.57]
strongest single step: after round 2 (176.287 → 139.281, -20.99%, variance explained 0.4206). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 102 | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| 105 | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| 107 | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| 109 | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| 110 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 18 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 20 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 27 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 30 | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| 37 | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| 41 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 45 | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| 46 | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| 5 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 56 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
