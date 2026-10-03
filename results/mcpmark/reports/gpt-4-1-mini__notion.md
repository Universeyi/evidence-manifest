# Noise floor — MCPMark gpt-4-1-mini__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 112}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 28 | 1 | 3.5714 |
| 2 | 28 | 0 | 0.0 |
| 3 | 28 | 0 | 0.0 |
| 4 | 28 | 1 | 3.5714 |

Complete rounds: mean 1.7857 %, sd 2.0619 pp, observed range 3.5714 pp.

## Headline

- single-run sd **1.7858 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **4.9499 pp** before the gap is outside noise; 7.0754 pp for 80% power
- 1 of 28 tasks flipped; mean flip rate 0.0238 (max possible at n=4: 0.6667)
- re-run (plugin) sd 1.7858 pp, (posterior) 5.8763 pp; bootstrap precision of this estimate 0.8921 pp
- leave-one-round-out keeps MDD in 4.6533–4.6816 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [1588.5, 1143.5, 443.5, 1111.5]
strongest single step: after round 2 (1366.0 → 777.5, -43.08%, variance explained 0.5181). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| it_trouble_shooting_hub__asset_retirement_migration | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
