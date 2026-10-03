# Noise floor — terminal-bench 2.0 ruley__gpt-5.3-codex_OpenAI

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 60 | 67.4157 |
| 2 | 89 | 66 | 74.1573 |
| 3 | 89 | 65 | 73.0337 |
| 4 | 89 | 60 | 67.4157 |
| 5 | 89 | 62 | 69.6629 |

Complete rounds: mean 70.3371 %, sd 3.138 pp, observed range 6.7416 pp.

## Headline

- single-run sd **2.622 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.2677 pp** before the gap is outside noise; 10.3885 pp for 80% power
- 29 of 89 tasks flipped; mean flip rate 0.1528 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.622 pp, (posterior) 3.6156 pp; bootstrap precision of this estimate 1.1544 pp
- leave-one-round-out keeps MDD in 6.7563–7.2483 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| cancel-async-tasks | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| compile-compcert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| dna-assembly | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| kv-store-grpc | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| overfull-hbox | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| polyglot-rust-c | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| protein-assembly | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| regex-chess | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| tune-mjcf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| adaptive-rejection-sampler | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| build-pov-ray | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| circuit-fibsqrt | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| db-wal-recovery | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| dna-insert | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
