# Noise floor — terminal-bench 2.0 gemini-cli__gemini-2.5-pro_gemini

437 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 437}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 22 | 24.7191 |
| 2 | 89 | 19 | 21.3483 |
| 3 | 89 | 16 | 17.9775 |
| 4 | 89 | 16 | 17.9775 |
| 5 (partial) | 81 | 13 | 16.0494 |

Complete rounds: mean 20.5056 %, sd 3.2273 pp, observed range 6.7416 pp.

## Headline

- single-run sd **2.9043 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.0502 pp** before the gap is outside noise; 11.507 pp for 80% power
- 35 of 89 tasks flipped; mean flip rate 0.1865 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.9043 pp, (posterior) 3.8246 pp; bootstrap precision of this estimate 1.2994 pp
- leave-one-round-out keeps MDD in 7.268–7.9584 pp

## Adjudicability

56 of 437 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 381, 'none': 56}.

## Drift screen

series (median completion tokens per round, {'run_total': 381}): [10585.5, 12137.0, 13496.0, 9214.0, 12747.0]
strongest single step: after round 3 (12072.833 → 10980.5, -9.05%, variance explained 0.1202). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| cobol-modernization | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| custom-memory-heap-crash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| financial-document-processor | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-git | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| hf-model-inference | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| nginx-request-logging | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| polyglot-c-py | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| portfolio-optimization | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| regex-log | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sparql-university | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| tune-mjcf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pmars | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| build-pov-ray | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| compile-compcert | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
