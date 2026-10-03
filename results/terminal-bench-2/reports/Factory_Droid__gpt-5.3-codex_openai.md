# Noise floor — terminal-bench 2.0 Factory_Droid__gpt-5.3-codex_openai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 69 | 77.5281 |
| 2 | 89 | 68 | 76.4045 |
| 3 | 89 | 68 | 76.4045 |
| 4 | 89 | 69 | 77.5281 |
| 5 | 89 | 70 | 78.6517 |

Complete rounds: mean 77.3034 %, sd 0.9401 pp, observed range 2.2472 pp.

## Headline

- single-run sd **2.2148 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.139 pp** before the gap is outside noise; 8.7751 pp for 80% power
- 19 of 89 tasks flipped; mean flip rate 0.1079 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.2148 pp, (posterior) 3.4791 pp; bootstrap precision of this estimate 0.9844 pp
- leave-one-round-out keeps MDD in 5.7975–6.1179 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| db-wal-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| dna-insert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-moves-from-video | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| gcode-to-text | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| model-extraction-relu-logits | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mteb-leaderboard | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| overfull-hbox | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| torch-tensor-parallelism | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| compile-compcert | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| extract-elf | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| feal-differential-cryptanalysis | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| gpt2-codegolf | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| make-mips-interpreter | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
