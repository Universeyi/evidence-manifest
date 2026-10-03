# Noise floor — terminal-bench 2.0 terminus-2__minimax-m2.1_openai

438 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 438}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 29 | 32.5843 |
| 2 | 89 | 26 | 29.2135 |
| 3 (partial) | 88 | 26 | 29.5455 |
| 4 (partial) | 86 | 25 | 29.0698 |
| 5 (partial) | 86 | 24 | 27.907 |

Complete rounds: mean 30.8989 %, sd 2.3835 pp, observed range 3.3708 pp.

## Headline

- single-run sd **2.9793 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.258 pp** before the gap is outside noise; 11.8041 pp for 80% power
- 35 of 89 tasks flipped; mean flip rate 0.1955 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.9793 pp, (posterior) 3.825 pp; bootstrap precision of this estimate 1.3375 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 7.7985–8.158 pp

## Adjudicability

0 of 438 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 438}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| code-from-image | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| compile-compcert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| constraints-scheduling | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| count-dataset-tokens | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| distribution-search | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-elf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| fix-git | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| log-summary-date-ranges | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mailman | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| nginx-request-logging | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| openssl-selfsigned-cert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-startup | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| regex-log | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| reshard-c4-data | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
