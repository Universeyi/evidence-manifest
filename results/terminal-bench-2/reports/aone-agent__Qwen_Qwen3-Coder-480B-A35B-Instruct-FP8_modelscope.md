# Noise floor — terminal-bench 2.0 aone-agent__Qwen_Qwen3-Coder-480B-A35B-Instruct-FP8_modelscope

442 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 442}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 23 | 25.8427 |
| 2 | 89 | 21 | 23.5955 |
| 3 (partial) | 88 | 25 | 28.4091 |
| 4 (partial) | 88 | 25 | 28.4091 |
| 5 (partial) | 88 | 27 | 30.6818 |

Complete rounds: mean 24.7191 %, sd 1.589 pp, observed range 2.2472 pp.

## Headline

- single-run sd **2.6039 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.2175 pp** before the gap is outside noise; 10.3168 pp for 80% power
- 28 of 89 tasks flipped; mean flip rate 0.1528 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.6039 pp, (posterior) 3.6854 pp; bootstrap precision of this estimate 1.1725 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 6.5401–7.2203 pp

## Adjudicability

442 of 442 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 442}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| cobol-modernization | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| count-dataset-tokens | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| headless-terminal | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| model-extraction-relu-logits | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| nginx-request-logging | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-startup | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| regex-log | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| rstan-to-pystan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sanitize-git-repo | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| train-fasttext | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| cancel-async-tasks | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| constraints-scheduling | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| custom-memory-heap-crash | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
