# Noise floor — terminal-bench 2.0 terminus-2__deepseek-v3.2_deepseek

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 39 | 43.8202 |
| 2 | 89 | 33 | 37.0787 |
| 3 | 89 | 34 | 38.2022 |
| 4 | 89 | 32 | 35.9551 |
| 5 | 89 | 38 | 42.6966 |

Complete rounds: mean 39.5506 %, sd 3.4994 pp, observed range 7.8651 pp.

## Headline

- single-run sd **2.8069 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.7802 pp** before the gap is outside noise; 11.121 pp for 80% power
- 33 of 89 tasks flipped; mean flip rate 0.1753 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.8069 pp, (posterior) 3.767 pp; bootstrap precision of this estimate 1.2679 pp
- leave-one-round-out keeps MDD in 7.2117–7.8595 pp

## Adjudicability

72 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 373, 'none': 72}.

## Drift screen

series (median completion tokens per round, {'run_total': 445}): [12715.0, 14082.0, 12317.0, 13820.0, 12020.0]
strongest single step: after round 2 (13398.5 → 12719.0, -5.07%, variance explained 0.1654). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| compile-compcert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| configure-git-webserver | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| count-dataset-tokens | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| crack-7z-hash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-linear-cryptanalysis | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-code-vulnerability | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| password-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| reshard-c4-data | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sparql-university | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| winning-avg-corewars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| adaptive-rejection-sampler | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| bn-fit-modify | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| build-cython-ext | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
