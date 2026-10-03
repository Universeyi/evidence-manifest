# Noise floor — MCPMark k2-0905__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 82, 'budget_exhausted': 1, 'error': 9}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 20 | 4 | 20.0 |
| 2 | 21 | 3 | 14.2857 |
| 3 | 20 | 4 | 20.0 |
| 4 | 22 | 4 | 18.1818 |

Complete rounds: mean 18.1169 %, sd 2.6941 pp, observed range 5.7143 pp.

## Headline

- single-run sd **4.0779 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **11.3032 pp** before the gap is outside noise; 16.1568 pp for 80% power
- 4 of 21 tasks flipped; mean flip rate 0.1032 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.0779 pp, (posterior) 7.2087 pp; bootstrap precision of this estimate 2.032 pp
- **not reportable:** a task has only 1 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 8.3187–12.4579 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [2691.0, 2749.0, 2777.0, 2757.0]
strongest single step: after round 2 (2720.0 → 2767.0, 1.73%, variance explained 0.54). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| missing-semester__find_legacy_name | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| build_your_own_x__find_rag_commit | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| easyr1__performance_regression_investigation | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| harmony__fix_conflict | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
