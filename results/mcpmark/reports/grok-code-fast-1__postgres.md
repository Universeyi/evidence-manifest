# Noise floor — MCPMark grok-code-fast-1__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 84}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 11 | 52.381 |
| 2 | 21 | 9 | 42.8571 |
| 3 | 21 | 11 | 52.381 |
| 4 | 21 | 9 | 42.8571 |

Complete rounds: mean 47.6191 %, sd 5.4986 pp, observed range 9.5239 pp.

## Headline

- single-run sd **5.8397 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **16.1865 pp** before the gap is outside noise; 23.1371 pp for 80% power
- 7 of 21 tasks flipped; mean flip rate 0.1905 (max possible at n=4: 0.6667)
- re-run (plugin) sd 5.8397 pp, (posterior) 8.0559 pp; bootstrap precision of this estimate 2.9159 pp
- leave-one-round-out keeps MDD in 14.029–16.4995 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [4364.0, 4943.0, 4132.0, 4482.0]
strongest single step: after round 2 (4653.5 → 4307.0, -7.45%, variance explained 0.3441). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| employees__management_structure_analysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| sports__baseball_player_analysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| sports__participant_report_optimization | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| employees__employee_demographics_report | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| lego__database_security_policies | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| lego__transactional_inventory_transfer | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| vectors__dba_vector_analysis | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
