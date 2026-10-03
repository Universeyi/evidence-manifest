# Noise floor — MCPMark gemini-2-5-pro__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 84}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 7 | 33.3333 |
| 2 | 21 | 5 | 23.8095 |
| 3 | 21 | 3 | 14.2857 |
| 4 | 21 | 7 | 33.3333 |

Complete rounds: mean 26.1905 %, sd 9.1183 pp, observed range 19.0476 pp.

## Headline

- single-run sd **6.0746 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **16.8376 pp** before the gap is outside noise; 24.0678 pp for 80% power
- 8 of 21 tasks flipped; mean flip rate 0.2064 (max possible at n=4: 0.6667)
- re-run (plugin) sd 6.0746 pp, (posterior) 8.1265 pp; bootstrap precision of this estimate 3.058 pp
- leave-one-round-out keeps MDD in 14.0151–17.7975 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [7613.0, 8779.0, 5453.0, 6866.0]
strongest single step: after round 2 (8196.0 → 6159.5, -24.85%, variance explained 0.7119). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| chinook__employee_hierarchy_management | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| lego__transactional_inventory_transfer | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| chinook__customer_data_migration | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| chinook__sales_and_music_charts | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| employees__management_structure_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| lego__consistency_enforcement | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| lego__database_security_policies | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| vectors__dba_vector_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
