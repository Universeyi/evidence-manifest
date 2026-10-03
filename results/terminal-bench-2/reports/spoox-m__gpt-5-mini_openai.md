# Noise floor — terminal-bench 2.0 spoox-m__gpt-5-mini_openai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 36 | 40.4494 |
| 2 | 89 | 31 | 34.8315 |
| 3 | 89 | 30 | 33.7079 |
| 4 | 89 | 26 | 29.2135 |
| 5 | 89 | 32 | 35.9551 |

Complete rounds: mean 34.8315 %, sd 4.0512 pp, observed range 11.2359 pp.

## Headline

- single-run sd **2.7685 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.6737 pp** before the gap is outside noise; 10.9689 pp for 80% power
- 30 of 89 tasks flipped; mean flip rate 0.1708 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.7685 pp, (posterior) 3.7413 pp; bootstrap precision of this estimate 1.2363 pp
- leave-one-round-out keeps MDD in 7.2341–7.7178 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pov-ray | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| code-from-image | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| constraints-scheduling | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-linear-cryptanalysis | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| headless-terminal | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| large-scale-text-editing | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mailman | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| password-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| reshard-c4-data | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| rstan-to-pystan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sparql-university | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
