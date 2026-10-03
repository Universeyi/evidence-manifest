# Noise floor — terminal-bench 2.0 terminus-2__accounts_fireworks_models_glm-4p6_fireworks_ai

904 manifests, 89 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]; outcomes {'completed': 904}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 21 | 23.5955 |
| 2 | 89 | 20 | 22.4719 |
| 3 | 89 | 27 | 30.3371 |
| 4 | 89 | 19 | 21.3483 |
| 5 | 89 | 24 | 26.9663 |
| 6 | 89 | 24 | 26.9663 |
| 7 | 89 | 20 | 22.4719 |
| 8 | 89 | 22 | 24.7191 |
| 9 (partial) | 88 | 20 | 22.7273 |
| 10 (partial) | 88 | 23 | 26.1364 |
| 11 (partial) | 8 | 2 | 25.0 |
| 12 (partial) | 8 | 2 | 25.0 |

Complete rounds: mean 24.8595 %, sd 3.0291 pp, observed range 8.9888 pp.

## Headline

- single-run sd **2.5134 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.9667 pp** before the gap is outside noise; 9.9582 pp for 80% power
- 27 of 89 tasks flipped; mean flip rate 0.127 (max possible at n=10: 0.5556)
- re-run (plugin) sd 2.5134 pp, (posterior) 3.1697 pp; bootstrap precision of this estimate 0.7945 pp
- leave-one-round-out keeps MDD in 6.8433–7.0756 pp

## Adjudicability

0 of 904 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 904}.

## Drift screen

series (median completion tokens per round, {'run_total': 904}): [7208.0, 8007.0, 6384.0, 7346.0, 7137.0, 7258.0, 7922.0, 7068.0, 7575.0, 6633.5, 6389.5, 7004.0]
strongest single step: after round 9 (7322.778 → 6675.667, -8.84%, variance explained 0.3117). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| cancel-async-tasks | 6/12 | 0.5 | 0.2538–0.7462 | 0.5455 |
| custom-memory-heap-crash | 6/12 | 0.5 | 0.2538–0.7462 | 0.5455 |
| kv-store-grpc | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| largest-eigenval | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| openssl-selfsigned-cert | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| password-recovery | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| pypi-server | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| qemu-startup | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| sqlite-with-gcov | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| configure-git-webserver | 8/12 | 0.6667 | 0.3906–0.8619 | 0.4848 |
| build-cython-ext | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
| build-pov-ray | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
| cobol-modernization | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
| compile-compcert | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
| extract-elf | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
