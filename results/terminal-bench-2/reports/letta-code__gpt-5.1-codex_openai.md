# Noise floor — terminal-bench 2.0 letta-code__gpt-5.1-codex_openai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 48 | 53.9326 |
| 2 | 89 | 48 | 53.9326 |
| 3 | 89 | 48 | 53.9326 |
| 4 | 89 | 48 | 53.9326 |
| 5 | 89 | 46 | 51.6854 |

Complete rounds: mean 53.4832 %, sd 1.005 pp, observed range 2.2472 pp.

## Headline

- single-run sd **2.877 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.9745 pp** before the gap is outside noise; 11.3988 pp for 80% power
- 32 of 89 tasks flipped; mean flip rate 0.1865 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.877 pp, (posterior) 3.7183 pp; bootstrap precision of this estimate 1.3063 pp
- leave-one-round-out keeps MDD in 7.3927–7.9498 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-cython-ext | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| circuit-fibsqrt | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| code-from-image | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| configure-git-webserver | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| count-dataset-tokens | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| custom-memory-heap-crash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-differential-cryptanalysis | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mailman | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mcmc-sampling-stan | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mteb-leaderboard | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| overfull-hbox | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| path-tracing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
