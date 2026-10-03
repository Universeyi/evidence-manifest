# Noise floor — terminal-bench 2.0 mini-swe-agent__gpt-5-codex_openai

444 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 444}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 42 | 47.191 |
| 2 | 89 | 39 | 43.8202 |
| 3 | 89 | 37 | 41.573 |
| 4 | 89 | 34 | 38.2022 |
| 5 (partial) | 88 | 32 | 36.3636 |

Complete rounds: mean 42.6966 %, sd 3.7826 pp, observed range 8.9888 pp.

## Headline

- single-run sd **2.8404 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.873 pp** before the gap is outside noise; 11.2538 pp for 80% power
- 32 of 89 tasks flipped; mean flip rate 0.1775 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.8404 pp, (posterior) 3.7552 pp; bootstrap precision of this estimate 1.2723 pp
- leave-one-round-out keeps MDD in 7.3808–7.9712 pp

## Adjudicability

18 of 444 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 426, 'none': 18}.

## Drift screen

series (median completion tokens per round, {'run_total': 425}): [20615.0, 18871.0, 17598.0, 13114.0, 19117.5]
strongest single step: after round 2 (19743.0 → 16609.833, -15.87%, variance explained 0.3593). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-cython-ext | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pov-ray | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| crack-7z-hash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-differential-cryptanalysis | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-linear-cryptanalysis | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| llm-inference-batching-scheduler | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| nginx-request-logging | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| password-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| protein-assembly | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pypi-server | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sparql-university | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| tune-mjcf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
