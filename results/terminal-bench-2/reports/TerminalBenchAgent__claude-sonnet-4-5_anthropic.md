# Noise floor — terminal-bench 2.0 TerminalBenchAgent__claude-sonnet-4-5_anthropic

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 42 | 47.191 |
| 2 | 89 | 42 | 47.191 |
| 3 | 89 | 44 | 49.4382 |
| 4 | 89 | 37 | 41.573 |
| 5 | 89 | 42 | 47.191 |

Complete rounds: mean 46.5168 %, sd 2.93 pp, observed range 7.8652 pp.

## Headline

- single-run sd **2.4143 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.692 pp** before the gap is outside noise; 9.5656 pp for 80% power
- 24 of 89 tasks flipped; mean flip rate 0.1281 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.4143 pp, (posterior) 3.5748 pp; bootstrap precision of this estimate 1.0679 pp
- leave-one-round-out keeps MDD in 6.1947–6.7829 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-pov-ray | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| crack-7z-hash | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| largest-eigenval | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| llm-inference-batching-scheduler | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| openssl-selfsigned-cert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| password-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| regex-log | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| reshard-c4-data | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| bn-fit-modify | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| compile-compcert | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| count-dataset-tokens | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| distribution-search | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| feal-differential-cryptanalysis | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| fix-ocaml-gc | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
