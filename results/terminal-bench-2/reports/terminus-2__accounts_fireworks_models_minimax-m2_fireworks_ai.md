# Noise floor — terminal-bench 2.0 terminus-2__accounts_fireworks_models_minimax-m2_fireworks_ai

902 manifests, 89 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]; outcomes {'completed': 902}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 31 | 34.8315 |
| 2 | 89 | 24 | 26.9663 |
| 3 | 89 | 27 | 30.3371 |
| 4 | 89 | 27 | 30.3371 |
| 5 | 89 | 26 | 29.2135 |
| 6 | 89 | 27 | 30.3371 |
| 7 | 89 | 26 | 29.2135 |
| 8 | 89 | 26 | 29.2135 |
| 9 | 89 | 26 | 29.2135 |
| 10 | 89 | 28 | 31.4607 |
| 11 (partial) | 6 | 4 | 66.6667 |
| 12 (partial) | 6 | 4 | 66.6667 |

Complete rounds: mean 30.1124 %, sd 2.0377 pp, observed range 7.8652 pp.

## Headline

- single-run sd **2.8369 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.8633 pp** before the gap is outside noise; 11.2399 pp for 80% power
- 31 of 89 tasks flipped; mean flip rate 0.1567 (max possible at n=10: 0.5556)
- re-run (plugin) sd 2.8369 pp, (posterior) 3.3791 pp; bootstrap precision of this estimate 0.886 pp
- leave-one-round-out keeps MDD in 7.7101–7.9775 pp

## Adjudicability

0 of 902 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 902}.

## Drift screen

series (median completion tokens per round, {'run_total': 898}): [9188.0, 9472.5, 10205.5, 9700.0, 8971.0, 8623.0, 10034.0, 9188.0, 10240.0, 8845.5, 5633.0, 9557.0]
strongest single step: after round 10 (9446.75 → 7595.0, -19.6%, variance explained 0.3479). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| cancel-async-tasks | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| compile-compcert | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| custom-memory-heap-crash | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| distribution-search | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| git-multibranch | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| headless-terminal | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| mailman | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| merge-diff-arc-agi-task | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| nginx-request-logging | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| portfolio-optimization | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| pytorch-model-cli | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| pytorch-model-recovery | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| regex-log | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| reshard-c4-data | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| vulnerable-secret | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
