# Noise floor — terminal-bench 2.0 terminus-2__glm-4.7_z-ai

427 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 427}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 34 | 38.2022 |
| 2 | 89 | 27 | 30.3371 |
| 3 | 89 | 26 | 29.2135 |
| 4 (partial) | 85 | 30 | 35.2941 |
| 5 (partial) | 75 | 30 | 40.0 |

Complete rounds: mean 32.5843 %, sd 4.8976 pp, observed range 8.9887 pp.

## Headline

- single-run sd **2.7887 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.7297 pp** before the gap is outside noise; 11.0489 pp for 80% power
- 30 of 89 tasks flipped; mean flip rate 0.1757 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.7887 pp, (posterior) 3.8039 pp; bootstrap precision of this estimate 1.2891 pp
- leave-one-round-out keeps MDD in 7.1604–7.6807 pp

## Adjudicability

427 of 427 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 427}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| code-from-image | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| count-dataset-tokens | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| build-cython-ext | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| compile-compcert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| custom-memory-heap-crash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| financial-document-processor | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-git | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| large-scale-text-editing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mcmc-sampling-stan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| password-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-cli | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-startup | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sparql-university | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sqlite-with-gcov | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
