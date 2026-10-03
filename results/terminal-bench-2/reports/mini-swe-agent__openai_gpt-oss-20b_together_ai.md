# Noise floor — terminal-bench 2.0 mini-swe-agent__openai_gpt-oss-20b_together_ai

888 manifests, 89 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; outcomes {'completed': 888}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 7 | 7.8652 |
| 2 | 89 | 2 | 2.2472 |
| 3 | 89 | 2 | 2.2472 |
| 4 | 89 | 3 | 3.3708 |
| 5 | 89 | 1 | 1.1236 |
| 6 | 89 | 2 | 2.2472 |
| 7 | 89 | 4 | 4.4944 |
| 8 | 89 | 1 | 1.1236 |
| 9 | 89 | 4 | 4.4944 |
| 10 (partial) | 87 | 4 | 4.5977 |

Complete rounds: mean 3.246 %, sd 2.1352 pp, observed range 6.7416 pp.

## Headline

- single-run sd **1.3801 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **3.8254 pp** before the gap is outside noise; 5.468 pp for 80% power
- 8 of 89 tasks flipped; mean flip rate 0.038 (max possible at n=10: 0.5556)
- re-run (plugin) sd 1.3801 pp, (posterior) 2.5346 pp; bootstrap precision of this estimate 0.4328 pp
- leave-one-round-out keeps MDD in 3.5831–3.9152 pp

## Adjudicability

2 of 888 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 886, 'none': 2}.

## Drift screen

series (median completion tokens per round, {'run_total': 884}): [5747.0, 4713.0, 4796.5, 4664.0, 4540.5, 5372.0, 4568.0, 4364.0, 4481.5, 5009.0]
strongest single step: after round 2 (5230.0 → 4724.438, -9.67%, variance explained 0.2406). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| cancel-async-tasks | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| constraints-scheduling | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| multi-source-data-merger | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| fix-git | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
| nginx-request-logging | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
| prove-plus-comm | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
| qemu-startup | 8/10 | 0.8 | 0.4902–0.9433 | 0.3556 |
| sqlite-with-gcov | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
