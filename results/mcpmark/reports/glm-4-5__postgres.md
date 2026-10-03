# Noise floor — MCPMark glm-4-5__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 83, 'budget_exhausted': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 5 | 23.8095 |
| 2 | 21 | 2 | 9.5238 |
| 3 | 21 | 4 | 19.0476 |
| 4 | 21 | 1 | 4.7619 |

Complete rounds: mean 14.2857 %, sd 8.694 pp, observed range 19.0476 pp.

## Headline

- single-run sd **4.9823 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **13.81 pp** before the gap is outside noise; 19.7401 pp for 80% power
- 5 of 21 tasks flipped; mean flip rate 0.1429 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.9823 pp, (posterior) 7.7605 pp; bootstrap precision of this estimate 2.4883 pp
- leave-one-round-out keeps MDD in 10.7455–13.884 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [5888.0, 3958.0, 5534.0, 3036.0]
strongest single step: after round 2 (4923.0 → 4285.0, -12.96%, variance explained 0.0755). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| dvdrental__film_inventory_management | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| lego__consistency_enforcement | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| vectors__dba_vector_analysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| chinook__employee_hierarchy_management | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| sports__participant_report_optimization | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
