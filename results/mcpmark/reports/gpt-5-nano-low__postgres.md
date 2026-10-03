# Noise floor — MCPMark gpt-5-nano-low__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 84}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 2 | 9.5238 |
| 2 | 21 | 3 | 14.2857 |
| 3 | 21 | 1 | 4.7619 |
| 4 | 21 | 1 | 4.7619 |

Complete rounds: mean 8.3333 %, sd 4.5592 pp, observed range 9.5238 pp.

## Headline

- single-run sd **4.3059 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **11.9351 pp** before the gap is outside noise; 17.0601 pp for 80% power
- 4 of 21 tasks flipped; mean flip rate 0.1032 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.3059 pp, (posterior) 7.3219 pp; bootstrap precision of this estimate 2.1492 pp
- leave-one-round-out keeps MDD in 8.7506–12.4715 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [10748.0, 13692.0, 12564.0, 15500.0]
strongest single step: after round 2 (12220.0 → 14032.0, 14.83%, variance explained 0.2753). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| dvdrental__film_inventory_management | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| chinook__employee_hierarchy_management | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| chinook__sales_and_music_charts | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| vectors__dba_vector_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
