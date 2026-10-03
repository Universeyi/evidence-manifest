# Noise floor — terminal-bench 2.0 mini-swe-agent__gpt-5-mini_openai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 22 | 24.7191 |
| 2 | 89 | 23 | 25.8427 |
| 3 | 89 | 19 | 21.3483 |
| 4 | 89 | 16 | 17.9775 |
| 5 | 89 | 19 | 21.3483 |

Complete rounds: mean 22.2472 %, sd 3.1179 pp, observed range 7.8652 pp.

## Headline

- single-run sd **2.6709 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.4032 pp** before the gap is outside noise; 10.5822 pp for 80% power
- 30 of 89 tasks flipped; mean flip rate 0.1596 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.6709 pp, (posterior) 3.6393 pp; bootstrap precision of this estimate 1.191 pp
- leave-one-round-out keeps MDD in 7.049–7.3439 pp

## Adjudicability

11 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 434, 'none': 11}.

## Drift screen

series (median completion tokens per round, {'run_total': 433}): [11632.0, 10594.0, 12413.0, 14575.0, 13230.5]
strongest single step: after round 3 (11546.333 → 13902.75, 20.41%, variance explained 0.7217). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-pmars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| configure-git-webserver | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| distribution-search | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| feal-linear-cryptanalysis | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| git-leak-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| kv-store-grpc | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| large-scale-text-editing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| modernize-scientific-stack | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| nginx-request-logging | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-startup | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| adaptive-rejection-sampler | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| bn-fit-modify | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| cancel-async-tasks | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| cobol-modernization | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
