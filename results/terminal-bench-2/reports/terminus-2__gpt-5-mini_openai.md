# Noise floor — terminal-bench 2.0 terminus-2__gpt-5-mini_openai

438 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 438}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 19 | 21.3483 |
| 2 | 89 | 26 | 29.2135 |
| 3 | 89 | 27 | 30.3371 |
| 4 | 89 | 18 | 20.2247 |
| 5 (partial) | 82 | 17 | 20.7317 |

Complete rounds: mean 25.2809 %, sd 5.2301 pp, observed range 10.1124 pp.

## Headline

- single-run sd **2.5901 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.1793 pp** before the gap is outside noise; 10.2621 pp for 80% power
- 27 of 89 tasks flipped; mean flip rate 0.1483 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.5901 pp, (posterior) 3.6304 pp; bootstrap precision of this estimate 1.1603 pp
- leave-one-round-out keeps MDD in 6.5351–7.2802 pp

## Adjudicability

1 of 438 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 437, 'none': 1}.

## Drift screen

series (median completion tokens per round, {'run_total': 438}): [10173.0, 10289.0, 12252.0, 10347.0, 11188.5]
strongest single step: after round 2 (10231.0 → 11262.5, 10.08%, variance explained 0.411). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-cython-ext | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pmars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| db-wal-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| distribution-search | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-linear-cryptanalysis | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-git | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-startup | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| regex-log | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| vulnerable-secret | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| bn-fit-modify | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| cancel-async-tasks | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| code-from-image | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
