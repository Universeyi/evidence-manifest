# Noise floor — terminal-bench 2.0 terminus-2__moonshotai_Kimi-K2-Thinking_together_ai

892 manifests, 89 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]; outcomes {'completed': 892}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 33 | 37.0787 |
| 2 | 89 | 35 | 39.3258 |
| 3 | 89 | 29 | 32.5843 |
| 4 | 89 | 29 | 32.5843 |
| 5 | 89 | 33 | 37.0787 |
| 6 | 89 | 30 | 33.7079 |
| 7 | 89 | 31 | 34.8315 |
| 8 | 89 | 32 | 35.9551 |
| 9 | 89 | 33 | 37.0787 |
| 10 | 89 | 33 | 37.0787 |
| 11 (partial) | 1 | 1 | 100.0 |
| 12 (partial) | 1 | 1 | 100.0 |

Complete rounds: mean 35.7304 %, sd 2.2347 pp, observed range 6.7415 pp.

## Headline

- single-run sd **2.8868 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.0017 pp** before the gap is outside noise; 11.4376 pp for 80% power
- 36 of 89 tasks flipped; mean flip rate 0.1638 (max possible at n=10: 0.5556)
- re-run (plugin) sd 2.8868 pp, (posterior) 3.4265 pp; bootstrap precision of this estimate 0.9129 pp
- leave-one-round-out keeps MDD in 7.8547–8.059 pp

## Adjudicability

0 of 892 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 892}.

## Drift screen

series (median completion tokens per round, {'run_total': 890}): [9748.0, 10227.0, 13008.0, 11163.5, 11805.0, 10978.0, 11481.0, 10687.0, 11297.0, 9517.0, 4279.0, 5669.0]
strongest single step: after round 10 (10991.15 → 4974.0, -54.75%, variance explained 0.8523). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| bn-fit-modify | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| build-pmars | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| cancel-async-tasks | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| count-dataset-tokens | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| fix-code-vulnerability | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| largest-eigenval | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| mailman | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| openssl-selfsigned-cert | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| pytorch-model-cli | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| reshard-c4-data | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| adaptive-rejection-sampler | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
| build-pov-ray | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
| compile-compcert | 8/10 | 0.8 | 0.4902–0.9433 | 0.3556 |
| configure-git-webserver | 8/10 | 0.8 | 0.4902–0.9433 | 0.3556 |
| custom-memory-heap-crash | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
