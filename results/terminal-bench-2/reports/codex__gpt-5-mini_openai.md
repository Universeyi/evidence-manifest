# Noise floor — terminal-bench 2.0 codex__gpt-5-mini_openai

437 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 437}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 29 | 32.5843 |
| 2 | 89 | 30 | 33.7079 |
| 3 | 89 | 30 | 33.7079 |
| 4 | 89 | 25 | 28.0899 |
| 5 (partial) | 81 | 24 | 29.6296 |

Complete rounds: mean 32.0225 %, sd 2.6747 pp, observed range 5.618 pp.

## Headline

- single-run sd **2.9839 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.2708 pp** before the gap is outside noise; 11.8223 pp for 80% power
- 36 of 89 tasks flipped; mean flip rate 0.2004 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.9839 pp, (posterior) 3.8567 pp; bootstrap precision of this estimate 1.3685 pp
- leave-one-round-out keeps MDD in 7.518–8.3182 pp

## Adjudicability

27 of 437 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 410, 'none': 27}.

## Drift screen

series (median completion tokens per round, {'run_total': 411}): [5416.0, 5197.5, 4813.0, 5271.5, 5156.0]
strongest single step: after round 2 (5306.75 → 5080.167, -4.27%, variance explained 0.3093). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-cython-ext | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| cancel-async-tasks | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| count-dataset-tokens | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-linear-cryptanalysis | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-git | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-ocaml-gc | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| git-multibranch | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| large-scale-text-editing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mcmc-sampling-stan | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-startup | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| regex-log | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sparql-university | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
