# Noise floor — terminal-bench 2.0 gemini-cli__gemini-2.5-flash_gemini

439 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 439}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 17 | 19.1011 |
| 2 | 89 | 11 | 12.3596 |
| 3 | 89 | 10 | 11.236 |
| 4 | 89 | 15 | 16.8539 |
| 5 (partial) | 83 | 15 | 18.0723 |

Complete rounds: mean 14.8877 %, sd 3.7124 pp, observed range 7.8651 pp.

## Headline

- single-run sd **2.3248 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.4439 pp** before the gap is outside noise; 9.211 pp for 80% power
- 22 of 89 tasks flipped; mean flip rate 0.121 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.3248 pp, (posterior) 3.5261 pp; bootstrap precision of this estimate 1.0446 pp
- leave-one-round-out keeps MDD in 5.4738–6.6094 pp

## Adjudicability

33 of 439 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 406, 'none': 33}.

## Drift screen

series (median completion tokens per round, {'run_total': 406}): [4140.0, 3883.0, 5649.0, 4501.0, 3627.0]
strongest single step: after round 2 (4011.5 → 4592.333, 14.48%, variance explained 0.1623). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-pov-ray | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| build-pmars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| cobol-modernization | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| code-from-image | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| nginx-request-logging | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| regex-log | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sam-cell-seg | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sqlite-with-gcov | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| caffe-cifar-10 | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| constraints-scheduling | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| count-dataset-tokens | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| financial-document-processor | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| fix-code-vulnerability | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| fix-ocaml-gc | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
