# Noise floor — terminal-bench 2.0 codex__gpt-5.1-codex-mini_openai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 36 | 40.4494 |
| 2 | 89 | 35 | 39.3258 |
| 3 | 89 | 43 | 48.3146 |
| 4 | 89 | 41 | 46.0674 |
| 5 | 89 | 37 | 41.573 |

Complete rounds: mean 43.146 %, sd 3.8597 pp, observed range 8.9888 pp.

## Headline

- single-run sd **3.0724 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.5161 pp** before the gap is outside noise; 12.173 pp for 80% power
- 37 of 89 tasks flipped; mean flip rate 0.209 (max possible at n=5: 0.6)
- re-run (plugin) sd 3.0724 pp, (posterior) 3.904 pp; bootstrap precision of this estimate 1.3626 pp
- leave-one-round-out keeps MDD in 7.8872–8.6267 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {'run_total': 395}): [11378.0, 10195.5, 13225.0, 11341.5, 12623.0]
strongest single step: after round 2 (10786.75 → 12396.5, 14.92%, variance explained 0.5494). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-cython-ext | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pov-ray | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| compile-compcert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| count-dataset-tokens | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| financial-document-processor | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| git-leak-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| hf-model-inference | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mcmc-sampling-stan | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mteb-leaderboard | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mteb-retrieve | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| overfull-hbox | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| password-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pypi-server | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
