# Noise floor — terminal-bench 2.0 terminus-2__glm-5_z-ai

442 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 442}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 50 | 56.1798 |
| 2 | 89 | 44 | 49.4382 |
| 3 | 89 | 44 | 49.4382 |
| 4 (partial) | 88 | 46 | 52.2727 |
| 5 (partial) | 87 | 47 | 54.023 |

Complete rounds: mean 51.6854 %, sd 3.8923 pp, observed range 6.7416 pp.

## Headline

- single-run sd **2.655 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.3591 pp** before the gap is outside noise; 10.5192 pp for 80% power
- 31 of 89 tasks flipped; mean flip rate 0.1584 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.655 pp, (posterior) 3.7072 pp; bootstrap precision of this estimate 1.2185 pp
- leave-one-round-out keeps MDD in 6.7457–7.7137 pp

## Adjudicability

66 of 442 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 376, 'none': 66}.

## Drift screen

series (median completion tokens per round, {'run_total': 442}): [0.0, 0.0, 0.0, 0.0, 0.0]
strongest single step: after round 2 (0.0 → 0.0, None%, variance explained 1.0). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pov-ray | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-elf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| feal-differential-cryptanalysis | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| log-summary-date-ranges | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-startup | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sparql-university | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| tune-mjcf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| compile-compcert | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| bn-fit-modify | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| build-cython-ext | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| cancel-async-tasks | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| circuit-fibsqrt | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| configure-git-webserver | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| count-dataset-tokens | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
