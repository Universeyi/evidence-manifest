# Noise floor — MCPMark deepseek-chat__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'error': 4, 'completed': 79, 'budget_exhausted': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 20 | 8 | 40.0 |
| 2 | 20 | 7 | 35.0 |
| 3 | 20 | 11 | 55.0 |
| 4 | 20 | 10 | 50.0 |

Complete rounds: mean 45.0 %, sd 9.1287 pp, observed range 20.0 pp.

## Headline

- single-run sd **5.8669 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **16.2619 pp** before the gap is outside noise; 23.2449 pp for 80% power
- 7 of 20 tasks flipped; mean flip rate 0.1833 (max possible at n=4: 0.6667)
- re-run (plugin) sd 5.8669 pp, (posterior) 8.091 pp; bootstrap precision of this estimate 2.9594 pp
- leave-one-round-out keeps MDD in 12.9726–17.2725 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [3990.0, 4067.0, 4060.0, 3913.0]
strongest single step: after round 2 (4028.5 → 3986.5, -1.04%, variance explained 0.1136). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| employees__employee_demographics_report | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| employees__management_structure_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| lego__consistency_enforcement | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| lego__database_security_policies | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| lego__transactional_inventory_transfer | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| sports__baseball_player_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| vectors__dba_vector_analysis | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
