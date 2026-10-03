# Noise floor — terminal-bench 2.0 terminus-2__grok-4-0709_xai

436 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 436}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 17 | 19.1011 |
| 2 | 89 | 18 | 20.2247 |
| 3 | 89 | 24 | 26.9663 |
| 4 | 89 | 19 | 21.3483 |
| 5 (partial) | 80 | 25 | 31.25 |

Complete rounds: mean 21.9101 %, sd 3.4934 pp, observed range 7.8652 pp.

## Headline

- single-run sd **2.9738 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.2428 pp** before the gap is outside noise; 11.7823 pp for 80% power
- 35 of 89 tasks flipped; mean flip rate 0.1955 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.9738 pp, (posterior) 3.852 pp; bootstrap precision of this estimate 1.3427 pp
- leave-one-round-out keeps MDD in 7.8376–8.0973 pp

## Adjudicability

0 of 436 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 436}.

## Drift screen

series (median completion tokens per round, {'run_total': 435}): [2358.0, 1955.5, 2184.0, 1988.0, 2417.0]
strongest single step: after round 2 (2156.75 → 2196.333, 1.84%, variance explained 0.0107). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| bn-fit-modify | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pmars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pov-ray | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| code-from-image | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| count-dataset-tokens | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| distribution-search | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| fix-git | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| git-leak-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| headless-terminal | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| nginx-request-logging | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| polyglot-c-py | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| prove-plus-comm | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-cli | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| regex-log | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
