# Noise floor — terminal-bench 2.0 terminus-2__openai_gpt-oss-120b_together_ai

925 manifests, 89 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]; outcomes {'completed': 925}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 16 | 17.9775 |
| 2 | 89 | 11 | 12.3596 |
| 3 | 89 | 18 | 20.2247 |
| 4 | 89 | 18 | 20.2247 |
| 5 | 89 | 19 | 21.3483 |
| 6 | 89 | 21 | 23.5955 |
| 7 | 89 | 16 | 17.9775 |
| 8 | 89 | 17 | 19.1011 |
| 9 (partial) | 87 | 20 | 22.9885 |
| 10 (partial) | 86 | 11 | 12.7907 |
| 11 (partial) | 20 | 5 | 25.0 |
| 12 (partial) | 20 | 6 | 30.0 |

Complete rounds: mean 19.1011 %, sd 3.2895 pp, observed range 11.2359 pp.

## Headline

- single-run sd **2.7835 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.7153 pp** before the gap is outside noise; 11.0283 pp for 80% power
- 33 of 89 tasks flipped; mean flip rate 0.1534 (max possible at n=10: 0.5556)
- re-run (plugin) sd 2.7835 pp, (posterior) 3.3535 pp; bootstrap precision of this estimate 0.8687 pp
- leave-one-round-out keeps MDD in 7.5626–7.8001 pp

## Adjudicability

1 of 925 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 924, 'none': 1}.

## Drift screen

series (median completion tokens per round, {'run_total': 923}): [5582.0, 4510.0, 5404.0, 4485.0, 4404.0, 5320.5, 5616.5, 4895.0, 4028.0, 4748.5, 5502.0, 4393.0]
strongest single step: after round 8 (5027.125 → 4667.875, -7.15%, variance explained 0.1018). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-pmars | 6/12 | 0.5 | 0.2538–0.7462 | 0.5455 |
| custom-memory-heap-crash | 6/12 | 0.5 | 0.2538–0.7462 | 0.5455 |
| git-leak-recovery | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| git-multibranch | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| headless-terminal | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| mcmc-sampling-stan | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| nginx-request-logging | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| portfolio-optimization | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| pypi-server | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| sqlite-with-gcov | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| vulnerable-secret | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| winning-avg-corewars | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| configure-git-webserver | 8/12 | 0.6667 | 0.3906–0.8619 | 0.4848 |
| fix-git | 8/10 | 0.8 | 0.4902–0.9433 | 0.3556 |
| large-scale-text-editing | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
