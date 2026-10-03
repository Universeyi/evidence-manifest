# Noise floor — terminal-bench 2.0 openhands__claude-sonnet-4-5-20250929_anthropic

443 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 443}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 35 | 39.3258 |
| 2 | 89 | 37 | 41.573 |
| 3 | 89 | 46 | 51.6854 |
| 4 | 89 | 36 | 40.4494 |
| 5 (partial) | 87 | 34 | 39.0805 |

Complete rounds: mean 43.2584 %, sd 5.6924 pp, observed range 12.3596 pp.

## Headline

- single-run sd **2.7931 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.7419 pp** before the gap is outside noise; 11.0664 pp for 80% power
- 32 of 89 tasks flipped; mean flip rate 0.176 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.7931 pp, (posterior) 3.7185 pp; bootstrap precision of this estimate 1.2633 pp
- leave-one-round-out keeps MDD in 7.1316–7.727 pp

## Adjudicability

5 of 443 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 438, 'none': 5}.

## Drift screen

series (median completion tokens per round, {'run_total': 438}): [10525.0, 11412.0, 11307.0, 11387.0, 12810.0]
strongest single step: after round 3 (11081.333 → 12098.5, 9.18%, variance explained 0.4558). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| mailman | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| adaptive-rejection-sampler | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pmars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| distribution-search | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-elf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| hf-model-inference | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| overfull-hbox | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-cli | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-alpine-ssh | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| rstan-to-pystan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sparql-university | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| tune-mjcf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| bn-fit-modify | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
