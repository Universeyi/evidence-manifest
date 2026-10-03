# Noise floor — terminal-bench 2.0 terminus-2__gpt-5_openai

438 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 438}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 33 | 37.0787 |
| 2 | 89 | 35 | 39.3258 |
| 3 | 89 | 31 | 34.8315 |
| 4 | 89 | 29 | 32.5843 |
| 5 (partial) | 82 | 28 | 34.1463 |

Complete rounds: mean 35.9551 %, sd 2.9011 pp, observed range 6.7415 pp.

## Headline

- single-run sd **3.123 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.6564 pp** before the gap is outside noise; 12.3735 pp for 80% power
- 36 of 89 tasks flipped; mean flip rate 0.2135 (max possible at n=5: 0.6)
- re-run (plugin) sd 3.123 pp, (posterior) 3.9251 pp; bootstrap precision of this estimate 1.3959 pp
- leave-one-round-out keeps MDD in 7.8852–8.5455 pp

## Adjudicability

2 of 438 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 436, 'none': 2}.

## Drift screen

series (median completion tokens per round, {'run_total': 438}): [13030.0, 15133.0, 14124.0, 13475.0, 13812.0]
strongest single step: after round 3 (14095.667 → 13643.5, -3.21%, variance explained 0.0976). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| bn-fit-modify | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| break-filter-js-from-html | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pmars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| cancel-async-tasks | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| circuit-fibsqrt | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| cobol-modernization | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| code-from-image | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| count-dataset-tokens | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| db-wal-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-linear-cryptanalysis | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| git-leak-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| kv-store-grpc | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
