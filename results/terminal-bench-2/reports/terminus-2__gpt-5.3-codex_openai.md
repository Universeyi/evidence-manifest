# Noise floor — terminal-bench 2.0 terminus-2__gpt-5.3-codex_openai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 53 | 59.5506 |
| 2 | 89 | 59 | 66.2921 |
| 3 | 89 | 59 | 66.2921 |
| 4 | 89 | 60 | 67.4157 |
| 5 | 89 | 57 | 64.0449 |

Complete rounds: mean 64.7191 %, sd 3.138 pp, observed range 7.8651 pp.

## Headline

- single-run sd **2.7824 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.7123 pp** before the gap is outside noise; 11.024 pp for 80% power
- 32 of 89 tasks flipped; mean flip rate 0.1708 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.7824 pp, (posterior) 3.7499 pp; bootstrap precision of this estimate 1.2387 pp
- leave-one-round-out keeps MDD in 7.1618–7.6191 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {'run_total': 445}): [23855.0, 23698.0, 18414.0, 19329.0, 20615.0]
strongest single step: after round 2 (23776.5 → 19452.667, -18.19%, variance explained 0.9013). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| compile-compcert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| crack-7z-hash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| dna-insert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| log-summary-date-ranges | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| path-tracing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| path-tracing-reverse | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-alpine-ssh | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| regex-chess | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| rstan-to-pystan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| write-compressor | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| adaptive-rejection-sampler | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| build-pmars | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| build-pov-ray | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
