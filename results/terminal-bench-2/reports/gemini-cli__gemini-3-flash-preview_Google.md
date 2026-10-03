# Noise floor — terminal-bench 2.0 gemini-cli__gemini-3-flash-preview_Google

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 43 | 48.3146 |
| 2 | 89 | 47 | 52.809 |
| 3 | 89 | 49 | 55.0562 |
| 4 | 89 | 44 | 49.4382 |
| 5 | 89 | 44 | 49.4382 |

Complete rounds: mean 51.0112 %, sd 2.8202 pp, observed range 6.7416 pp.

## Headline

- single-run sd **3.0515 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.4582 pp** before the gap is outside noise; 12.0902 pp for 80% power
- 34 of 89 tasks flipped; mean flip rate 0.2022 (max possible at n=5: 0.6)
- re-run (plugin) sd 3.0515 pp, (posterior) 3.8469 pp; bootstrap precision of this estimate 1.3571 pp
- leave-one-round-out keeps MDD in 7.9642–8.2289 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| break-filter-js-from-html | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-cython-ext | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pmars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| cancel-async-tasks | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| circuit-fibsqrt | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| configure-git-webserver | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| crack-7z-hash | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| distribution-search | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| feal-linear-cryptanalysis | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| financial-document-processor | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| headless-terminal | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| hf-model-inference | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| largest-eigenval | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| log-summary-date-ranges | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mailman | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
