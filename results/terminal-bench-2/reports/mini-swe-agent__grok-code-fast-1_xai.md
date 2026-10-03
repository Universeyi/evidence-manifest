# Noise floor — terminal-bench 2.0 mini-swe-agent__grok-code-fast-1_xai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 24 | 26.9663 |
| 2 | 89 | 19 | 21.3483 |
| 3 | 89 | 25 | 28.0899 |
| 4 | 89 | 23 | 25.8427 |
| 5 | 89 | 24 | 26.9663 |

Complete rounds: mean 25.8427 %, sd 2.6351 pp, observed range 6.7416 pp.

## Headline

- single-run sd **2.6544 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.3575 pp** before the gap is outside noise; 10.5168 pp for 80% power
- 30 of 89 tasks flipped; mean flip rate 0.1596 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.6544 pp, (posterior) 3.6691 pp; bootstrap precision of this estimate 1.208 pp
- leave-one-round-out keeps MDD in 6.8392–7.4337 pp

## Adjudicability

9 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 436, 'none': 9}.

## Drift screen

series (median completion tokens per round, {'run_total': 435}): [2132.0, 2086.0, 2040.0, 2096.0, 1842.0]
strongest single step: after round 3 (2086.0 → 1969.0, -5.61%, variance explained 0.3104). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-pmars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pov-ray | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| custom-memory-heap-crash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-ocaml-gc | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| kv-store-grpc | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| large-scale-text-editing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| openssl-selfsigned-cert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| winning-avg-corewars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-cython-ext | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| cancel-async-tasks | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| code-from-image | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| crack-7z-hash | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
