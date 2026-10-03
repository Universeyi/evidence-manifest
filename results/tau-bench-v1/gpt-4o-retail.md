# Noise floor — tau-bench v1 gpt-4o-retail

460 manifests, 115 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 460}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 115 | 71 | 61.7391 |
| 2 | 115 | 71 | 61.7391 |
| 3 | 115 | 69 | 60.0 |
| 4 | 115 | 67 | 58.2609 |

Complete rounds: mean 60.4348 %, sd 1.6651 pp, observed range 3.4782 pp.

## Headline

- single-run sd **2.7374 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.5875 pp** before the gap is outside noise; 10.8457 pp for 80% power
- 49 of 115 tasks flipped; mean flip rate 0.2261 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.7374 pp, (posterior) 3.5765 pp; bootstrap precision of this estimate 1.3326 pp
- leave-one-round-out keeps MDD in 6.8979–7.1876 pp

## Adjudicability

0 of 460 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 460}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 0 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 14 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 16 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 32 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 56 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 64 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 76 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 85 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 87 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 100 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 104 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 106 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 107 | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| 109 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 113 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
