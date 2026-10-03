# Noise floor — MCPMark deepseek-chat__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'budget_exhausted': 38, 'completed': 53, 'error': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 23 | 2 | 8.6957 |
| 2 | 23 | 2 | 8.6957 |
| 3 | 23 | 3 | 13.0435 |
| 4 | 22 | 2 | 9.0909 |

Complete rounds: mean 9.8815 %, sd 2.1162 pp, observed range 4.3478 pp.

## Headline

- single-run sd **1.8848 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **5.2243 pp** before the gap is outside noise; 7.4677 pp for 80% power
- 1 of 23 tasks flipped; mean flip rate 0.0217 (max possible at n=4: 0.6667)
- re-run (plugin) sd 1.8848 pp, (posterior) 6.4102 pp; bootstrap precision of this estimate 0.9521 pp
- leave-one-round-out keeps MDD in 0.0–5.6792 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [1296.0, 2121.0, 1853.0, 1657.0]
strongest single step: after round 2 (1708.5 → 1755.0, 2.72%, variance explained 0.006). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| claude-code__critical_issue_hotfix_workflow | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
