# Noise floor — terminal-bench 2.0 Factory_Droid__gpt-5.2_openai

444 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 444}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 58 | 65.1685 |
| 2 | 89 | 57 | 64.0449 |
| 3 | 89 | 60 | 67.4157 |
| 4 | 89 | 58 | 65.1685 |
| 5 (partial) | 88 | 56 | 63.6364 |

Complete rounds: mean 65.4494 %, sd 1.4138 pp, observed range 3.3708 pp.

## Headline

- single-run sd **2.8603 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.9282 pp** before the gap is outside noise; 11.3326 pp for 80% power
- 33 of 89 tasks flipped; mean flip rate 0.1775 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.8603 pp, (posterior) 3.757 pp; bootstrap precision of this estimate 1.278 pp
- leave-one-round-out keeps MDD in 7.4232–7.8204 pp

## Adjudicability

444 of 444 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 444}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| break-filter-js-from-html | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-cython-ext | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| chess-best-move | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| circuit-fibsqrt | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| large-scale-text-editing | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| model-extraction-relu-logits | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| path-tracing | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| path-tracing-reverse | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| polyglot-c-py | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-alpine-ssh | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sanitize-git-repo | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| schemelike-metacircular-eval | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| torch-tensor-parallelism | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| adaptive-rejection-sampler | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| build-pov-ray | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
