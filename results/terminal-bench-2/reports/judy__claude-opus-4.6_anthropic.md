# Noise floor — terminal-bench 2.0 judy__claude-opus-4.6_anthropic

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 65 | 73.0337 |
| 2 | 89 | 67 | 75.2809 |
| 3 | 89 | 62 | 69.6629 |
| 4 | 89 | 61 | 68.5393 |
| 5 | 89 | 65 | 73.0337 |

Complete rounds: mean 71.9101 %, sd 2.7522 pp, observed range 6.7416 pp.

## Headline

- single-run sd **2.7244 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.5515 pp** before the gap is outside noise; 10.7942 pp for 80% power
- 32 of 89 tasks flipped; mean flip rate 0.1663 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.7244 pp, (posterior) 3.7459 pp; bootstrap precision of this estimate 1.2068 pp
- leave-one-round-out keeps MDD in 7.0883–7.516 pp

## Adjudicability

288 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 157, 'none': 288}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| dna-insert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| financial-document-processor | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| gcode-to-text | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| path-tracing | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| schemelike-metacircular-eval | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| torch-tensor-parallelism | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| tune-mjcf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| write-compressor | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| adaptive-rejection-sampler | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| build-pmars | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| build-pov-ray | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| cancel-async-tasks | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| chess-best-move | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
