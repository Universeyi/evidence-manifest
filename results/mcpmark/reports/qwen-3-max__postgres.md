# Noise floor — MCPMark qwen-3-max__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 81, 'error': 3}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 9 | 42.8571 |
| 2 | 21 | 10 | 47.619 |
| 3 | 20 | 9 | 45.0 |
| 4 | 19 | 9 | 47.3684 |

Complete rounds: mean 45.7111 %, sd 2.2389 pp, observed range 4.7619 pp.

## Headline

- single-run sd **2.892 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.0161 pp** before the gap is outside noise; 11.4582 pp for 80% power
- 2 of 21 tasks flipped; mean flip rate 0.0476 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.892 pp, (posterior) 7.1209 pp; bootstrap precision of this estimate 1.4552 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 6.2111–8.7309 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [1791.0, 1722.0, 1980.0, 1771.0]
strongest single step: after round 2 (1756.5 → 1875.5, 6.77%, variance explained 0.3689). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| employees__employee_retention_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| security__user_permission_audit | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
