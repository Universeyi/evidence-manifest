# Noise floor — MCPMark gemini-2-5-flash__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 88, 'error': 3, 'budget_exhausted': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 22 | 4 | 18.1818 |
| 2 | 23 | 3 | 13.0435 |
| 3 | 21 | 3 | 14.2857 |
| 4 | 23 | 4 | 17.3913 |

Complete rounds: mean 15.7256 %, sd 2.4546 pp, observed range 5.1383 pp.

## Headline

- single-run sd **3.4456 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **9.5505 pp** before the gap is outside noise; 13.6516 pp for 80% power
- 3 of 23 tasks flipped; mean flip rate 0.0725 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.4456 pp, (posterior) 6.8956 pp; bootstrap precision of this estimate 1.7165 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 7.9845–9.9123 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [4366.0, 5854.0, 5787.0, 7656.0]
strongest single step: after round 2 (5110.0 → 6721.5, 31.54%, variance explained 0.4765). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| harmony__issue_pr_commit_workflow | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| claude-code__critical_issue_hotfix_workflow | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| missing-semester__find_salient_file | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
