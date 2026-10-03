# Noise floor — MCPMark gpt-5-nano-low__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 112}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 28 | 0 | 0.0 |
| 2 | 28 | 0 | 0.0 |
| 3 | 28 | 0 | 0.0 |
| 4 | 28 | 0 | 0.0 |

Complete rounds: mean 0.0 %, sd 0.0 pp, observed range 0.0 pp.

## Headline

- single-run sd **0.0 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **0.0 pp** before the gap is outside noise; 0.0 pp for 80% power
- 0 of 28 tasks flipped; mean flip rate 0.0 (max possible at n=4: 0.6667)
- re-run (plugin) sd 0.0 pp, (posterior) 5.6924 pp; bootstrap precision of this estimate 0.0 pp
- leave-one-round-out keeps MDD in 0.0–0.0 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [29754.5, 1647.5, 1543.5, 1738.0]
strongest single step: after round 2 (15701.0 → 1640.75, -89.55%, variance explained 0.3335). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
