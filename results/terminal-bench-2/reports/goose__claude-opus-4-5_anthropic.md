# Noise floor — terminal-bench 2.0 goose__claude-opus-4-5_anthropic

442 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 442}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 49 | 55.0562 |
| 2 | 89 | 48 | 53.9326 |
| 3 | 89 | 48 | 53.9326 |
| 4 | 89 | 46 | 51.6854 |
| 5 (partial) | 86 | 48 | 55.814 |

Complete rounds: mean 53.6517 %, sd 1.4138 pp, observed range 3.3708 pp.

## Headline

- single-run sd **2.6913 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.4598 pp** before the gap is outside noise; 10.663 pp for 80% power
- 29 of 89 tasks flipped; mean flip rate 0.1584 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.6913 pp, (posterior) 3.6251 pp; bootstrap precision of this estimate 1.1907 pp
- leave-one-round-out keeps MDD in 6.8441–7.6108 pp

## Adjudicability

442 of 442 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 442}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| code-from-image | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| configure-git-webserver | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| count-dataset-tokens | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-differential-cryptanalysis | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| financial-document-processor | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mailman | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| openssl-selfsigned-cert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| path-tracing-reverse | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| rstan-to-pystan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| torch-pipeline-parallelism | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| tune-mjcf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-recovery | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| circuit-fibsqrt | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| compile-compcert | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
