# Noise floor — tau2-bench gpt-4.1-mini_retail

456 manifests, 114 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 456}; verifier versions ['ade39493be54aad326a4c65295f77fe09780329b']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 114 | 78 | 68.4211 |
| 2 | 114 | 77 | 67.5439 |
| 3 | 114 | 69 | 60.5263 |
| 4 | 114 | 77 | 67.5439 |

Complete rounds: mean 66.0088 %, sd 3.6783 pp, observed range 7.8948 pp.

## Headline

- single-run sd **2.9505 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.1782 pp** before the gap is outside noise; 11.69 pp for 80% power
- 53 of 114 tasks flipped; mean flip rate 0.2617 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.9505 pp, (posterior) 3.6835 pp; bootstrap precision of this estimate 1.4642 pp
- leave-one-round-out keeps MDD in 7.4872–7.8722 pp

## Adjudicability

0 of 456 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 456}.

## Drift screen

series (median completion tokens per round, {'per_step_mean': 456}): [68.26, 67.13, 67.41, 66.84]
strongest single step: after round 2 (67.695 → 67.125, -0.84%, variance explained 0.2889). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| 1 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 100 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 101 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 107 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 14 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 15 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 19 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 33 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 38 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 47 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 54 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 57 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 63 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 64 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| 7 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
