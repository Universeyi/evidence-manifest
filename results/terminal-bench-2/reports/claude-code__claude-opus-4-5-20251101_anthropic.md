# Noise floor — terminal-bench 2.0 claude-code__claude-opus-4-5-20251101_anthropic

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 48 | 53.9326 |
| 2 | 89 | 45 | 50.5618 |
| 3 | 89 | 43 | 48.3146 |
| 4 | 89 | 49 | 55.0562 |
| 5 | 89 | 47 | 52.809 |

Complete rounds: mean 52.1348 %, sd 2.706 pp, observed range 6.7416 pp.

## Headline

- single-run sd **2.5653 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.1105 pp** before the gap is outside noise; 10.1638 pp for 80% power
- 28 of 89 tasks flipped; mean flip rate 0.1483 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.5653 pp, (posterior) 3.6487 pp; bootstrap precision of this estimate 1.1543 pp
- leave-one-round-out keeps MDD in 6.5911–7.2652 pp

## Adjudicability

9 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 436, 'none': 9}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-pmars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| count-dataset-tokens | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-elf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| financial-document-processor | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| headless-terminal | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| openssl-selfsigned-cert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| path-tracing | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| path-tracing-reverse | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-cli | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-alpine-ssh | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| adaptive-rejection-sampler | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| circuit-fibsqrt | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| compile-compcert | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| configure-git-webserver | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| dna-assembly | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
