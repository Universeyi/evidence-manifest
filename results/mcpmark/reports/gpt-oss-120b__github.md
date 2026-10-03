# Noise floor — MCPMark gpt-oss-120b__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 85, 'error': 7}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 0 | 0.0 |
| 2 | 21 | 1 | 4.7619 |
| 3 | 22 | 2 | 9.0909 |
| 4 | 21 | 1 | 4.7619 |

Complete rounds: mean 4.6537 %, sd 3.7134 pp, observed range 9.0909 pp.

## Headline

- single-run sd **2.6375 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.3106 pp** before the gap is outside noise; 10.4499 pp for 80% power
- 2 of 22 tasks flipped; mean flip rate 0.0455 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.6375 pp, (posterior) 6.8793 pp; bootstrap precision of this estimate 1.3333 pp
- **not reportable:** a task has only 1 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 5.6792–7.9778 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [950.0, 754.0, 860.0, 1137.0]
strongest single step: after round 2 (852.0 → 998.5, 17.19%, variance explained 0.2716). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| claude-code__critical_issue_hotfix_workflow | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| easyr1__advanced_branch_strategy | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
