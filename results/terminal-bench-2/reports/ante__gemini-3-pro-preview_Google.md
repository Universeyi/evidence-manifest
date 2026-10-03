# Noise floor — terminal-bench 2.0 ante__gemini-3-pro-preview_Google

444 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 444}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 64 | 71.9101 |
| 2 | 89 | 63 | 70.7865 |
| 3 | 89 | 55 | 61.7978 |
| 4 | 89 | 54 | 60.6742 |
| 5 (partial) | 88 | 52 | 59.0909 |

Complete rounds: mean 66.2922 %, sd 5.8743 pp, observed range 11.2359 pp.

## Headline

- single-run sd **2.7336 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.577 pp** before the gap is outside noise; 10.8306 pp for 80% power
- 33 of 89 tasks flipped; mean flip rate 0.1685 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.7336 pp, (posterior) 3.7432 pp; bootstrap precision of this estimate 1.2326 pp
- leave-one-round-out keeps MDD in 6.9312–7.5831 pp

## Adjudicability

444 of 444 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 444}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-pmars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| crack-7z-hash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| dna-assembly | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mteb-retrieve | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| path-tracing | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-alpine-ssh | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-startup | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| rstan-to-pystan | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sanitize-git-repo | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| adaptive-rejection-sampler | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| bn-fit-modify | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| build-cython-ext | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| build-pov-ray | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| caffe-cifar-10 | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| chess-best-move | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
