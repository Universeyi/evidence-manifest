# Noise floor — terminal-bench 2.0 claude-code__claude-opus-4-6_anthropic

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 51 | 57.3034 |
| 2 | 89 | 50 | 56.1798 |
| 3 | 89 | 52 | 58.427 |
| 4 | 89 | 50 | 56.1798 |
| 5 | 89 | 55 | 61.7978 |

Complete rounds: mean 57.9776 %, sd 2.3299 pp, observed range 5.618 pp.

## Headline

- single-run sd **2.9605 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.2059 pp** before the gap is outside noise; 11.7296 pp for 80% power
- 35 of 89 tasks flipped; mean flip rate 0.1955 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.9605 pp, (posterior) 3.8599 pp; bootstrap precision of this estimate 1.3252 pp
- leave-one-round-out keeps MDD in 7.6765–8.11 pp

## Adjudicability

10 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 435, 'none': 10}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| cancel-async-tasks | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| count-dataset-tokens | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| financial-document-processor | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| headless-terminal | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| make-mips-interpreter | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| path-tracing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| portfolio-optimization | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| protein-assembly | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| raman-fitting | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| regex-chess | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| schemelike-metacircular-eval | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| torch-pipeline-parallelism | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| tune-mjcf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
