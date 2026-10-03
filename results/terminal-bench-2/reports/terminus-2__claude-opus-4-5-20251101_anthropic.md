# Noise floor — terminal-bench 2.0 terminus-2__claude-opus-4-5-20251101_anthropic

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 51 | 57.3034 |
| 2 | 89 | 49 | 55.0562 |
| 3 | 89 | 56 | 62.9213 |
| 4 | 89 | 52 | 58.427 |
| 5 | 89 | 49 | 55.0562 |

Complete rounds: mean 57.7528 %, sd 3.237 pp, observed range 7.8651 pp.

## Headline

- single-run sd **2.5879 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.1732 pp** before the gap is outside noise; 10.2534 pp for 80% power
- 28 of 89 tasks flipped; mean flip rate 0.1483 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.5879 pp, (posterior) 3.5973 pp; bootstrap precision of this estimate 1.1555 pp
- leave-one-round-out keeps MDD in 6.6346–7.2463 pp

## Adjudicability

0 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 445}.

## Drift screen

series (median completion tokens per round, {'run_total': 445}): [6338.0, 7023.0, 6470.0, 7566.0, 6787.0]
strongest single step: after round 3 (6610.333 → 7176.5, 8.56%, variance explained 0.404). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-cython-ext | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pov-ray | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| circuit-fibsqrt | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mailman | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| password-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sqlite-with-gcov | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| torch-tensor-parallelism | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| tune-mjcf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| write-compressor | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| adaptive-rejection-sampler | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| bn-fit-modify | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| cancel-async-tasks | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| compile-compcert | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| count-dataset-tokens | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
