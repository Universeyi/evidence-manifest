# Noise floor — terminal-bench 2.0 mux__claude-opus-4-6_anthropic

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 61 | 68.5393 |
| 2 | 89 | 60 | 67.4157 |
| 3 | 89 | 57 | 64.0449 |
| 4 | 89 | 60 | 67.4157 |
| 5 | 89 | 58 | 65.1685 |

Complete rounds: mean 66.5168 %, sd 1.8463 pp, observed range 4.4944 pp.

## Headline

- single-run sd **2.5881 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.1737 pp** before the gap is outside noise; 10.2542 pp for 80% power
- 27 of 89 tasks flipped; mean flip rate 0.1483 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.5881 pp, (posterior) 3.6513 pp; bootstrap precision of this estimate 1.1394 pp
- leave-one-round-out keeps MDD in 6.4608–7.2929 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| cancel-async-tasks | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| count-dataset-tokens | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-moves-from-video | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| gcode-to-text | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| largest-eigenval | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| model-extraction-relu-logits | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mteb-leaderboard | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| openssl-selfsigned-cert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| protein-assembly | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| query-optimize | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sqlite-with-gcov | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| write-compressor | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pmars | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| build-pov-ray | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| circuit-fibsqrt | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
