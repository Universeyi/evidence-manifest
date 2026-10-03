# Noise floor — terminal-bench 2.0 Factory_Droid__claude-opus-4-6_anthropic

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 61 | 68.5393 |
| 2 | 89 | 64 | 71.9101 |
| 3 | 89 | 61 | 68.5393 |
| 4 | 89 | 63 | 70.7865 |
| 5 | 89 | 62 | 69.6629 |

Complete rounds: mean 69.8876 %, sd 1.465 pp, observed range 3.3708 pp.

## Headline

- single-run sd **2.4912 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.9051 pp** before the gap is outside noise; 9.8702 pp for 80% power
- 26 of 89 tasks flipped; mean flip rate 0.1416 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.4912 pp, (posterior) 3.6093 pp; bootstrap precision of this estimate 1.1389 pp
- leave-one-round-out keeps MDD in 6.511–6.8234 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| cancel-async-tasks | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| compile-compcert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| configure-git-webserver | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| count-dataset-tokens | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| dna-insert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| make-mips-interpreter | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| schemelike-metacircular-eval | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sparql-university | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| tune-mjcf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| video-processing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| break-filter-js-from-html | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| build-pmars | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| build-pov-ray | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| dna-assembly | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
