# Noise floor — terminal-bench 2.0 terminus-2__moonshotai_Kimi-K2-Instruct-0905_together_ai

923 manifests, 89 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]; outcomes {'completed': 923}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 21 | 23.5955 |
| 2 | 89 | 24 | 26.9663 |
| 3 | 89 | 30 | 33.7079 |
| 4 | 89 | 22 | 24.7191 |
| 5 | 89 | 26 | 29.2135 |
| 6 | 89 | 29 | 32.5843 |
| 7 | 89 | 21 | 23.5955 |
| 8 | 89 | 24 | 26.9663 |
| 9 | 89 | 27 | 30.3371 |
| 10 (partial) | 88 | 22 | 25.0 |
| 11 (partial) | 17 | 8 | 47.0588 |
| 12 (partial) | 17 | 4 | 23.5294 |

Complete rounds: mean 27.9651 %, sd 3.7453 pp, observed range 10.1124 pp.

## Headline

- single-run sd **2.6383 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.3129 pp** before the gap is outside noise; 10.453 pp for 80% power
- 27 of 89 tasks flipped; mean flip rate 0.138 (max possible at n=10: 0.5556)
- re-run (plugin) sd 2.6383 pp, (posterior) 3.3022 pp; bootstrap precision of this estimate 0.8133 pp
- leave-one-round-out keeps MDD in 7.2214–7.3561 pp

## Adjudicability

0 of 923 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 923}.

## Drift screen

series (median completion tokens per round, {'run_total': 923}): [7025.0, 7877.0, 6975.0, 6968.0, 7178.0, 7578.0, 7641.0, 8037.0, 6761.0, 7146.0, 8256.0, 5481.0]
strongest single step: after round 8 (7409.875 → 6911.0, -6.73%, variance explained 0.113). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-pmars | 6/12 | 0.5 | 0.2538–0.7462 | 0.5455 |
| build-pov-ray | 6/12 | 0.5 | 0.2538–0.7462 | 0.5455 |
| code-from-image | 6/12 | 0.5 | 0.2538–0.7462 | 0.5455 |
| crack-7z-hash | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| distribution-search | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| extract-elf | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| mailman | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| nginx-request-logging | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| pypi-server | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| qemu-startup | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| query-optimize | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| sqlite-with-gcov | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| vulnerable-secret | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| cancel-async-tasks | 8/12 | 0.6667 | 0.3906–0.8619 | 0.4848 |
| cobol-modernization | 8/12 | 0.6667 | 0.3906–0.8619 | 0.4848 |
