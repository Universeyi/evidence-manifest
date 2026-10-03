# Noise floor — MCPMark grok-4__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 84}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 12 | 57.1429 |
| 2 | 21 | 15 | 71.4286 |
| 3 | 21 | 11 | 52.381 |
| 4 | 21 | 11 | 52.381 |

Complete rounds: mean 58.3334 %, sd 9.0141 pp, observed range 19.0476 pp.

## Headline

- single-run sd **6.4457 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **17.8662 pp** before the gap is outside noise; 25.5381 pp for 80% power
- 9 of 21 tasks flipped; mean flip rate 0.2302 (max possible at n=4: 0.6667)
- re-run (plugin) sd 6.4457 pp, (posterior) 8.3593 pp; bootstrap precision of this estimate 3.2149 pp
- leave-one-round-out keeps MDD in 16.3903–17.7484 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [7588.0, 7424.0, 6306.0, 6751.0]
strongest single step: after round 2 (7506.0 → 6528.5, -13.02%, variance explained 0.8947). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| employees__employee_performance_analysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| employees__management_structure_analysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| chinook__sales_and_music_charts | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| dvdrental__customer_analysis_fix | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| dvdrental__customer_analytics_optimization | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| employees__employee_demographics_report | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| security__user_permission_audit | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| sports__team_roster_management | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| vectors__dba_vector_analysis | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
