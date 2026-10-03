# Noise floor — MCPMark gpt-5-mini-low__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 84}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 3 | 14.2857 |
| 2 | 21 | 2 | 9.5238 |
| 3 | 21 | 3 | 14.2857 |
| 4 | 21 | 4 | 19.0476 |

Complete rounds: mean 14.2857 %, sd 3.8881 pp, observed range 9.5238 pp.

## Headline

- single-run sd **5.3598 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **14.8563 pp** before the gap is outside noise; 21.2357 pp for 80% power
- 6 of 21 tasks flipped; mean flip rate 0.1587 (max possible at n=4: 0.6667)
- re-run (plugin) sd 5.3598 pp, (posterior) 7.7855 pp; bootstrap precision of this estimate 2.6565 pp
- leave-one-round-out keeps MDD in 12.5189–15.3464 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [3756.0, 3753.0, 3731.0, 5609.0]
strongest single step: after round 2 (3754.5 → 4670.0, 24.38%, variance explained 0.3222). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| chinook__sales_and_music_charts | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| employees__employee_demographics_report | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| chinook__customer_data_migration | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| chinook__employee_hierarchy_management | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| security__user_permission_audit | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| sports__participant_report_optimization | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
