# Noise floor — MCPMark gpt-4-1-mini__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 97, 'budget_exhausted': 3}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 25 | 0 | 0.0 |
| 2 | 25 | 0 | 0.0 |
| 3 | 25 | 0 | 0.0 |
| 4 | 25 | 0 | 0.0 |

Complete rounds: mean 0.0 %, sd 0.0 pp, observed range 0.0 pp.

## Headline

- single-run sd **0.0 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **0.0 pp** before the gap is outside noise; 0.0 pp for 80% power
- 0 of 25 tasks flipped; mean flip rate 0.0 (max possible at n=4: 0.6667)
- re-run (plugin) sd 0.0 pp, (posterior) 5.9986 pp; bootstrap precision of this estimate 0.0 pp
- leave-one-round-out keeps MDD in 0.0–0.0 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [2577.0, 2104.0, 2114.0, 2001.0]
strongest single step: after round 2 (2340.5 → 2057.5, -12.09%, variance explained 0.4038). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
