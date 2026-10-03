# Noise floor — terminal-bench 2.0 codex__gpt-5.1-codex-max_openai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 52 | 58.427 |
| 2 | 89 | 51 | 57.3034 |
| 3 | 89 | 56 | 62.9213 |
| 4 | 89 | 57 | 64.0449 |
| 5 | 89 | 53 | 59.5506 |

Complete rounds: mean 60.4494 %, sd 2.9083 pp, observed range 6.7415 pp.

## Headline

- single-run sd **2.69 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.4562 pp** before the gap is outside noise; 10.6579 pp for 80% power
- 29 of 89 tasks flipped; mean flip rate 0.164 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.69 pp, (posterior) 3.7132 pp; bootstrap precision of this estimate 1.209 pp
- leave-one-round-out keeps MDD in 7.1116–7.6385 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {'run_total': 393}): [14226.0, 12283.5, 12448.0, 14327.0, 14356.0]
strongest single step: after round 3 (12985.833 → 14341.5, 10.44%, variance explained 0.4872). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| bn-fit-modify | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pov-ray | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| cancel-async-tasks | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| count-dataset-tokens | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| crack-7z-hash | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| feal-differential-cryptanalysis | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| gcode-to-text | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| model-extraction-relu-logits | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mteb-leaderboard | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| path-tracing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| reshard-c4-data | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| schemelike-metacircular-eval | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sparql-university | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
