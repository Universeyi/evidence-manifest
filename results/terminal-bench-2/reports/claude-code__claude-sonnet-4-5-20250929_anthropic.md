# Noise floor — terminal-bench 2.0 claude-code__claude-sonnet-4-5-20250929_anthropic

437 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 437}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 40 | 44.9438 |
| 2 | 89 | 36 | 40.4494 |
| 3 | 89 | 33 | 37.0787 |
| 4 | 89 | 34 | 38.2022 |
| 5 (partial) | 81 | 30 | 37.037 |

Complete rounds: mean 40.1685 %, sd 3.4783 pp, observed range 7.8651 pp.

## Headline

- single-run sd **2.9096 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.0649 pp** before the gap is outside noise; 11.528 pp for 80% power
- 35 of 89 tasks flipped; mean flip rate 0.1899 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.9096 pp, (posterior) 3.797 pp; bootstrap precision of this estimate 1.3312 pp
- leave-one-round-out keeps MDD in 7.4728–8.082 pp

## Adjudicability

33 of 437 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 404, 'none': 33}.

## Drift screen

series (median completion tokens per round, {'run_total': 403}): [633.0, 587.0, 541.0, 525.0, 540.0]
strongest single step: after round 2 (610.0 → 535.333, -12.24%, variance explained 0.8459). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| distribution-search | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| hf-model-inference | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| large-scale-text-editing | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| largest-eigenval | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| llm-inference-batching-scheduler | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mcmc-sampling-stan | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-startup | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| schemelike-metacircular-eval | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| adaptive-rejection-sampler | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| bn-fit-modify | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| break-filter-js-from-html | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
