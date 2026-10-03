# Noise floor — terminal-bench 2.0 openhands__gemini-2.5-pro_gemini

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 17 | 19.1011 |
| 2 | 89 | 11 | 12.3596 |
| 3 | 89 | 18 | 20.2247 |
| 4 | 89 | 14 | 15.7303 |
| 5 | 89 | 13 | 14.6067 |

Complete rounds: mean 16.4045 %, sd 3.237 pp, observed range 7.8651 pp.

## Headline

- single-run sd **2.818 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.811 pp** before the gap is outside noise; 11.165 pp for 80% power
- 32 of 89 tasks flipped; mean flip rate 0.1753 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.818 pp, (posterior) 3.7538 pp; bootstrap precision of this estimate 1.2544 pp
- leave-one-round-out keeps MDD in 7.0459–7.896 pp

## Adjudicability

9 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 436, 'none': 9}.

## Drift screen

series (median completion tokens per round, {'run_total': 435}): [5765.0, 5771.0, 6059.0, 4754.0, 5522.0]
strongest single step: after round 3 (5865.0 → 5138.0, -12.4%, variance explained 0.6435). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-pmars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| cobol-modernization | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| custom-memory-heap-crash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-ocaml-gc | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| git-leak-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| hf-model-inference | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| modernize-scientific-stack | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| multi-source-data-merger | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| nginx-request-logging | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| regex-log | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sparql-university | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| vulnerable-secret | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| adaptive-rejection-sampler | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
