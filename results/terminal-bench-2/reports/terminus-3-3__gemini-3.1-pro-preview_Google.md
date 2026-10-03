# Noise floor — terminal-bench 2.0 terminus-3-3__gemini-3.1-pro-preview_Google

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 65 | 73.0337 |
| 2 | 89 | 68 | 76.4045 |
| 3 | 89 | 66 | 74.1573 |
| 4 | 89 | 67 | 75.2809 |
| 5 | 89 | 67 | 75.2809 |

Complete rounds: mean 74.8315 %, sd 1.2811 pp, observed range 3.3708 pp.

## Headline

- single-run sd **2.6217 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.2668 pp** before the gap is outside noise; 10.3873 pp for 80% power
- 28 of 89 tasks flipped; mean flip rate 0.1528 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.6217 pp, (posterior) 3.6097 pp; bootstrap precision of this estimate 1.1711 pp
- leave-one-round-out keeps MDD in 6.8037–7.3389 pp

## Adjudicability

14 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 431, 'none': 14}.

## Drift screen

series (median completion tokens per round, {'run_total': 445}): [21830.0, 21840.0, 24979.0, 23458.0, 19949.0]
strongest single step: after round 3 (22883.0 → 21703.5, -5.15%, variance explained 0.1158). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| crack-7z-hash | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| dna-assembly | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| dna-insert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-elf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| financial-document-processor | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| make-mips-interpreter | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| path-tracing-reverse | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| regex-chess | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| rstan-to-pystan | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sanitize-git-repo | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| torch-tensor-parallelism | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-cython-ext | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| build-pov-ray | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| db-wal-recovery | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
