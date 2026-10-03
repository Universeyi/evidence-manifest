# Noise floor — terminal-bench 2.0 terminus-2__gpt-5-codex_openai

437 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 437}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 41 | 46.0674 |
| 2 | 89 | 38 | 42.6966 |
| 3 | 89 | 33 | 37.0787 |
| 4 | 89 | 41 | 46.0674 |
| 5 (partial) | 81 | 40 | 49.3827 |

Complete rounds: mean 42.9775 %, sd 4.2415 pp, observed range 8.9887 pp.

## Headline

- single-run sd **2.8769 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.9742 pp** before the gap is outside noise; 11.3984 pp for 80% power
- 37 of 89 tasks flipped; mean flip rate 0.1899 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.8769 pp, (posterior) 3.8693 pp; bootstrap precision of this estimate 1.3001 pp
- leave-one-round-out keeps MDD in 7.4431–7.9947 pp

## Adjudicability

0 of 437 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 437}.

## Drift screen

series (median completion tokens per round, {'run_total': 437}): [19899.0, 19237.0, 20984.0, 18305.0, 15105.0]
strongest single step: after round 3 (20040.0 → 16705.0, -16.64%, variance explained 0.6666). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| compile-compcert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| financial-document-processor | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| llm-inference-batching-scheduler | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mcmc-sampling-stan | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-cli | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-alpine-ssh | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| regex-log | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sparql-university | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| winning-avg-corewars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| password-recovery | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| adaptive-rejection-sampler | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| bn-fit-modify | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| break-filter-js-from-html | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| build-cython-ext | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
