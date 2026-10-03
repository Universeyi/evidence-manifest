# Noise floor — terminal-bench 2.0 codex__gpt-5.2_openai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 53 | 59.5506 |
| 2 | 89 | 60 | 67.4157 |
| 3 | 89 | 54 | 60.6742 |
| 4 | 89 | 52 | 58.427 |
| 5 | 89 | 61 | 68.5393 |

Complete rounds: mean 62.9214 %, sd 4.7003 pp, observed range 10.1123 pp.

## Headline

- single-run sd **3.0693 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.5075 pp** before the gap is outside noise; 12.1607 pp for 80% power
- 37 of 89 tasks flipped; mean flip rate 0.209 (max possible at n=5: 0.6)
- re-run (plugin) sd 3.0693 pp, (posterior) 3.9021 pp; bootstrap precision of this estimate 1.3681 pp
- leave-one-round-out keeps MDD in 8.0155–8.3492 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-cython-ext | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| chess-best-move | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| circuit-fibsqrt | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| configure-git-webserver | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| gcode-to-text | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| kv-store-grpc | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| large-scale-text-editing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| largest-eigenval | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mcmc-sampling-stan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| model-extraction-relu-logits | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mteb-leaderboard | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mteb-retrieve | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| path-tracing-reverse | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pypi-server | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-cli | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
