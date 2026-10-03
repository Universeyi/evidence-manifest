# Noise floor — terminal-bench 2.0 letta-code__gemini-3-pro-preview_google

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 50 | 56.1798 |
| 2 | 89 | 51 | 57.3034 |
| 3 | 89 | 50 | 56.1798 |
| 4 | 89 | 48 | 53.9326 |
| 5 | 89 | 50 | 56.1798 |

Complete rounds: mean 55.9551 %, sd 1.2308 pp, observed range 3.3708 pp.

## Headline

- single-run sd **3.0137 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.3534 pp** before the gap is outside noise; 11.9404 pp for 80% power
- 35 of 89 tasks flipped; mean flip rate 0.2045 (max possible at n=5: 0.6)
- re-run (plugin) sd 3.0137 pp, (posterior) 3.8183 pp; bootstrap precision of this estimate 1.3515 pp
- leave-one-round-out keeps MDD in 7.8675–8.2741 pp

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
| compile-compcert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| large-scale-text-editing | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| largest-eigenval | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| log-summary-date-ranges | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| path-tracing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| polyglot-rust-c | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-cli | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
