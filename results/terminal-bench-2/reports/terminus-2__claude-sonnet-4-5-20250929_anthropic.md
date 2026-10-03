# Noise floor — terminal-bench 2.0 terminus-2__claude-sonnet-4-5-20250929_anthropic

440 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 440}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 37 | 41.573 |
| 2 | 89 | 35 | 39.3258 |
| 3 | 89 | 41 | 46.0674 |
| 4 | 89 | 38 | 42.6966 |
| 5 (partial) | 84 | 39 | 46.4286 |

Complete rounds: mean 42.4157 %, sd 2.809 pp, observed range 6.7416 pp.

## Headline

- single-run sd **2.8254 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.8315 pp** before the gap is outside noise; 11.1943 pp for 80% power
- 33 of 89 tasks flipped; mean flip rate 0.1783 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.8254 pp, (posterior) 3.7504 pp; bootstrap precision of this estimate 1.2627 pp
- leave-one-round-out keeps MDD in 7.4656–7.6959 pp

## Adjudicability

0 of 440 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 440}.

## Drift screen

series (median completion tokens per round, {'run_total': 439}): [8201.0, 7009.0, 7459.0, 7167.0, 7328.0]
strongest single step: after round 3 (7556.333 → 7247.5, -4.09%, variance explained 0.1343). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| password-recovery | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| adaptive-rejection-sampler | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| cancel-async-tasks | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| circuit-fibsqrt | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| code-from-image | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| count-dataset-tokens | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mailman | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-cli | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-startup | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sqlite-with-gcov | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| bn-fit-modify | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| break-filter-js-from-html | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
