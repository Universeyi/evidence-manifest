# Noise floor — terminal-bench 2.0 mux__gpt-5.3-codex_openai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 62 | 69.6629 |
| 2 | 89 | 65 | 73.0337 |
| 3 | 89 | 60 | 67.4157 |
| 4 | 89 | 61 | 68.5393 |
| 5 | 89 | 57 | 64.0449 |

Complete rounds: mean 68.5393 %, sd 3.2758 pp, observed range 8.9888 pp.

## Headline

- single-run sd **2.4574 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.8114 pp** before the gap is outside noise; 9.7363 pp for 80% power
- 24 of 89 tasks flipped; mean flip rate 0.1326 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.4574 pp, (posterior) 3.5931 pp; bootstrap precision of this estimate 1.0918 pp
- leave-one-round-out keeps MDD in 6.0553–6.8871 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| db-wal-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| dna-insert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mailman | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| make-mips-interpreter | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| model-extraction-relu-logits | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mteb-leaderboard | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| polyglot-c-py | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| query-optimize | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| torch-tensor-parallelism | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| tune-mjcf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pov-ray | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| dna-assembly | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| fix-code-vulnerability | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| large-scale-text-editing | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
