# Noise floor — MCPMark k2-0905__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 82, 'error': 2}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 11 | 52.381 |
| 2 | 21 | 11 | 52.381 |
| 3 | 20 | 9 | 45.0 |
| 4 | 20 | 9 | 45.0 |

Complete rounds: mean 48.6905 %, sd 4.2614 pp, observed range 7.381 pp.

## Headline

- single-run sd **5.8491 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **16.2126 pp** before the gap is outside noise; 23.1744 pp for 80% power
- 7 of 21 tasks flipped; mean flip rate 0.1905 (max possible at n=4: 0.6667)
- re-run (plugin) sd 5.8491 pp, (posterior) 8.116 pp; bootstrap precision of this estimate 2.9106 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 14.0434–16.7425 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [4053.0, 4222.0, 3864.0, 3698.0]
strongest single step: after round 2 (4137.5 → 3781.0, -8.62%, variance explained 0.8192). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| chinook__customer_data_migration | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| dvdrental__customer_analysis_fix | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| employees__management_structure_analysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| employees__employee_performance_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| employees__executive_dashboard_automation | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| lego__database_security_policies | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| vectors__dba_vector_analysis | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
