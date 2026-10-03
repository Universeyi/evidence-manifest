# Noise floor — tau-bench v1 sonnet-35-new-retail

920 manifests, 115 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8]; outcomes {'completed': 920}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 115 | 84 | 73.0435 |
| 2 | 115 | 81 | 70.4348 |
| 3 | 115 | 81 | 70.4348 |
| 4 | 115 | 79 | 68.6957 |
| 5 | 115 | 81 | 70.4348 |
| 6 | 115 | 70 | 60.8696 |
| 7 | 115 | 86 | 74.7826 |
| 8 | 115 | 75 | 65.2174 |

Complete rounds: mean 69.2391 %, sd 4.408 pp, observed range 13.913 pp.

## Headline

- single-run sd **2.9991 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.3129 pp** before the gap is outside noise; 11.8826 pp for 80% power
- 67 of 115 tasks flipped; mean flip rate 0.2326 (max possible at n=8: 0.5714)
- re-run (plugin) sd 2.9991 pp, (posterior) 3.3912 pp; bootstrap precision of this estimate 1.0495 pp
- leave-one-round-out keeps MDD in 7.9412–8.4432 pp

## Adjudicability

0 of 920 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 920}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 100 | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| 102 | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| 4 | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| 45 | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| 64 | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| 9 | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| 108 | 5/8 | 0.625 | 0.3057–0.8632 | 0.5357 |
| 110 | 3/8 | 0.375 | 0.1368–0.6943 | 0.5357 |
| 111 | 5/8 | 0.625 | 0.3057–0.8632 | 0.5357 |
| 113 | 5/8 | 0.625 | 0.3057–0.8632 | 0.5357 |
| 15 | 5/8 | 0.625 | 0.3057–0.8632 | 0.5357 |
| 16 | 5/8 | 0.625 | 0.3057–0.8632 | 0.5357 |
| 21 | 3/8 | 0.375 | 0.1368–0.6943 | 0.5357 |
| 56 | 5/8 | 0.625 | 0.3057–0.8632 | 0.5357 |
| 6 | 5/8 | 0.625 | 0.3057–0.8632 | 0.5357 |
