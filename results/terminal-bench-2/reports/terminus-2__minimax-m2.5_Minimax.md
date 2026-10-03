# Noise floor — terminal-bench 2.0 terminus-2__minimax-m2.5_Minimax

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 37 | 41.573 |
| 2 | 89 | 36 | 40.4494 |
| 3 | 89 | 43 | 48.3146 |
| 4 | 89 | 33 | 37.0787 |
| 5 | 89 | 39 | 43.8202 |

Complete rounds: mean 42.2472 %, sd 4.174 pp, observed range 11.2359 pp.

## Headline

- single-run sd **2.6742 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.4124 pp** before the gap is outside noise; 10.5953 pp for 80% power
- 29 of 89 tasks flipped; mean flip rate 0.1596 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.6742 pp, (posterior) 3.6552 pp; bootstrap precision of this estimate 1.1957 pp
- leave-one-round-out keeps MDD in 6.9996–7.4548 pp

## Adjudicability

34 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 411, 'none': 34}.

## Drift screen

series (median completion tokens per round, {'run_total': 445}): [7734.0, 7173.0, 7905.0, 7222.0, 7851.0]
strongest single step: after round 2 (7453.5 → 7659.333, 2.76%, variance explained 0.1024). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-elf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| fix-ocaml-gc | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| large-scale-text-editing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| llm-inference-batching-scheduler | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mcmc-sampling-stan | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| nginx-request-logging | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| password-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| regex-log | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| reshard-c4-data | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sparql-university | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sqlite-db-truncate | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| winning-avg-corewars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| bn-fit-modify | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| build-cython-ext | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
