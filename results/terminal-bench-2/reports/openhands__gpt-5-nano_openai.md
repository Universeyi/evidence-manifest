# Noise floor — terminal-bench 2.0 openhands__gpt-5-nano_openai

444 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 444}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 11 | 12.3596 |
| 2 | 89 | 11 | 12.3596 |
| 3 | 89 | 9 | 10.1124 |
| 4 | 89 | 3 | 3.3708 |
| 5 (partial) | 88 | 10 | 11.3636 |

Complete rounds: mean 9.5506 %, sd 4.2539 pp, observed range 8.9888 pp.

## Headline

- single-run sd **2.1551 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **5.9735 pp** before the gap is outside noise; 8.5386 pp for 80% power
- 18 of 89 tasks flipped; mean flip rate 0.1034 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.1551 pp, (posterior) 3.4291 pp; bootstrap precision of this estimate 0.9598 pp
- leave-one-round-out keeps MDD in 5.5317–5.9688 pp

## Adjudicability

17 of 444 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 427, 'none': 17}.

## Drift screen

series (median completion tokens per round, {'run_total': 426}): [95556.5, 83208.0, 86092.0, 90216.5, 85467.5]
strongest single step: after round 2 (89382.25 → 87258.667, -2.38%, variance explained 0.057). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| bn-fit-modify | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pmars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| cobol-modernization | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| constraints-scheduling | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| git-leak-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| headless-terminal | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| log-summary-date-ranges | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| multi-source-data-merger | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| openssl-selfsigned-cert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-startup | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| cancel-async-tasks | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| distribution-search | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| extract-elf | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| merge-diff-arc-agi-task | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| portfolio-optimization | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
