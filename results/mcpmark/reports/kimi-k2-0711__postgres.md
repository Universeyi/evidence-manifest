# Noise floor — MCPMark kimi-k2-0711__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 81, 'error': 3}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 11 | 52.381 |
| 2 | 19 | 9 | 47.3684 |
| 3 | 21 | 7 | 33.3333 |
| 4 | 20 | 7 | 35.0 |

Complete rounds: mean 42.0207 %, sd 9.3219 pp, observed range 19.0477 pp.

## Headline

- single-run sd **6.456 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **17.8948 pp** before the gap is outside noise; 25.5789 pp for 80% power
- 9 of 21 tasks flipped; mean flip rate 0.2302 (max possible at n=4: 0.6667)
- re-run (plugin) sd 6.456 pp, (posterior) 8.2384 pp; bootstrap precision of this estimate 3.2208 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 14.2252–18.1279 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [3946.0, 3762.0, 3848.0, 3981.0]
strongest single step: after round 2 (3854.0 → 3914.5, 1.57%, variance explained 0.1244). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| lego__database_security_policies | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| security__user_permission_audit | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| dvdrental__customer_analysis_fix | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| employees__employee_project_tracking | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| employees__executive_dashboard_automation | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| employees__management_structure_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| lego__transactional_inventory_transfer | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| sports__baseball_player_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| sports__team_roster_management | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
