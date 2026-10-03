# Noise floor — terminal-bench 2.0 terminus-2__kimi-k2.5_kimi

435 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 435}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 37 | 41.573 |
| 2 | 89 | 40 | 44.9438 |
| 3 | 89 | 40 | 44.9438 |
| 4 (partial) | 88 | 40 | 45.4545 |
| 5 (partial) | 80 | 32 | 40.0 |

Complete rounds: mean 43.8202 %, sd 1.9461 pp, observed range 3.3708 pp.

## Headline

- single-run sd **2.893 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.0188 pp** before the gap is outside noise; 11.4622 pp for 80% power
- 34 of 89 tasks flipped; mean flip rate 0.1876 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.893 pp, (posterior) 3.832 pp; bootstrap precision of this estimate 1.3071 pp
- leave-one-round-out keeps MDD in 7.6028–7.936 pp

## Adjudicability

435 of 435 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 435}.

## Drift screen

series (median completion tokens per round, {'run_total': 435}): [10039.0, 8174.0, 8223.0, 9004.0, 9401.5]
strongest single step: after round 3 (8812.0 → 9202.75, 4.43%, variance explained 0.0727). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| bn-fit-modify | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-cython-ext | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| cancel-async-tasks | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| count-dataset-tokens | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| largest-eigenval | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| openssl-selfsigned-cert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| password-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-cli | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| schemelike-metacircular-eval | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sqlite-with-gcov | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| tune-mjcf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-recovery | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
