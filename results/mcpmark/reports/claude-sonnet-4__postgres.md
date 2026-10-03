# Noise floor — MCPMark claude-sonnet-4__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 83, 'budget_exhausted': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 10 | 47.619 |
| 2 | 21 | 12 | 57.1429 |
| 3 | 21 | 13 | 61.9048 |
| 4 | 21 | 10 | 47.619 |

Complete rounds: mean 53.5714 %, sd 7.1429 pp, observed range 14.2858 pp.

## Headline

- single-run sd **5.7403 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **15.911 pp** before the gap is outside noise; 22.7433 pp for 80% power
- 7 of 21 tasks flipped; mean flip rate 0.1825 (max possible at n=4: 0.6667)
- re-run (plugin) sd 5.7403 pp, (posterior) 7.8692 pp; bootstrap precision of this estimate 2.8373 pp
- leave-one-round-out keeps MDD in 10.8583–16.6985 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [5951.0, 5836.0, 6366.0, 6010.0]
strongest single step: after round 2 (5893.5 → 6188.0, 5.0%, variance explained 0.5534). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| lego__transactional_inventory_transfer | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| sports__baseball_player_analysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| chinook__customer_data_migration | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| employees__employee_performance_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| employees__employee_project_tracking | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| employees__executive_dashboard_automation | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| security__rls_business_access | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
