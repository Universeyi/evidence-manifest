# Noise floor — MCPMark qwen-3-coder-plus__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 84}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 12 | 57.1429 |
| 2 | 21 | 9 | 42.8571 |
| 3 | 21 | 10 | 47.619 |
| 4 | 21 | 9 | 42.8571 |

Complete rounds: mean 47.619 %, sd 6.7344 pp, observed range 14.2858 pp.

## Headline

- single-run sd **4.7673 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **13.214 pp** before the gap is outside noise; 18.8882 pp for 80% power
- 5 of 21 tasks flipped; mean flip rate 0.127 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.7673 pp, (posterior) 7.5856 pp; bootstrap precision of this estimate 2.3705 pp
- leave-one-round-out keeps MDD in 8.7509–13.9278 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [3196.0, 3467.0, 3541.0, 3365.0]
strongest single step: after round 2 (3331.5 → 3453.0, 3.65%, variance explained 0.2204). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| lego__database_security_policies | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| employees__employee_performance_analysis | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| employees__management_structure_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| lego__transactional_inventory_transfer | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| sports__team_roster_management | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
