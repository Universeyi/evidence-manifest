# Noise floor — terminal-bench 2.0 mini-swe-agent__gemini-2.5-flash_gemini

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 12 | 13.4831 |
| 2 | 89 | 15 | 16.8539 |
| 3 | 89 | 22 | 24.7191 |
| 4 | 89 | 14 | 15.7303 |
| 5 | 89 | 13 | 14.6067 |

Complete rounds: mean 17.0786 %, sd 4.4521 pp, observed range 11.236 pp.

## Headline

- single-run sd **2.5387 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.0368 pp** before the gap is outside noise; 10.0584 pp for 80% power
- 27 of 89 tasks flipped; mean flip rate 0.1438 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.5387 pp, (posterior) 3.6022 pp; bootstrap precision of this estimate 1.1346 pp
- leave-one-round-out keeps MDD in 6.4109–7.1951 pp

## Adjudicability

13 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 432, 'none': 13}.

## Drift screen

series (median completion tokens per round, {'run_total': 431}): [14548.0, 13780.5, 9638.0, 12708.5, 11032.0]
strongest single step: after round 2 (14164.25 → 11126.167, -21.45%, variance explained 0.688). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-pmars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| cobol-modernization | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| custom-memory-heap-crash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| hf-model-inference | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| multi-source-data-merger | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| nginx-request-logging | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| portfolio-optimization | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-cli | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| vulnerable-secret | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| bn-fit-modify | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| build-pov-ray | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| cancel-async-tasks | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| code-from-image | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| crack-7z-hash | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
