# Noise floor — terminal-bench 2.0 terminus-2__gpt-5-nano_openai

436 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 436}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 7 | 7.8652 |
| 2 | 89 | 7 | 7.8652 |
| 3 | 89 | 9 | 10.1124 |
| 4 | 89 | 5 | 5.618 |
| 5 (partial) | 80 | 7 | 8.75 |

Complete rounds: mean 7.8652 %, sd 1.8348 pp, observed range 4.4944 pp.

## Headline

- single-run sd **1.9159 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **5.3105 pp** before the gap is outside noise; 7.5909 pp for 80% power
- 15 of 89 tasks flipped; mean flip rate 0.0809 (max possible at n=5: 0.6)
- re-run (plugin) sd 1.9159 pp, (posterior) 3.3663 pp; bootstrap precision of this estimate 0.8555 pp
- leave-one-round-out keeps MDD in 4.8351–5.4436 pp

## Adjudicability

1 of 436 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 435, 'none': 1}.

## Drift screen

series (median completion tokens per round, {'run_total': 436}): [38378.0, 50920.0, 41144.0, 47994.0, 37968.0]
strongest single step: after round 2 (44649.0 → 42368.667, -5.11%, variance explained 0.0454). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| cobol-modernization | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| hf-model-inference | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| openssl-selfsigned-cert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| prove-plus-comm | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pypi-server | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| constraints-scheduling | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| distribution-search | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| fix-code-vulnerability | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| git-multibranch | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| modernize-scientific-stack | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| multi-source-data-merger | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| regex-log | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| schemelike-metacircular-eval | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| sqlite-with-gcov | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
