# Noise floor — terminal-bench 2.0 mini-swe-agent__gpt-5-nano_openai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 6 | 6.7416 |
| 2 | 89 | 9 | 10.1124 |
| 3 | 89 | 4 | 4.4944 |
| 4 | 89 | 7 | 7.8652 |
| 5 | 89 | 5 | 5.618 |

Complete rounds: mean 6.9663 %, sd 2.1613 pp, observed range 5.618 pp.

## Headline

- single-run sd **1.9534 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **5.4144 pp** before the gap is outside noise; 7.7394 pp for 80% power
- 16 of 89 tasks flipped; mean flip rate 0.0854 (max possible at n=5: 0.6)
- re-run (plugin) sd 1.9534 pp, (posterior) 3.378 pp; bootstrap precision of this estimate 0.8751 pp
- leave-one-round-out keeps MDD in 5.0136–5.6265 pp

## Adjudicability

4 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 441, 'none': 4}.

## Drift screen

series (median completion tokens per round, {'run_total': 438}): [16988.0, 18804.0, 21429.0, 19015.0, 15955.5]
strongest single step: after round 3 (19073.667 → 17485.25, -8.33%, variance explained 0.1713). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| distribution-search | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-elf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| hf-model-inference | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| modernize-scientific-stack | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-startup | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| regex-log | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| adaptive-rejection-sampler | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| bn-fit-modify | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| cancel-async-tasks | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| cobol-modernization | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| constraints-scheduling | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| fix-git | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| multi-source-data-merger | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| openssl-selfsigned-cert | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| portfolio-optimization | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
