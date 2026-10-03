# Noise floor — MCPMark glm-4-5__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 88, 'budget_exhausted': 3, 'error': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 23 | 5 | 21.7391 |
| 2 | 23 | 6 | 26.087 |
| 3 | 23 | 3 | 13.0435 |
| 4 | 22 | 7 | 31.8182 |

Complete rounds: mean 23.1719 %, sd 7.914 pp, observed range 18.7747 pp.

## Headline

- single-run sd **4.4656 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **12.3778 pp** before the gap is outside noise; 17.6929 pp for 80% power
- 5 of 23 tasks flipped; mean flip rate 0.1232 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.4656 pp, (posterior) 7.2958 pp; bootstrap precision of this estimate 2.2148 pp
- leave-one-round-out keeps MDD in 11.2425–12.553 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [3047.0, 3488.0, 2637.0, 2947.0]
strongest single step: after round 2 (3267.5 → 2792.0, -14.55%, variance explained 0.6088). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| harmony__fix_conflict | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| harmony__issue_tagging_pr_closure | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| build_your_own_x__find_rag_commit | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| claude-code__critical_issue_hotfix_workflow | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| harmony__issue_pr_commit_workflow | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
