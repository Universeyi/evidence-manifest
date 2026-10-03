# Noise floor — terminal-bench 2.0 mini-swe-agent__claude-haiku-4-5-20251001_anthropic

444 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 444}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 26 | 29.2135 |
| 2 | 89 | 27 | 30.3371 |
| 3 | 89 | 26 | 29.2135 |
| 4 | 89 | 27 | 30.3371 |
| 5 (partial) | 88 | 26 | 29.5455 |

Complete rounds: mean 29.7753 %, sd 0.6487 pp, observed range 1.1236 pp.

## Headline

- single-run sd **2.548 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.0626 pp** before the gap is outside noise; 10.0953 pp for 80% power
- 26 of 89 tasks flipped; mean flip rate 0.1449 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.548 pp, (posterior) 3.6319 pp; bootstrap precision of this estimate 1.1589 pp
- leave-one-round-out keeps MDD in 6.4666–7.0634 pp

## Adjudicability

16 of 444 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 428, 'none': 16}.

## Drift screen

series (median completion tokens per round, {'run_total': 428}): [8160.0, 10258.0, 9870.0, 10610.0, 8738.0]
strongest single step: after round 2 (9209.0 → 9739.333, 5.76%, variance explained 0.0782). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| break-filter-js-from-html | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| custom-memory-heap-crash | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| distribution-search | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-cli | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| query-optimize | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| regex-log | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sqlite-with-gcov | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| tune-mjcf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| winning-avg-corewars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mailman | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| adaptive-rejection-sampler | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| bn-fit-modify | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
