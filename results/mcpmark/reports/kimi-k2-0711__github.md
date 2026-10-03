# Noise floor — MCPMark kimi-k2-0711__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'error': 40, 'completed': 52}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 14 | 3 | 21.4286 |
| 2 | 12 | 2 | 16.6667 |
| 3 | 12 | 2 | 16.6667 |
| 4 | 14 | 3 | 21.4286 |

Complete rounds: mean 19.0476 %, sd 2.7493 pp, observed range 4.7619 pp.

## Headline

- single-run sd **3.8265 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **10.6063 pp** before the gap is outside noise; 15.1607 pp for 80% power
- 2 of 14 tasks flipped; mean flip rate 0.0714 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.8265 pp, (posterior) 8.8804 pp; bootstrap precision of this estimate 1.921 pp
- **not reportable:** a task has only 1 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 8.1405–12.2514 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [1766.0, 1758.0, 1766.0, 2202.0]
strongest single step: after round 2 (1762.0 → 1984.0, 12.6%, variance explained 0.3414). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| claude-code__critical_issue_hotfix_workflow | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| easyr1__advanced_branch_strategy | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
