# Noise floor — terminal-bench 2.0 simple_codex__gpt-5.3-codex_openai

443 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 443}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 67 | 75.2809 |
| 2 | 89 | 65 | 73.0337 |
| 3 | 89 | 66 | 74.1573 |
| 4 | 89 | 67 | 75.2809 |
| 5 (partial) | 87 | 67 | 77.0115 |

Complete rounds: mean 74.4382 %, sd 1.0758 pp, observed range 2.2472 pp.

## Headline

- single-run sd **2.4427 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.7707 pp** before the gap is outside noise; 9.6781 pp for 80% power
- 23 of 89 tasks flipped; mean flip rate 0.1326 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.4427 pp, (posterior) 3.5482 pp; bootstrap precision of this estimate 1.0945 pp
- leave-one-round-out keeps MDD in 6.2831–6.7516 pp

## Adjudicability

443 of 443 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 443}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| break-filter-js-from-html | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-differential-cryptanalysis | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| gcode-to-text | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| model-extraction-relu-logits | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mteb-leaderboard | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mteb-retrieve | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| polyglot-rust-c | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-startup | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| torch-tensor-parallelism | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| tune-mjcf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| video-processing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| adaptive-rejection-sampler | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| cancel-async-tasks | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
