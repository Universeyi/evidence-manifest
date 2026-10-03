# Noise floor — terminal-bench 2.0 goose__claude-sonnet-4-5_anthropic

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 38 | 42.6966 |
| 2 | 89 | 44 | 49.4382 |
| 3 | 89 | 34 | 38.2022 |
| 4 | 89 | 40 | 44.9438 |
| 5 | 89 | 36 | 40.4494 |

Complete rounds: mean 43.146 %, sd 4.3226 pp, observed range 11.236 pp.

## Headline

- single-run sd **2.6452 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.332 pp** before the gap is outside noise; 10.4804 pp for 80% power
- 29 of 89 tasks flipped; mean flip rate 0.1551 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.6452 pp, (posterior) 3.6553 pp; bootstrap precision of this estimate 1.1663 pp
- leave-one-round-out keeps MDD in 6.9223–7.3608 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| bn-fit-modify | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| cancel-async-tasks | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| compile-compcert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| distribution-search | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| feal-differential-cryptanalysis | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| hf-model-inference | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-alpine-ssh | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| regex-log | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| rstan-to-pystan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| tune-mjcf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| adaptive-rejection-sampler | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| build-cython-ext | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| build-pov-ray | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| crack-7z-hash | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
