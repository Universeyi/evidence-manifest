# Noise floor — terminal-bench 2.0 terminus-2__gemini-3-flash-preview_gemini

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 46 | 51.6854 |
| 2 | 89 | 46 | 51.6854 |
| 3 | 89 | 47 | 52.809 |
| 4 | 89 | 46 | 51.6854 |
| 5 | 89 | 45 | 50.5618 |

Complete rounds: mean 51.6854 %, sd 0.7945 pp, observed range 2.2472 pp.

## Headline

- single-run sd **3.205 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.8836 pp** before the gap is outside noise; 12.6983 pp for 80% power
- 39 of 89 tasks flipped; mean flip rate 0.227 (max possible at n=5: 0.6)
- re-run (plugin) sd 3.205 pp, (posterior) 3.927 pp; bootstrap precision of this estimate 1.4297 pp
- leave-one-round-out keeps MDD in 8.0255–8.8656 pp

## Adjudicability

1 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 444, 'none': 1}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| break-filter-js-from-html | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-cython-ext | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pmars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pov-ray | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| cancel-async-tasks | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| circuit-fibsqrt | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| code-from-image | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| compile-compcert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| count-dataset-tokens | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| crack-7z-hash | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| feal-linear-cryptanalysis | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| llm-inference-batching-scheduler | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mailman | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
