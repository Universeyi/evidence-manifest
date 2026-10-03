# Noise floor — tau-bench v1 gpt-4o-airline

200 manifests, 50 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 200}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 50 | 21 | 42.0 |
| 2 | 50 | 22 | 44.0 |
| 3 | 50 | 20 | 40.0 |
| 4 | 50 | 21 | 42.0 |

Complete rounds: mean 42.0 %, sd 1.633 pp, observed range 4.0 pp.

## Headline

- single-run sd **4.6699 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **12.9441 pp** before the gap is outside noise; 18.5023 pp for 80% power
- 26 of 50 tasks flipped; mean flip rate 0.2933 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.6699 pp, (posterior) 5.6248 pp; bootstrap precision of this estimate 2.3588 pp
- leave-one-round-out keeps MDD in 11.4071–12.7592 pp

## Adjudicability

0 of 200 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 200}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 13 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 15 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 26 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 27 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 30 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 31 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 41 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 44 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 45 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 46 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 1 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 11 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 16 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 17 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| 2 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
