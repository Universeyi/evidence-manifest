# Noise floor — terminal-bench 2.0 terminus-2__Qwen_Qwen3-Coder-480B-A35B-Instruct-FP8_together_ai

929 manifests, 89 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]; outcomes {'completed': 929}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 21 | 23.5955 |
| 2 | 89 | 19 | 21.3483 |
| 3 | 89 | 24 | 26.9663 |
| 4 | 89 | 22 | 24.7191 |
| 5 | 89 | 20 | 22.4719 |
| 6 | 89 | 20 | 22.4719 |
| 7 | 89 | 17 | 19.1011 |
| 8 | 89 | 23 | 25.8427 |
| 9 | 89 | 27 | 30.3371 |
| 10 (partial) | 88 | 22 | 25.0 |
| 11 (partial) | 20 | 4 | 20.0 |
| 12 (partial) | 20 | 5 | 25.0 |

Complete rounds: mean 24.0949 %, sd 3.3289 pp, observed range 11.236 pp.

## Headline

- single-run sd **2.926 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.1103 pp** before the gap is outside noise; 11.5929 pp for 80% power
- 34 of 89 tasks flipped; mean flip rate 0.1702 (max possible at n=10: 0.5556)
- re-run (plugin) sd 2.926 pp, (posterior) 3.4498 pp; bootstrap precision of this estimate 0.9077 pp
- leave-one-round-out keeps MDD in 7.9695–8.1918 pp

## Adjudicability

1 of 929 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 928, 'none': 1}.

## Drift screen

series (median completion tokens per round, {'run_total': 927}): [6789.0, 7644.0, 6758.0, 7328.0, 6541.0, 7114.0, 6737.0, 6978.0, 6085.0, 6430.0, 7043.5, 8830.5]
strongest single step: after round 10 (6840.4 → 7937.0, 16.03%, variance explained 0.3693). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| code-from-image | 6/12 | 0.5 | 0.2538–0.7462 | 0.5455 |
| distribution-search | 6/12 | 0.5 | 0.2538–0.7462 | 0.5455 |
| compile-compcert | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| custom-memory-heap-crash | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| extract-elf | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| git-multibranch | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| hf-model-inference | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| mcmc-sampling-stan | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| model-extraction-relu-logits | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| pypi-server | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| pytorch-model-recovery | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| qemu-startup | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| regex-log | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| vulnerable-secret | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| build-pov-ray | 4/12 | 0.3333 | 0.1381–0.6094 | 0.4848 |
