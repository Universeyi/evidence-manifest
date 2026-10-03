# Noise floor — terminal-bench 2.0 claude-code__minimax-m2.1_minimax

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 35 | 39.3258 |
| 2 | 89 | 29 | 32.5843 |
| 3 | 89 | 35 | 39.3258 |
| 4 | 89 | 33 | 37.0787 |
| 5 | 89 | 31 | 34.8315 |

Complete rounds: mean 36.6292 %, sd 2.9299 pp, observed range 6.7415 pp.

## Headline

- single-run sd **2.9847 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.273 pp** before the gap is outside noise; 11.8255 pp for 80% power
- 34 of 89 tasks flipped; mean flip rate 0.1933 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.9847 pp, (posterior) 3.8457 pp; bootstrap precision of this estimate 1.3272 pp
- leave-one-round-out keeps MDD in 7.3938–8.2361 pp

## Adjudicability

5 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 440, 'none': 5}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-cython-ext | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pmars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pov-ray | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| cancel-async-tasks | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| compile-compcert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| constraints-scheduling | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| distribution-search | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| fix-ocaml-gc | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| large-scale-text-editing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mcmc-sampling-stan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| openssl-selfsigned-cert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| overfull-hbox | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| portfolio-optimization | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
