# Noise floor — terminal-bench 2.0 openhands__Qwen_Qwen3-Coder-480B-A35B-Instruct-FP8_together_ai

878 manifests, 89 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; outcomes {'completed': 878}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 24 | 26.9663 |
| 2 | 89 | 25 | 28.0899 |
| 3 | 89 | 22 | 24.7191 |
| 4 | 89 | 23 | 25.8427 |
| 5 | 89 | 19 | 21.3483 |
| 6 | 89 | 21 | 23.5955 |
| 7 (partial) | 88 | 22 | 25.0 |
| 8 (partial) | 88 | 25 | 28.4091 |
| 9 (partial) | 88 | 24 | 27.2727 |
| 10 (partial) | 80 | 21 | 26.25 |

Complete rounds: mean 25.0936 %, sd 2.4273 pp, observed range 6.7416 pp.

## Headline

- single-run sd **2.6325 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.2968 pp** before the gap is outside noise; 10.4301 pp for 80% power
- 28 of 89 tasks flipped; mean flip rate 0.1391 (max possible at n=10: 0.5556)
- re-run (plugin) sd 2.6325 pp, (posterior) 3.2751 pp; bootstrap precision of this estimate 0.8358 pp
- leave-one-round-out keeps MDD in 7.1962–7.3835 pp

## Adjudicability

8 of 878 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 870, 'none': 8}.

## Drift screen

series (median completion tokens per round, {'run_total': 868}): [7680.0, 7437.0, 9181.0, 8299.5, 8267.0, 8349.0, 7200.0, 6999.0, 8865.0, 8272.0]
strongest single step: after round 8 (7926.562 → 8568.5, 8.1%, variance explained 0.1455). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| configure-git-webserver | 4/9 | 0.4444 | 0.1888–0.7333 | 0.5556 |
| custom-memory-heap-crash | 4/9 | 0.4444 | 0.1888–0.7333 | 0.5556 |
| build-pov-ray | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| code-from-image | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| fix-code-vulnerability | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| git-multibranch | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| headless-terminal | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| hf-model-inference | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| merge-diff-arc-agi-task | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| portfolio-optimization | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| qemu-startup | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| query-optimize | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| schemelike-metacircular-eval | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| mteb-retrieve | 2/9 | 0.2222 | 0.0632–0.5474 | 0.3889 |
| pytorch-model-cli | 2/9 | 0.2222 | 0.0632–0.5474 | 0.3889 |
