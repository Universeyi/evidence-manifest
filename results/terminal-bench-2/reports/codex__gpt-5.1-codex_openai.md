# Noise floor — terminal-bench 2.0 codex__gpt-5.1-codex_openai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 54 | 60.6742 |
| 2 | 89 | 55 | 61.7978 |
| 3 | 89 | 53 | 59.5506 |
| 4 | 89 | 50 | 56.1798 |
| 5 | 89 | 45 | 50.5618 |

Complete rounds: mean 57.7528 %, sd 4.5363 pp, observed range 11.236 pp.

## Headline

- single-run sd **3.0066 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.3337 pp** before the gap is outside noise; 11.9123 pp for 80% power
- 38 of 89 tasks flipped; mean flip rate 0.2 (max possible at n=5: 0.6)
- re-run (plugin) sd 3.0066 pp, (posterior) 3.8414 pp; bootstrap precision of this estimate 1.3261 pp
- leave-one-round-out keeps MDD in 7.4212–8.4163 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {'run_total': 391}): [8898.5, 9110.0, 9567.0, 10052.0, 9038.5]
strongest single step: after round 2 (9004.25 → 9552.5, 6.09%, variance explained 0.4021). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| circuit-fibsqrt | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| count-dataset-tokens | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| largest-eigenval | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| make-mips-interpreter | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mcmc-sampling-stan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mteb-leaderboard | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| password-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| protein-assembly | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-alpine-ssh | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| reshard-c4-data | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sanitize-git-repo | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sparql-university | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| write-compressor | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| adaptive-rejection-sampler | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| break-filter-js-from-html | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
