# Noise floor — terminal-bench 2.0 openhands__gpt-5_openai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 41 | 46.0674 |
| 2 | 89 | 40 | 44.9438 |
| 3 | 89 | 42 | 47.191 |
| 4 | 89 | 39 | 43.8202 |
| 5 | 89 | 33 | 37.0787 |

Complete rounds: mean 43.8202 %, sd 3.9725 pp, observed range 10.1123 pp.

## Headline

- single-run sd **3.0435 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.436 pp** before the gap is outside noise; 12.0585 pp for 80% power
- 38 of 89 tasks flipped; mean flip rate 0.2067 (max possible at n=5: 0.6)
- re-run (plugin) sd 3.0435 pp, (posterior) 3.9148 pp; bootstrap precision of this estimate 1.3736 pp
- leave-one-round-out keeps MDD in 7.9507–8.3947 pp

## Adjudicability

9 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 436, 'none': 9}.

## Drift screen

series (median completion tokens per round, {'run_total': 434}): [34120.0, 31444.0, 33480.0, 34890.0, 33265.0]
strongest single step: after round 2 (32782.0 → 33878.333, 3.34%, variance explained 0.2192). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pmars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pov-ray | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| cancel-async-tasks | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| count-dataset-tokens | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-differential-cryptanalysis | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| kv-store-grpc | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| log-summary-date-ranges | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| model-extraction-relu-logits | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pypi-server | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-alpine-ssh | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-startup | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
