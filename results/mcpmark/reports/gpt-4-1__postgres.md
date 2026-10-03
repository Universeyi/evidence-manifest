# Noise floor — MCPMark gpt-4-1__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 84}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 1 | 4.7619 |
| 2 | 21 | 1 | 4.7619 |
| 3 | 21 | 1 | 4.7619 |
| 4 | 21 | 1 | 4.7619 |

Complete rounds: mean 4.7619 %, sd 0.0 pp, observed range 0.0 pp.

## Headline

- single-run sd **0.0 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **0.0 pp** before the gap is outside noise; 0.0 pp for 80% power
- 0 of 21 tasks flipped; mean flip rate 0.0 (max possible at n=4: 0.6667)
- re-run (plugin) sd 0.0 pp, (posterior) 6.5908 pp; bootstrap precision of this estimate 0.0 pp
- leave-one-round-out keeps MDD in 0.0–0.0 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [889.0, 982.0, 772.0, 868.0]
strongest single step: after round 2 (935.5 → 820.0, -12.35%, variance explained 0.5989). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
