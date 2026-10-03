# Noise floor — MCPMark gpt-5-low__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 84}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 16 | 76.1905 |
| 2 | 21 | 16 | 76.1905 |
| 3 | 21 | 14 | 66.6667 |
| 4 | 21 | 16 | 76.1905 |

Complete rounds: mean 73.8096 %, sd 4.7619 pp, observed range 9.5238 pp.

## Headline

- single-run sd **7.3769 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **20.4473 pp** before the gap is outside noise; 29.2276 pp for 80% power
- 12 of 21 tasks flipped; mean flip rate 0.3016 (max possible at n=4: 0.6667)
- re-run (plugin) sd 7.3769 pp, (posterior) 8.8335 pp; bootstrap precision of this estimate 3.6631 pp
- leave-one-round-out keeps MDD in 16.7545–21.7617 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [14776.0, 17779.0, 14209.0, 14264.0]
strongest single step: after round 2 (16277.5 → 14236.5, -12.54%, variance explained 0.4801). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| employees__management_structure_analysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| sports__baseball_player_analysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| dvdrental__customer_analysis_fix | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| dvdrental__customer_analytics_optimization | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| employees__employee_demographics_report | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| employees__employee_performance_analysis | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| employees__employee_retention_analysis | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| employees__executive_dashboard_automation | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| lego__consistency_enforcement | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| lego__transactional_inventory_transfer | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| security__rls_business_access | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| sports__team_roster_management | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
