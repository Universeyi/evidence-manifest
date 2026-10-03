# Noise floor — terminal-bench 2.0 mini-swe-agent__claude-sonnet-4-5-20250929_anthropic

442 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 442}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 39 | 43.8202 |
| 2 | 89 | 37 | 41.573 |
| 3 | 89 | 42 | 47.191 |
| 4 | 89 | 35 | 39.3258 |
| 5 (partial) | 86 | 35 | 40.6977 |

Complete rounds: mean 42.9775 %, sd 3.3552 pp, observed range 7.8652 pp.

## Headline

- single-run sd **2.8534 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.9091 pp** before the gap is outside noise; 11.3053 pp for 80% power
- 31 of 89 tasks flipped; mean flip rate 0.1809 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.8534 pp, (posterior) 3.7556 pp; bootstrap precision of this estimate 1.2806 pp
- leave-one-round-out keeps MDD in 7.0983–7.9024 pp

## Adjudicability

23 of 442 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 419, 'none': 23}.

## Drift screen

series (median completion tokens per round, {'run_total': 419}): [9046.0, 7929.0, 9365.5, 8271.5, 8210.5]
strongest single step: after round 3 (8780.167 → 8241.0, -6.14%, variance explained 0.2344). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| break-filter-js-from-html | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-cython-ext | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| compile-compcert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| count-dataset-tokens | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| crack-7z-hash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| distribution-search | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-elf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| feal-differential-cryptanalysis | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-ocaml-gc | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| largest-eigenval | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mailman | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| overfull-hbox | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| portfolio-optimization | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
