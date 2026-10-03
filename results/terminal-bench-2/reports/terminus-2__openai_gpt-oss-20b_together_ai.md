# Noise floor — terminal-bench 2.0 terminus-2__openai_gpt-oss-20b_together_ai

932 manifests, 89 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]; outcomes {'completed': 932}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 2 | 2.2472 |
| 2 | 89 | 2 | 2.2472 |
| 3 | 89 | 4 | 4.4944 |
| 4 | 89 | 4 | 4.4944 |
| 5 | 89 | 2 | 2.2472 |
| 6 | 89 | 3 | 3.3708 |
| 7 | 89 | 3 | 3.3708 |
| 8 | 89 | 1 | 1.1236 |
| 9 | 89 | 3 | 3.3708 |
| 10 | 89 | 2 | 2.2472 |
| 11 (partial) | 21 | 1 | 4.7619 |
| 12 (partial) | 21 | 1 | 4.7619 |

Complete rounds: mean 2.9214 %, sd 1.0855 pp, observed range 3.3708 pp.

## Headline

- single-run sd **1.5694 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **4.3501 pp** before the gap is outside noise; 6.218 pp for 80% power
- 11 of 89 tasks flipped; mean flip rate 0.0488 (max possible at n=10: 0.5556)
- re-run (plugin) sd 1.5694 pp, (posterior) 2.6018 pp; bootstrap precision of this estimate 0.4882 pp
- leave-one-round-out keeps MDD in 4.1899–4.4022 pp

## Adjudicability

0 of 932 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 932}.

## Drift screen

series (median completion tokens per round, {'run_total': 932}): [3484.0, 4563.0, 4202.0, 4417.0, 4062.0, 4316.0, 4436.0, 4017.0, 4405.0, 3904.0, 3871.0, 3769.0]
strongest single step: after round 9 (4211.333 → 3848.0, -8.63%, variance explained 0.2558). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| hf-model-inference | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| modernize-scientific-stack | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| nginx-request-logging | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| git-leak-recovery | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
| multi-source-data-merger | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
| openssl-selfsigned-cert | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
| prove-plus-comm | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
| pypi-server | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
| qemu-startup | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
| cancel-async-tasks | 2/12 | 0.1667 | 0.047–0.448 | 0.303 |
| configure-git-webserver | 2/12 | 0.1667 | 0.047–0.448 | 0.303 |
