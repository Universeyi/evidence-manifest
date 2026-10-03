# Noise floor — terminal-bench 2.0 sage__gemini-3-pro-preview_Google

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 57 | 64.0449 |
| 2 | 89 | 58 | 65.1685 |
| 3 | 89 | 61 | 68.5393 |
| 4 | 89 | 57 | 64.0449 |
| 5 | 89 | 57 | 64.0449 |

Complete rounds: mean 65.1685 %, sd 1.9461 pp, observed range 4.4944 pp.

## Headline

- single-run sd **2.0995 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **5.8194 pp** before the gap is outside noise; 8.3183 pp for 80% power
- 20 of 89 tasks flipped; mean flip rate 0.0989 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.0995 pp, (posterior) 3.4081 pp; bootstrap precision of this estimate 0.937 pp
- leave-one-round-out keeps MDD in 5.1933–6.1204 pp

## Adjudicability

445 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 445}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| break-filter-js-from-html | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| circuit-fibsqrt | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sparql-university | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| winning-avg-corewars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| adaptive-rejection-sampler | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| dna-assembly | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| gcode-to-text | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| large-scale-text-editing | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| largest-eigenval | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| log-summary-date-ranges | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| merge-diff-arc-agi-task | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| mteb-leaderboard | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| pytorch-model-cli | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| query-optimize | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| raman-fitting | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
