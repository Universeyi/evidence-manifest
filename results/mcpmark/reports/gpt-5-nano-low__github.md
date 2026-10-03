# Noise floor — MCPMark gpt-5-nano-low__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 91, 'budget_exhausted': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 23 | 0 | 0.0 |
| 2 | 23 | 0 | 0.0 |
| 3 | 23 | 0 | 0.0 |
| 4 | 23 | 0 | 0.0 |

Complete rounds: mean 0.0 %, sd 0.0 pp, observed range 0.0 pp.

## Headline

- single-run sd **0.0 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **0.0 pp** before the gap is outside noise; 0.0 pp for 80% power
- 0 of 23 tasks flipped; mean flip rate 0.0 (max possible at n=4: 0.6667)
- re-run (plugin) sd 0.0 pp, (posterior) 6.2498 pp; bootstrap precision of this estimate 0.0 pp
- leave-one-round-out keeps MDD in 0.0–0.0 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [3346.0, 2925.0, 2723.0, 3533.0]
strongest single step: after round 2 (3135.5 → 3128.0, -0.24%, variance explained 0.0001). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
