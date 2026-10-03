# Noise floor — terminal-bench 2.0 claude-code__GLM-4.7_z-ai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 28 | 31.4607 |
| 2 | 89 | 31 | 34.8315 |
| 3 | 89 | 29 | 32.5843 |
| 4 | 89 | 27 | 30.3371 |
| 5 | 89 | 33 | 37.0787 |

Complete rounds: mean 33.2585 %, sd 2.706 pp, observed range 6.7416 pp.

## Headline

- single-run sd **2.4902 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.9024 pp** before the gap is outside noise; 9.8663 pp for 80% power
- 27 of 89 tasks flipped; mean flip rate 0.1393 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.4902 pp, (posterior) 3.5762 pp; bootstrap precision of this estimate 1.1176 pp
- leave-one-round-out keeps MDD in 6.1856–6.9475 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {'run_total': 440}): [0.0, 0.0, 0.0, 0.0, 0.0]
strongest single step: after round 2 (0.0 → 0.0, None%, variance explained 1.0). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-cython-ext | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pmars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| compile-compcert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mailman | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-cli | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-startup | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| adaptive-rejection-sampler | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| bn-fit-modify | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| count-dataset-tokens | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| fix-code-vulnerability | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| fix-git | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| fix-ocaml-gc | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| git-multibranch | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
