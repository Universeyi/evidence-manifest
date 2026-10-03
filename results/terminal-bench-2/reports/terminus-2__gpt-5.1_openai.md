# Noise floor — terminal-bench 2.0 terminus-2__gpt-5.1_openai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5, 6]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 45 | 50.5618 |
| 2 | 89 | 46 | 51.6854 |
| 3 | 89 | 40 | 44.9438 |
| 4 | 89 | 39 | 43.8202 |
| 5 (partial) | 88 | 42 | 47.7273 |
| 6 (partial) | 1 | 0 | 0.0 |

Complete rounds: mean 47.7528 %, sd 3.946 pp, observed range 7.8652 pp.

## Headline

- single-run sd **2.8649 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.941 pp** before the gap is outside noise; 11.3508 pp for 80% power
- 33 of 89 tasks flipped; mean flip rate 0.1764 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.8649 pp, (posterior) 3.7502 pp; bootstrap precision of this estimate 1.2526 pp
- leave-one-round-out keeps MDD in 7.3846–8.0069 pp

## Adjudicability

0 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 445}.

## Drift screen

series (median completion tokens per round, {'run_total': 444}): [30223.0, 26414.5, 32923.0, 28756.0, 26252.5, 12676.0]
strongest single step: after round 4 (29579.125 → 19464.25, -34.2%, variance explained 0.5438). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| bn-fit-modify | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| break-filter-js-from-html | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| cancel-async-tasks | 3/6 | 0.5 | 0.1876–0.8124 | 0.6 |
| feal-linear-cryptanalysis | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| fix-code-vulnerability | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| hf-model-inference | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| kv-store-grpc | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| log-summary-date-ranges | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| password-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| tune-mjcf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| circuit-fibsqrt | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| build-pov-ray | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| code-from-image | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
