# Noise floor — terminal-bench 2.0 terminus-2__claude-haiku-4-5-20251001_anthropic

439 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 439}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 25 | 28.0899 |
| 2 | 89 | 27 | 30.3371 |
| 3 | 89 | 27 | 30.3371 |
| 4 | 89 | 19 | 21.3483 |
| 5 (partial) | 83 | 27 | 32.5301 |

Complete rounds: mean 27.5281 %, sd 4.2539 pp, observed range 8.9888 pp.

## Headline

- single-run sd **2.8956 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.026 pp** before the gap is outside noise; 11.4725 pp for 80% power
- 32 of 89 tasks flipped; mean flip rate 0.1888 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.8956 pp, (posterior) 3.8088 pp; bootstrap precision of this estimate 1.2972 pp
- leave-one-round-out keeps MDD in 7.4659–7.9839 pp

## Adjudicability

0 of 439 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 439}.

## Drift screen

series (median completion tokens per round, {'run_total': 438}): [9959.0, 9928.0, 8138.5, 9616.0, 9078.0]
strongest single step: after round 2 (9943.5 → 8944.167, -10.05%, variance explained 0.5172). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| cancel-async-tasks | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| cobol-modernization | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| code-from-image | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| compile-compcert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| crack-7z-hash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| custom-memory-heap-crash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| distribution-search | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-code-vulnerability | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| git-multibranch | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| model-extraction-relu-logits | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| nginx-request-logging | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| openssl-selfsigned-cert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-cli | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
