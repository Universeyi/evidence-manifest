# Noise floor — terminal-bench 2.0 mini-swe-agent__claude-opus-4-1-20250805_anthropic

444 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 444}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 28 | 31.4607 |
| 2 | 89 | 33 | 37.0787 |
| 3 | 89 | 32 | 35.9551 |
| 4 | 89 | 34 | 38.2022 |
| 5 (partial) | 88 | 29 | 32.9545 |

Complete rounds: mean 35.6742 %, sd 2.955 pp, observed range 6.7415 pp.

## Headline

- single-run sd **2.5648 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.1091 pp** before the gap is outside noise; 10.1618 pp for 80% power
- 26 of 89 tasks flipped; mean flip rate 0.1461 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.5648 pp, (posterior) 3.6272 pp; bootstrap precision of this estimate 1.1385 pp
- leave-one-round-out keeps MDD in 6.5082–7.1995 pp

## Adjudicability

15 of 444 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 429, 'none': 15}.

## Drift screen

series (median completion tokens per round, {'run_total': 428}): [7465.0, 6587.0, 6081.0, 6393.5, 5076.0]
strongest single step: after round 2 (7026.0 → 5850.167, -16.74%, variance explained 0.5544). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-pmars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| code-from-image | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-elf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| fix-ocaml-gc | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| large-scale-text-editing | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mailman | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mcmc-sampling-stan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| openssl-selfsigned-cert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| overfull-hbox | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-cli | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-startup | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sqlite-with-gcov | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| bn-fit-modify | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| build-pov-ray | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
