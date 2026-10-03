# Noise floor — terminal-bench 2.0 ii-agent-simple__gemini-3-pro-preview_gemini

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 59 | 66.2921 |
| 2 | 89 | 55 | 61.7978 |
| 3 | 89 | 54 | 60.6742 |
| 4 | 89 | 50 | 56.1798 |
| 5 | 89 | 57 | 64.0449 |

Complete rounds: mean 61.7978 %, sd 3.8103 pp, observed range 10.1123 pp.

## Headline

- single-run sd **2.877 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.9745 pp** before the gap is outside noise; 11.3988 pp for 80% power
- 35 of 89 tasks flipped; mean flip rate 0.1843 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.877 pp, (posterior) 3.7671 pp; bootstrap precision of this estimate 1.2857 pp
- leave-one-round-out keeps MDD in 7.5576–7.9279 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-cython-ext | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pmars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-elf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| large-scale-text-editing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| largest-eigenval | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| path-tracing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| protein-assembly | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-alpine-ssh | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| query-optimize | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| schemelike-metacircular-eval | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| winning-avg-corewars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| adaptive-rejection-sampler | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| bn-fit-modify | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| cancel-async-tasks | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
