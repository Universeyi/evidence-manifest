# Noise floor — terminal-bench 2.0 ruley__gemini-3-pro-preview_Google

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 56 | 62.9213 |
| 2 | 89 | 56 | 62.9213 |
| 3 | 89 | 54 | 60.6742 |
| 4 | 89 | 56 | 62.9213 |
| 5 | 89 | 55 | 61.7978 |

Complete rounds: mean 62.2472 %, sd 1.0049 pp, observed range 2.2471 pp.

## Headline

- single-run sd **2.6699 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.4004 pp** before the gap is outside noise; 10.5783 pp for 80% power
- 27 of 89 tasks flipped; mean flip rate 0.1573 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.6699 pp, (posterior) 3.6544 pp; bootstrap precision of this estimate 1.1914 pp
- leave-one-round-out keeps MDD in 6.8292–7.2871 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-pmars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| chess-best-move | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| code-from-image | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| count-dataset-tokens | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| crack-7z-hash | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| financial-document-processor | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| large-scale-text-editing | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| openssl-selfsigned-cert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| password-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| prove-plus-comm | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-alpine-ssh | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-startup | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| torch-pipeline-parallelism | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| winning-avg-corewars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
