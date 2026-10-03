# Noise floor — terminal-bench 2.0 Junie__gemini-3-flash-preview_gemini

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 61 | 68.5393 |
| 2 | 89 | 56 | 62.9213 |
| 3 | 89 | 59 | 66.2921 |
| 4 | 89 | 59 | 66.2921 |
| 5 | 89 | 51 | 57.3034 |

Complete rounds: mean 64.2696 %, sd 4.3806 pp, observed range 11.2359 pp.

## Headline

- single-run sd **2.8571 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.9193 pp** before the gap is outside noise; 11.3199 pp for 80% power
- 33 of 89 tasks flipped; mean flip rate 0.1798 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.8571 pp, (posterior) 3.7584 pp; bootstrap precision of this estimate 1.2599 pp
- leave-one-round-out keeps MDD in 7.0337–8.0712 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| break-filter-js-from-html | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| chess-best-move | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| dna-assembly | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mcmc-sampling-stan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mteb-retrieve | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| polyglot-rust-c | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| portfolio-optimization | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| rstan-to-pystan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sanitize-git-repo | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| winning-avg-corewars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-cython-ext | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
