# Noise floor — terminal-bench 2.0 mini-swe-agent__grok-4-0709_xai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 25 | 28.0899 |
| 2 | 89 | 21 | 23.5955 |
| 3 | 89 | 25 | 28.0899 |
| 4 | 89 | 17 | 19.1011 |
| 5 | 89 | 25 | 28.0899 |

Complete rounds: mean 25.3933 %, sd 4.0199 pp, observed range 8.9888 pp.

## Headline

- single-run sd **2.9918 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.2927 pp** before the gap is outside noise; 11.8536 pp for 80% power
- 36 of 89 tasks flipped; mean flip rate 0.1978 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.9918 pp, (posterior) 3.8268 pp; bootstrap precision of this estimate 1.332 pp
- leave-one-round-out keeps MDD in 7.6968–8.2849 pp

## Adjudicability

32 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 413, 'none': 32}.

## Drift screen

series (median completion tokens per round, {'run_total': 411}): [2521.0, 2550.0, 3192.0, 1889.0, 2414.5]
strongest single step: after round 3 (2754.333 → 2151.75, -21.88%, variance explained 0.5057). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| constraints-scheduling | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| count-dataset-tokens | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| custom-memory-heap-crash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-differential-cryptanalysis | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-code-vulnerability | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| git-multibranch | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| headless-terminal | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mailman | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| nginx-request-logging | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| portfolio-optimization | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| prove-plus-comm | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pypi-server | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-cli | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sparql-university | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
