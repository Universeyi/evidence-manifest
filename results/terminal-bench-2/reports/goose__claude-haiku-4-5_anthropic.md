# Noise floor — terminal-bench 2.0 goose__claude-haiku-4-5_anthropic

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 31 | 34.8315 |
| 2 | 89 | 36 | 40.4494 |
| 3 | 89 | 32 | 35.9551 |
| 4 | 89 | 32 | 35.9551 |
| 5 | 89 | 27 | 30.3371 |

Complete rounds: mean 35.5056 %, sd 3.606 pp, observed range 10.1123 pp.

## Headline

- single-run sd **2.9668 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.2234 pp** before the gap is outside noise; 11.7546 pp for 80% power
- 34 of 89 tasks flipped; mean flip rate 0.1933 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.9668 pp, (posterior) 3.8239 pp; bootstrap precision of this estimate 1.3244 pp
- leave-one-round-out keeps MDD in 7.6754–8.1328 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-cython-ext | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pov-ray | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| caffe-cifar-10 | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| compile-compcert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| crack-7z-hash | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| custom-memory-heap-crash | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| fix-ocaml-gc | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| hf-model-inference | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| largest-eigenval | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mailman | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| regex-log | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| reshard-c4-data | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
