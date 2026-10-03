# Noise floor — terminal-bench 2.0 terminus-2__claude-opus-4-6_anthropic

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 60 | 67.4157 |
| 2 | 89 | 53 | 59.5506 |
| 3 | 89 | 56 | 62.9213 |
| 4 | 89 | 58 | 65.1685 |
| 5 | 89 | 53 | 59.5506 |

Complete rounds: mean 62.9213 %, sd 3.4631 pp, observed range 7.8651 pp.

## Headline

- single-run sd **2.7275 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.5601 pp** before the gap is outside noise; 10.8065 pp for 80% power
- 30 of 89 tasks flipped; mean flip rate 0.164 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.7275 pp, (posterior) 3.7316 pp; bootstrap precision of this estimate 1.2317 pp
- leave-one-round-out keeps MDD in 6.9991–7.7173 pp

## Adjudicability

0 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 445}.

## Drift screen

series (median completion tokens per round, {'run_total': 445}): [8177.0, 9317.0, 9864.0, 7583.0, 8008.0]
strongest single step: after round 3 (9119.333 → 7795.5, -14.52%, variance explained 0.5723). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-cython-ext | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pmars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| cancel-async-tasks | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| count-dataset-tokens | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| dna-assembly | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| dna-insert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| headless-terminal | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| make-mips-interpreter | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| overfull-hbox | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| path-tracing-reverse | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-cli | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| torch-pipeline-parallelism | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| bn-fit-modify | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| build-pov-ray | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
