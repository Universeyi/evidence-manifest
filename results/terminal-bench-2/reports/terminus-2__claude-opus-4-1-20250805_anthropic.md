# Noise floor — terminal-bench 2.0 terminus-2__claude-opus-4-1-20250805_anthropic

443 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 443}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 34 | 38.2022 |
| 2 | 89 | 32 | 35.9551 |
| 3 | 89 | 37 | 41.573 |
| 4 | 89 | 34 | 38.2022 |
| 5 (partial) | 87 | 32 | 36.7816 |

Complete rounds: mean 38.4831 %, sd 2.3163 pp, observed range 5.6179 pp.

## Headline

- single-run sd **2.6576 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.3664 pp** before the gap is outside noise; 10.5295 pp for 80% power
- 29 of 89 tasks flipped; mean flip rate 0.1596 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.6576 pp, (posterior) 3.6974 pp; bootstrap precision of this estimate 1.1939 pp
- leave-one-round-out keeps MDD in 6.5922–7.5515 pp

## Adjudicability

2 of 443 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 441, 'none': 2}.

## Drift screen

series (median completion tokens per round, {'run_total': 443}): [5284.0, 5778.0, 5513.0, 5782.0, 5710.0]
strongest single step: after round 3 (5525.0 → 5746.0, 4.0%, variance explained 0.3195). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-pmars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| cancel-async-tasks | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| distribution-search | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mailman | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| overfull-hbox | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-cli | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| reshard-c4-data | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| tune-mjcf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| adaptive-rejection-sampler | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| bn-fit-modify | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
