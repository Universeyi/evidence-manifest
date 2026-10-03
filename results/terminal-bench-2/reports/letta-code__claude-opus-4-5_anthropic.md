# Noise floor — terminal-bench 2.0 letta-code__claude-opus-4-5_anthropic

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 54 | 60.6742 |
| 2 | 89 | 53 | 59.5506 |
| 3 | 89 | 52 | 58.427 |
| 4 | 89 | 52 | 58.427 |
| 5 | 89 | 52 | 58.427 |

Complete rounds: mean 59.1012 %, sd 1.005 pp, observed range 2.2472 pp.

## Headline

- single-run sd **2.4649 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.8322 pp** before the gap is outside noise; 9.766 pp for 80% power
- 24 of 89 tasks flipped; mean flip rate 0.1348 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.4649 pp, (posterior) 3.6031 pp; bootstrap precision of this estimate 1.0844 pp
- leave-one-round-out keeps MDD in 6.3078–6.9062 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pmars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| count-dataset-tokens | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| dna-assembly | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-moves-from-video | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| openssl-selfsigned-cert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| path-tracing | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-alpine-ssh | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| query-optimize | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| torch-tensor-parallelism | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| tune-mjcf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| write-compressor | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| bn-fit-modify | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| chess-best-move | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| circuit-fibsqrt | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
