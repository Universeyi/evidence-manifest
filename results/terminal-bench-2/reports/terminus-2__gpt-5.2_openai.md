# Noise floor — terminal-bench 2.0 terminus-2__gpt-5.2_openai

444 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 444}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 49 | 55.0562 |
| 2 | 89 | 41 | 46.0674 |
| 3 | 89 | 51 | 57.3034 |
| 4 | 89 | 50 | 56.1798 |
| 5 (partial) | 88 | 49 | 55.6818 |

Complete rounds: mean 53.6517 %, sd 5.1388 pp, observed range 11.236 pp.

## Headline

- single-run sd **2.9278 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.1153 pp** before the gap is outside noise; 11.6001 pp for 80% power
- 35 of 89 tasks flipped; mean flip rate 0.1918 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.9278 pp, (posterior) 3.8092 pp; bootstrap precision of this estimate 1.3247 pp
- leave-one-round-out keeps MDD in 7.6912–7.9958 pp

## Adjudicability

1 of 444 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 443, 'none': 1}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| regex-chess | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| compile-compcert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| dna-insert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| financial-document-processor | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| git-leak-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| kv-store-grpc | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| large-scale-text-editing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mcmc-sampling-stan | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mteb-leaderboard | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-alpine-ssh | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-startup | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sanitize-git-repo | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sqlite-db-truncate | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| tune-mjcf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
