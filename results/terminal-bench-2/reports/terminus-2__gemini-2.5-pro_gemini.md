# Noise floor — terminal-bench 2.0 terminus-2__gemini-2.5-pro_gemini

442 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 442}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 21 | 23.5955 |
| 2 | 89 | 35 | 39.3258 |
| 3 | 89 | 28 | 31.4607 |
| 4 | 89 | 30 | 33.7079 |
| 5 (partial) | 86 | 31 | 36.0465 |

Complete rounds: mean 32.0225 %, sd 6.5194 pp, observed range 15.7303 pp.

## Headline

- single-run sd **3.0699 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.5092 pp** before the gap is outside noise; 12.1631 pp for 80% power
- 38 of 89 tasks flipped; mean flip rate 0.2101 (max possible at n=5: 0.6)
- re-run (plugin) sd 3.0699 pp, (posterior) 3.8951 pp; bootstrap precision of this estimate 1.3588 pp
- leave-one-round-out keeps MDD in 8.1535–8.4177 pp

## Adjudicability

0 of 442 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 442}.

## Drift screen

series (median completion tokens per round, {'run_total': 442}): [18919.0, 16461.0, 15468.0, 17599.0, 15693.5]
strongest single step: after round 2 (17690.0 → 16253.5, -8.12%, variance explained 0.3006). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| cancel-async-tasks | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| compile-compcert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| configure-git-webserver | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| crack-7z-hash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| distribution-search | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-code-vulnerability | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| large-scale-text-editing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mailman | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| openssl-selfsigned-cert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| overfull-hbox | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| polyglot-c-py | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| polyglot-rust-c | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pypi-server | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sam-cell-seg | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
