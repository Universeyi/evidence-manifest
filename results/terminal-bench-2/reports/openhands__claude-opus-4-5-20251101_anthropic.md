# Noise floor — terminal-bench 2.0 openhands__claude-opus-4-5-20251101_anthropic

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 49 | 55.0562 |
| 2 | 89 | 49 | 55.0562 |
| 3 | 89 | 41 | 46.0674 |
| 4 | 89 | 51 | 57.3034 |
| 5 | 89 | 41 | 46.0674 |

Complete rounds: mean 51.9101 %, sd 5.412 pp, observed range 11.236 pp.

## Headline

- single-run sd **2.9711 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.2353 pp** before the gap is outside noise; 11.7716 pp for 80% power
- 37 of 89 tasks flipped; mean flip rate 0.1933 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.9711 pp, (posterior) 3.8099 pp; bootstrap precision of this estimate 1.3193 pp
- leave-one-round-out keeps MDD in 7.6862–8.2456 pp

## Adjudicability

7 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 438, 'none': 7}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-pmars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| circuit-fibsqrt | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| configure-git-webserver | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-moves-from-video | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| feal-differential-cryptanalysis | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| feal-linear-cryptanalysis | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| largest-eigenval | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-alpine-ssh | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sanitize-git-repo | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| bn-fit-modify | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| break-filter-js-from-html | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| db-wal-recovery | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
