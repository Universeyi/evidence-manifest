# Noise floor — terminal-bench 2.0 codex__gpt-5_openai

439 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 439}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 42 | 47.191 |
| 2 | 89 | 46 | 51.6854 |
| 3 | 89 | 43 | 48.3146 |
| 4 | 89 | 45 | 50.5618 |
| 5 (partial) | 83 | 41 | 49.3976 |

Complete rounds: mean 49.4382 %, sd 2.0514 pp, observed range 4.4944 pp.

## Headline

- single-run sd **2.8773 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.9753 pp** before the gap is outside noise; 11.4 pp for 80% power
- 33 of 89 tasks flipped; mean flip rate 0.1884 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.8773 pp, (posterior) 3.7888 pp; bootstrap precision of this estimate 1.3079 pp
- leave-one-round-out keeps MDD in 7.4587–7.941 pp

## Adjudicability

30 of 439 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 409, 'none': 30}.

## Drift screen

series (median completion tokens per round, {'run_total': 408}): [6276.5, 6866.0, 6400.0, 7529.0, 5803.5]
strongest single step: after round 3 (6514.167 → 6666.25, 2.33%, variance explained 0.0162). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| cancel-async-tasks | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| compile-compcert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| configure-git-webserver | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| count-dataset-tokens | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| db-wal-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-elf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| kv-store-grpc | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| llm-inference-batching-scheduler | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| log-summary-date-ranges | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mcmc-sampling-stan | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| overfull-hbox | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| query-optimize | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sanitize-git-repo | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
