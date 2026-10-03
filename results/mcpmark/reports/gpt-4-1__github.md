# Noise floor — MCPMark gpt-4-1__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 90, 'error': 2}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 23 | 2 | 8.6957 |
| 2 | 23 | 2 | 8.6957 |
| 3 | 22 | 2 | 9.0909 |
| 4 | 22 | 1 | 4.5455 |

Complete rounds: mean 7.7569 %, sd 2.1491 pp, observed range 4.5454 pp.

## Headline

- single-run sd **1.8551 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **5.142 pp** before the gap is outside noise; 7.35 pp for 80% power
- 1 of 23 tasks flipped; mean flip rate 0.0217 (max possible at n=4: 0.6667)
- re-run (plugin) sd 1.8551 pp, (posterior) 6.5476 pp; bootstrap precision of this estimate 0.9445 pp
- leave-one-round-out keeps MDD in 0.0–5.6279 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [1439.0, 1534.0, 1251.0, 1267.0]
strongest single step: after round 2 (1486.5 → 1259.0, -15.3%, variance explained 0.9177). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| easyr1__advanced_branch_strategy | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
