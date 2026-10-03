# Noise floor — terminal-bench 2.0 claude-code__claude-opus-4-1-20250805_anthropic

437 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 437}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 31 | 34.8315 |
| 2 | 89 | 34 | 38.2022 |
| 3 | 89 | 32 | 35.9551 |
| 4 | 89 | 30 | 33.7079 |
| 5 (partial) | 81 | 25 | 30.8642 |

Complete rounds: mean 35.6742 %, sd 1.9189 pp, observed range 4.4943 pp.

## Headline

- single-run sd **2.8908 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.0127 pp** before the gap is outside noise; 11.4535 pp for 80% power
- 32 of 89 tasks flipped; mean flip rate 0.1873 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.8908 pp, (posterior) 3.8314 pp; bootstrap precision of this estimate 1.3194 pp
- leave-one-round-out keeps MDD in 7.3065–8.0502 pp

## Adjudicability

33 of 437 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 404, 'none': 33}.

## Drift screen

series (median completion tokens per round, {'run_total': 405}): [653.0, 654.5, 737.0, 658.5, 717.5]
strongest single step: after round 2 (653.75 → 704.333, 7.74%, variance explained 0.4788). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| caffe-cifar-10 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| cancel-async-tasks | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| count-dataset-tokens | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| crack-7z-hash | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| distribution-search | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-elf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| hf-model-inference | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| large-scale-text-editing | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| nginx-request-logging | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| openssl-selfsigned-cert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| password-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| rstan-to-pystan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
