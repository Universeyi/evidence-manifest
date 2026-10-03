# Noise floor — terminal-bench 2.0 terminus-2__grok-code-fast-1_xai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 14 | 15.7303 |
| 2 | 89 | 10 | 11.236 |
| 3 | 89 | 13 | 14.6067 |
| 4 | 89 | 12 | 13.4831 |
| 5 | 89 | 14 | 15.7303 |

Complete rounds: mean 14.1573 %, sd 1.8801 pp, observed range 4.4943 pp.

## Headline

- single-run sd **2.587 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.1707 pp** before the gap is outside noise; 10.2498 pp for 80% power
- 27 of 89 tasks flipped; mean flip rate 0.1506 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.587 pp, (posterior) 3.6328 pp; bootstrap precision of this estimate 1.1587 pp
- leave-one-round-out keeps MDD in 6.8028–7.1665 pp

## Adjudicability

0 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 445}.

## Drift screen

series (median completion tokens per round, {'run_total': 444}): [2353.0, 2202.0, 2226.0, 2264.0, 2059.0]
strongest single step: after round 3 (2260.333 → 2161.5, -4.37%, variance explained 0.2554). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| cobol-modernization | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| constraints-scheduling | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-code-vulnerability | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-git | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| git-multibranch | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| hf-model-inference | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| merge-diff-arc-agi-task | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| multi-source-data-merger | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| nginx-request-logging | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| prove-plus-comm | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pypi-server | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| bn-fit-modify | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| build-pmars | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
