# Noise floor — terminal-bench 2.0 mini-swe-agent__gemini-2.5-pro_gemini

444 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 444}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 29 | 32.5843 |
| 2 | 89 | 21 | 23.5955 |
| 3 | 89 | 20 | 22.4719 |
| 4 | 89 | 22 | 24.7191 |
| 5 (partial) | 88 | 24 | 27.2727 |

Complete rounds: mean 25.8427 %, sd 4.5871 pp, observed range 10.1124 pp.

## Headline

- single-run sd **2.6332 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.2987 pp** before the gap is outside noise; 10.4328 pp for 80% power
- 29 of 89 tasks flipped; mean flip rate 0.1506 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.6332 pp, (posterior) 3.5982 pp; bootstrap precision of this estimate 1.1612 pp
- leave-one-round-out keeps MDD in 6.9589–7.2061 pp

## Adjudicability

9 of 444 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 435, 'none': 9}.

## Drift screen

series (median completion tokens per round, {'run_total': 434}): [20081.0, 26955.0, 16969.0, 19496.0, 19446.0]
strongest single step: after round 2 (23518.0 → 18637.0, -20.75%, variance explained 0.507). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pov-ray | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| feal-differential-cryptanalysis | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| git-leak-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| log-summary-date-ranges | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mailman | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| multi-source-data-merger | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| vulnerable-secret | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| cancel-async-tasks | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| cobol-modernization | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| code-from-image | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| configure-git-webserver | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| distribution-search | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| dna-insert | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
