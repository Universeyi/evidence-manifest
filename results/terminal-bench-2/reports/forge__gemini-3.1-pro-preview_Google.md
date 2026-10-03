# Noise floor — terminal-bench 2.0 forge__gemini-3.1-pro-preview_Google

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 71 | 79.7753 |
| 2 | 89 | 65 | 73.0337 |
| 3 | 89 | 72 | 80.8989 |
| 4 | 89 | 70 | 78.6517 |
| 5 | 89 | 71 | 79.7753 |

Complete rounds: mean 78.427 %, sd 3.1179 pp, observed range 7.8652 pp.

## Headline

- single-run sd **1.8581 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **5.1503 pp** before the gap is outside noise; 7.3619 pp for 80% power
- 14 of 89 tasks flipped; mean flip rate 0.0764 (max possible at n=5: 0.6)
- re-run (plugin) sd 1.8581 pp, (posterior) 3.3171 pp; bootstrap precision of this estimate 0.8293 pp
- leave-one-round-out keeps MDD in 4.574–5.2257 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| dna-assembly | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| dna-insert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-linear-cryptanalysis | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mailman | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| portfolio-optimization | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| regex-chess | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| break-filter-js-from-html | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| build-cython-ext | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| financial-document-processor | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| git-multibranch | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| gpt2-codegolf | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| largest-eigenval | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| rstan-to-pystan | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| sam-cell-seg | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
