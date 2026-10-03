# Noise floor — terminal-bench 2.0 Factory_Droid__gemini-3-pro-preview_google

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 57 | 64.0449 |
| 2 | 89 | 53 | 59.5506 |
| 3 | 89 | 53 | 59.5506 |
| 4 | 89 | 56 | 62.9213 |
| 5 | 89 | 53 | 59.5506 |

Complete rounds: mean 61.1236 %, sd 2.1902 pp, observed range 4.4943 pp.

## Headline

- single-run sd **2.8356 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.8597 pp** before the gap is outside noise; 11.2348 pp for 80% power
- 33 of 89 tasks flipped; mean flip rate 0.1798 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.8356 pp, (posterior) 3.7472 pp; bootstrap precision of this estimate 1.2636 pp
- leave-one-round-out keeps MDD in 7.3824–7.7924 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| break-filter-js-from-html | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pmars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pov-ray | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| code-from-image | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| dna-assembly | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| feal-linear-cryptanalysis | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| large-scale-text-editing | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-alpine-ssh | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| schemelike-metacircular-eval | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| torch-pipeline-parallelism | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| winning-avg-corewars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| write-compressor | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| bn-fit-modify | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
