# Noise floor — terminal-bench 2.0 deepagent-harbor__gpt-5.2-codex_openai

433 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 433}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 59 | 66.2921 |
| 2 | 89 | 60 | 67.4157 |
| 3 (partial) | 86 | 56 | 65.1163 |
| 4 (partial) | 86 | 63 | 73.2558 |
| 5 (partial) | 83 | 55 | 66.2651 |

Complete rounds: mean 66.8539 %, sd 0.7945 pp, observed range 1.1236 pp.

## Headline

- single-run sd **2.9315 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.1256 pp** before the gap is outside noise; 11.6147 pp for 80% power
- 35 of 89 tasks flipped; mean flip rate 0.1985 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.9315 pp, (posterior) 3.8478 pp; bootstrap precision of this estimate 1.3588 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 7.5088–7.8675 pp

## Adjudicability

16 of 433 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 417, 'none': 16}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| mteb-leaderboard | 1/2 | 0.5 | 0.0945–0.9055 | 1.0 |
| make-mips-interpreter | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| adaptive-rejection-sampler | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| break-filter-js-from-html | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| chess-best-move | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| db-wal-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| financial-document-processor | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| model-extraction-relu-logits | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| overfull-hbox | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| password-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| path-tracing | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| path-tracing-reverse | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-cli | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-alpine-ssh | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
