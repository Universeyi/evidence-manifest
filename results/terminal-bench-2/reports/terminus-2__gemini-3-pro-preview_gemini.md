# Noise floor — terminal-bench 2.0 terminus-2__gemini-3-pro-preview_gemini

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 52 | 58.427 |
| 2 | 89 | 46 | 51.6854 |
| 3 | 89 | 51 | 57.3034 |
| 4 | 89 | 52 | 58.427 |
| 5 | 89 | 52 | 58.427 |

Complete rounds: mean 56.854 %, sd 2.93 pp, observed range 6.7416 pp.

## Headline

- single-run sd **2.5094 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.9556 pp** before the gap is outside noise; 9.9423 pp for 80% power
- 25 of 89 tasks flipped; mean flip rate 0.1416 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.5094 pp, (posterior) 3.6129 pp; bootstrap precision of this estimate 1.1337 pp
- leave-one-round-out keeps MDD in 6.5742–6.8527 pp

## Adjudicability

0 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 445}.

## Drift screen

series (median completion tokens per round, {'run_total': 445}): [17326.0, 18172.0, 15688.0, 15369.0, 17760.0]
strongest single step: after round 2 (17749.0 → 16272.333, -8.32%, variance explained 0.4124). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| bn-fit-modify | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| break-filter-js-from-html | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-cython-ext | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pmars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| circuit-fibsqrt | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| count-dataset-tokens | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-linear-cryptanalysis | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| overfull-hbox | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| protein-assembly | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sparql-university | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| winning-avg-corewars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| cancel-async-tasks | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| compile-compcert | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
