# Noise floor — terminal-bench 2.0 Factory_Droid__claude-opus-4-5-20251101_anthropic

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 56 | 62.9213 |
| 2 | 89 | 58 | 65.1685 |
| 3 | 89 | 55 | 61.7978 |
| 4 | 89 | 56 | 62.9213 |
| 5 | 89 | 56 | 62.9213 |

Complete rounds: mean 63.146 %, sd 1.2308 pp, observed range 3.3707 pp.

## Headline

- single-run sd **2.744 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.6058 pp** before the gap is outside noise; 10.8718 pp for 80% power
- 30 of 89 tasks flipped; mean flip rate 0.1685 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.744 pp, (posterior) 3.779 pp; bootstrap precision of this estimate 1.2174 pp
- leave-one-round-out keeps MDD in 7.154–7.572 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| dna-assembly | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| install-windows-3.11 | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mailman | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| path-tracing | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| path-tracing-reverse | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| polyglot-c-py | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-alpine-ssh | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| rstan-to-pystan | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| schemelike-metacircular-eval | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sparql-university | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| torch-pipeline-parallelism | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| torch-tensor-parallelism | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| winning-avg-corewars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| write-compressor | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
