# Noise floor — terminal-bench 2.0 openhands__gpt-5-mini_openai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 27 | 30.3371 |
| 2 | 89 | 27 | 30.3371 |
| 3 | 89 | 27 | 30.3371 |
| 4 | 89 | 23 | 25.8427 |
| 5 | 89 | 26 | 29.2135 |

Complete rounds: mean 29.2135 %, sd 1.9461 pp, observed range 4.4944 pp.

## Headline

- single-run sd **2.7632 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.6591 pp** before the gap is outside noise; 10.9479 pp for 80% power
- 31 of 89 tasks flipped; mean flip rate 0.1753 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.7632 pp, (posterior) 3.7413 pp; bootstrap precision of this estimate 1.2641 pp
- leave-one-round-out keeps MDD in 7.3012–7.8256 pp

## Adjudicability

16 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 429, 'none': 16}.

## Drift screen

series (median completion tokens per round, {'run_total': 428}): [25246.0, 25506.0, 26951.0, 25584.0, 21616.0]
strongest single step: after round 3 (25901.0 → 23600.0, -8.88%, variance explained 0.3993). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| bn-fit-modify | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pmars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| code-from-image | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| count-dataset-tokens | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-linear-cryptanalysis | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| headless-terminal | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| hf-model-inference | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| large-scale-text-editing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| nginx-request-logging | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| portfolio-optimization | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-startup | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| query-optimize | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
