# Noise floor — terminal-bench 2.0 claude-code__claude-haiku-4-5-20251001_anthropic

438 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 438}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 28 | 31.4607 |
| 2 | 89 | 25 | 28.0899 |
| 3 | 89 | 28 | 31.4607 |
| 4 | 89 | 22 | 24.7191 |
| 5 (partial) | 82 | 18 | 21.9512 |

Complete rounds: mean 28.9326 %, sd 3.2273 pp, observed range 6.7416 pp.

## Headline

- single-run sd **2.7746 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.6907 pp** before the gap is outside noise; 10.9931 pp for 80% power
- 31 of 89 tasks flipped; mean flip rate 0.1738 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.7746 pp, (posterior) 3.7834 pp; bootstrap precision of this estimate 1.2514 pp
- leave-one-round-out keeps MDD in 7.2147–7.5088 pp

## Adjudicability

35 of 438 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 403, 'none': 35}.

## Drift screen

series (median completion tokens per round, {'run_total': 403}): [951.0, 829.0, 879.0, 779.0, 579.0]
strongest single step: after round 3 (886.333 → 679.0, -23.39%, variance explained 0.6521). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-pov-ray | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| cancel-async-tasks | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| compile-compcert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| constraints-scheduling | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| large-scale-text-editing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| largest-eigenval | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mailman | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mcmc-sampling-stan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| openssl-selfsigned-cert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-cli | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-startup | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| tune-mjcf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| bn-fit-modify | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
