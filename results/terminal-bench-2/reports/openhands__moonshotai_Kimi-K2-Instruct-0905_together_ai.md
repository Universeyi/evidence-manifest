# Noise floor — terminal-bench 2.0 openhands__moonshotai_Kimi-K2-Instruct-0905_together_ai

875 manifests, 89 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; outcomes {'completed': 875}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 27 | 30.3371 |
| 2 | 89 | 27 | 30.3371 |
| 3 | 89 | 24 | 26.9663 |
| 4 | 89 | 21 | 23.5955 |
| 5 | 89 | 24 | 26.9663 |
| 6 | 89 | 26 | 29.2135 |
| 7 | 89 | 23 | 25.8427 |
| 8 | 89 | 27 | 30.3371 |
| 9 (partial) | 88 | 20 | 22.7273 |
| 10 (partial) | 75 | 19 | 25.3333 |

Complete rounds: mean 27.9494 %, sd 2.508 pp, observed range 6.7416 pp.

## Headline

- single-run sd **2.7164 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.5293 pp** before the gap is outside noise; 10.7625 pp for 80% power
- 29 of 89 tasks flipped; mean flip rate 0.1486 (max possible at n=10: 0.5556)
- re-run (plugin) sd 2.7164 pp, (posterior) 3.3535 pp; bootstrap precision of this estimate 0.8869 pp
- leave-one-round-out keeps MDD in 7.3777–7.6069 pp

## Adjudicability

15 of 875 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 860, 'none': 15}.

## Drift screen

series (median completion tokens per round, {'run_total': 861}): [7645.0, 6877.0, 6375.0, 7375.5, 6297.0, 6786.5, 6476.0, 6805.0, 7204.0, 6668.0]
strongest single step: after round 2 (7261.0 → 6748.375, -7.06%, variance explained 0.241). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| hf-model-inference | 4/9 | 0.4444 | 0.1888–0.7333 | 0.5556 |
| build-pmars | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| build-pov-ray | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| cobol-modernization | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| code-from-image | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| git-multibranch | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| kv-store-grpc | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| largest-eigenval | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| merge-diff-arc-agi-task | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| multi-source-data-merger | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| pytorch-model-cli | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| qemu-alpine-ssh | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| rstan-to-pystan | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| sqlite-with-gcov | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| tune-mjcf | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
