# Noise floor — MCPMark grok-4__github

92 manifests, 23 tasks, rounds [1, 2, 3, 4]; outcomes {'error': 23, 'completed': 69}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 18 | 3 | 16.6667 |
| 2 | 15 | 2 | 13.3333 |
| 3 | 15 | 4 | 26.6667 |
| 4 | 21 | 4 | 19.0476 |

Complete rounds: mean 18.9286 %, sd 5.6662 pp, observed range 13.3334 pp.

## Headline

- single-run sd **3.7864 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **10.4952 pp** before the gap is outside noise; 15.0019 pp for 80% power
- 3 of 19 tasks flipped; mean flip rate 0.0965 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.7864 pp, (posterior) 7.8451 pp; bootstrap precision of this estimate 1.8998 pp
- **not reportable:** a task has only 1 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 9.2634–10.8408 pp

## Adjudicability

0 of 92 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 92}.

## Drift screen

series (median completion tokens per round, {'run_total': 92}): [1348.0, 1514.0, 1706.0, 1328.0]
strongest single step: after round 2 (1431.0 → 1517.0, 6.01%, variance explained 0.0799). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| harmony__release_management_workflow | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| mcpmark-cicd__linting_ci_workflow | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| easyr1__performance_regression_investigation | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
