# Noise floor — tau-bench v1 sonnet-35-new-airline

400 manifests, 50 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8]; outcomes {'completed': 400}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 50 | 25 | 50.0 |
| 2 | 50 | 20 | 40.0 |
| 3 | 50 | 22 | 44.0 |
| 4 | 50 | 24 | 48.0 |
| 5 | 50 | 23 | 46.0 |
| 6 | 50 | 23 | 46.0 |
| 7 | 50 | 21 | 42.0 |
| 8 | 50 | 26 | 52.0 |

Complete rounds: mean 46.0 %, sd 4.0 pp, observed range 12.0 pp.

## Headline

- single-run sd **4.8518 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **13.4483 pp** before the gap is outside noise; 19.223 pp for 80% power
- 32 of 50 tasks flipped; mean flip rate 0.2686 (max possible at n=8: 0.5714)
- re-run (plugin) sd 4.8518 pp, (posterior) 5.4175 pp; bootstrap precision of this estimate 1.7075 pp
- leave-one-round-out keeps MDD in 12.9127–13.6473 pp

## Adjudicability

0 of 400 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 400}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 15 | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| 20 | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| 4 | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| 41 | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| 9 | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| 29 | 3/8 | 0.375 | 0.1368–0.6943 | 0.5357 |
| 34 | 5/8 | 0.625 | 0.3057–0.8632 | 0.5357 |
| 37 | 3/8 | 0.375 | 0.1368–0.6943 | 0.5357 |
| 5 | 5/8 | 0.625 | 0.3057–0.8632 | 0.5357 |
| 1 | 6/8 | 0.75 | 0.4093–0.9285 | 0.4286 |
| 10 | 2/8 | 0.25 | 0.0715–0.5907 | 0.4286 |
| 11 | 2/8 | 0.25 | 0.0715–0.5907 | 0.4286 |
| 13 | 6/8 | 0.75 | 0.4093–0.9285 | 0.4286 |
| 14 | 6/8 | 0.75 | 0.4093–0.9285 | 0.4286 |
| 16 | 6/8 | 0.75 | 0.4093–0.9285 | 0.4286 |
