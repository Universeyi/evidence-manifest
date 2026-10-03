# Noise floor — terminal-bench 2.0 openhands__claude-haiku-4-5-20251001_anthropic

444 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 444}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 16 | 17.9775 |
| 2 | 89 | 14 | 15.7303 |
| 3 | 89 | 9 | 10.1124 |
| 4 | 89 | 12 | 13.4831 |
| 5 (partial) | 88 | 11 | 12.5 |

Complete rounds: mean 14.3258 %, sd 3.3551 pp, observed range 7.8651 pp.

## Headline

- single-run sd **2.7859 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.722 pp** before the gap is outside noise; 11.0378 pp for 80% power
- 32 of 89 tasks flipped; mean flip rate 0.173 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.7859 pp, (posterior) 3.7359 pp; bootstrap precision of this estimate 1.2454 pp
- leave-one-round-out keeps MDD in 7.2294–7.8936 pp

## Adjudicability

26 of 444 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 418, 'none': 26}.

## Drift screen

series (median completion tokens per round, {'run_total': 418}): [18837.0, 18957.0, 20090.0, 25069.0, 21340.5]
strongest single step: after round 3 (19294.667 → 23204.75, 20.27%, variance explained 0.6988). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| cobol-modernization | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| code-from-image | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-git | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| kv-store-grpc | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| log-summary-date-ranges | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| modernize-scientific-stack | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| multi-source-data-merger | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| nginx-request-logging | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| prove-plus-comm | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-startup | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pmars | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| build-pov-ray | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
