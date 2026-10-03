# Noise floor — MCPMark grok-code-fast-1__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 90, 'error': 2}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 22 | 4 | 18.1818 |
| 2 | 23 | 1 | 4.3478 |
| 3 | 22 | 1 | 4.5455 |
| 4 | 23 | 2 | 8.6957 |

Complete rounds: mean 8.9427 %, sd 6.4774 pp, observed range 13.834 pp.

## Headline

- single-run sd **3.4039 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **9.435 pp** before the gap is outside noise; 13.4864 pp for 80% power
- 3 of 23 tasks flipped; mean flip rate 0.0725 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.4039 pp, (posterior) 6.9446 pp; bootstrap precision of this estimate 1.7291 pp
- leave-one-round-out keeps MDD in 5.6792–9.7967 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [5018.0, 6169.0, 6145.0, 5688.0]
strongest single step: after round 2 (5593.5 → 5916.5, 5.77%, variance explained 0.1198). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| claude-code__critical_issue_hotfix_workflow | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| claude-code__automated_changelog_generation | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| harmony__issue_tagging_pr_closure | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
