# Noise floor — MCPMark o3__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 84}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 8 | 38.0952 |
| 2 | 21 | 7 | 33.3333 |
| 3 | 21 | 9 | 42.8571 |
| 4 | 21 | 7 | 33.3333 |

Complete rounds: mean 36.9047 %, sd 4.5592 pp, observed range 9.5238 pp.

## Headline

- single-run sd **7.0344 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **19.498 pp** before the gap is outside noise; 27.8706 pp for 80% power
- 11 of 21 tasks flipped; mean flip rate 0.2778 (max possible at n=4: 0.6667)
- re-run (plugin) sd 7.0344 pp, (posterior) 8.7214 pp; bootstrap precision of this estimate 3.5241 pp
- leave-one-round-out keeps MDD in 16.4371–20.5809 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [3832.0, 4039.0, 4505.0, 4491.0]
strongest single step: after round 2 (3935.5 → 4498.0, 14.29%, variance explained 0.9363). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| employees__management_structure_analysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| lego__database_security_policies | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| chinook__employee_hierarchy_management | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| dvdrental__customer_analysis_fix | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| dvdrental__customer_analytics_optimization | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| dvdrental__film_inventory_management | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| employees__employee_demographics_report | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| employees__employee_performance_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| employees__executive_dashboard_automation | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| security__rls_business_access | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| vectors__dba_vector_analysis | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
