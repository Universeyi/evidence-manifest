# Noise floor — terminal-bench 2.0 final__claude-4.5-sonnet_anthropic

322 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 322}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 38 | 42.6966 |
| 2 (partial) | 87 | 37 | 42.5287 |
| 3 (partial) | 50 | 0 | 0.0 |
| 4 (partial) | 49 | 0 | 0.0 |
| 5 (partial) | 47 | 0 | 0.0 |

Complete rounds: mean 42.6966 %, sd 0.0 pp, observed range 0.0 pp.

## Headline

- single-run sd **0.0 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **0.0 pp** before the gap is outside noise; 0.0 pp for 80% power
- 0 of 87 tasks flipped; mean flip rate 0.0 (max possible at n=5: 0.6)
- re-run (plugin) sd 0.0 pp, (posterior) 3.456 pp; bootstrap precision of this estimate 0.0 pp
- **not reportable:** a task has only 1 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 0.0–0.0 pp

## Adjudicability

322 of 322 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 322}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
