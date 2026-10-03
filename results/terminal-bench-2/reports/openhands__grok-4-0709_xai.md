# Noise floor — terminal-bench 2.0 openhands__grok-4-0709_xai

444 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 444}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 27 | 30.3371 |
| 2 | 89 | 24 | 26.9663 |
| 3 | 89 | 23 | 25.8427 |
| 4 | 89 | 25 | 28.0899 |
| 5 (partial) | 88 | 22 | 25.0 |

Complete rounds: mean 27.809 %, sd 1.9189 pp, observed range 4.4944 pp.

## Headline

- single-run sd **3.1004 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.5937 pp** before the gap is outside noise; 12.2839 pp for 80% power
- 38 of 89 tasks flipped; mean flip rate 0.2157 (max possible at n=5: 0.6)
- re-run (plugin) sd 3.1004 pp, (posterior) 3.9164 pp; bootstrap precision of this estimate 1.3906 pp
- leave-one-round-out keeps MDD in 7.8631–8.599 pp

## Adjudicability

17 of 444 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 427, 'none': 17}.

## Drift screen

series (median completion tokens per round, {'run_total': 416}): [1614.0, 1895.0, 1697.0, 1775.0, 1889.0]
strongest single step: after round 3 (1735.333 → 1832.0, 5.57%, variance explained 0.1888). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| cobol-modernization | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| code-from-image | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| crack-7z-hash | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| custom-memory-heap-crash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-differential-cryptanalysis | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| fix-code-vulnerability | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| fix-git | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-ocaml-gc | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| kv-store-grpc | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| large-scale-text-editing | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mcmc-sampling-stan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| prove-plus-comm | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pypi-server | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
