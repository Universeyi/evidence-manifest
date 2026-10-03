# Noise floor — terminal-bench 2.0 openhands__gemini-2.5-flash_gemini

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 14 | 15.7303 |
| 2 | 89 | 14 | 15.7303 |
| 3 | 89 | 16 | 17.9775 |
| 4 | 89 | 14 | 15.7303 |
| 5 | 89 | 15 | 16.8539 |

Complete rounds: mean 16.4045 %, sd 1.005 pp, observed range 2.2472 pp.

## Headline

- single-run sd **2.4397 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.7624 pp** before the gap is outside noise; 9.6662 pp for 80% power
- 25 of 89 tasks flipped; mean flip rate 0.1326 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.4397 pp, (posterior) 3.5586 pp; bootstrap precision of this estimate 1.1131 pp
- leave-one-round-out keeps MDD in 6.2125–6.8538 pp

## Adjudicability

9 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 436, 'none': 9}.

## Drift screen

series (median completion tokens per round, {'run_total': 436}): [9618.0, 11199.0, 9782.0, 9529.0, 9967.0]
strongest single step: after round 2 (10408.5 → 9759.333, -6.24%, variance explained 0.273). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| code-from-image | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| headless-terminal | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mcmc-sampling-stan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| model-extraction-relu-logits | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-startup | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| regex-log | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sqlite-with-gcov | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pmars | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| build-pov-ray | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| cobol-modernization | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| compile-compcert | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| constraints-scheduling | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| crack-7z-hash | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
