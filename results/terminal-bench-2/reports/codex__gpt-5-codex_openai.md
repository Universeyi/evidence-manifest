# Noise floor — terminal-bench 2.0 codex__gpt-5-codex_openai

436 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 436}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 38 | 42.6966 |
| 2 | 89 | 40 | 44.9438 |
| 3 | 89 | 41 | 46.0674 |
| 4 | 89 | 40 | 44.9438 |
| 5 (partial) | 80 | 34 | 42.5 |

Complete rounds: mean 44.6629 %, sd 1.4138 pp, observed range 3.3708 pp.

## Headline

- single-run sd **2.6873 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.4487 pp** before the gap is outside noise; 10.6472 pp for 80% power
- 29 of 89 tasks flipped; mean flip rate 0.1644 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.6873 pp, (posterior) 3.7052 pp; bootstrap precision of this estimate 1.243 pp
- leave-one-round-out keeps MDD in 7.0254–7.3137 pp

## Adjudicability

268 of 436 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 268, 'per_step': 168}.

## Drift screen

series (median completion tokens per round, {'run_total': 167}): [6490.5, 7688.5, 5576.0, 3808.0, 3696.0]
strongest single step: after round 3 (6585.0 → 3752.0, -43.02%, variance explained 0.8106). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| bn-fit-modify | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| cancel-async-tasks | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-linear-cryptanalysis | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| financial-document-processor | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-code-vulnerability | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| fix-ocaml-gc | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| headless-terminal | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| hf-model-inference | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| password-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-cli | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-startup | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| schemelike-metacircular-eval | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| tune-mjcf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| adaptive-rejection-sampler | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
