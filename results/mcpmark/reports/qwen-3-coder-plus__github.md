# Noise floor — MCPMark qwen-3-coder-plus__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 78, 'budget_exhausted': 1, 'error': 13}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 20 | 3 | 15.0 |
| 2 | 19 | 6 | 31.5789 |
| 3 | 19 | 3 | 15.7895 |
| 4 | 21 | 6 | 28.5714 |

Complete rounds: mean 22.735 %, sd 8.5703 pp, observed range 16.5789 pp.

## Headline

- single-run sd **4.8818 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **13.5314 pp** before the gap is outside noise; 19.3419 pp for 80% power
- 5 of 20 tasks flipped; mean flip rate 0.1417 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.8818 pp, (posterior) 7.8114 pp; bootstrap precision of this estimate 2.4837 pp
- **not reportable:** a task has only 1 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 10.7729–14.2332 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [2250.0, 2435.0, 2521.0, 2517.0]
strongest single step: after round 2 (2342.5 → 2519.0, 7.53%, variance explained 0.6453). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| claude-code__critical_issue_hotfix_workflow | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| harmony__release_management_workflow | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| build_your_own_x__find_rag_commit | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| harmony__fix_conflict | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| missing-semester__find_legacy_name | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
