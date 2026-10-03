# Noise floor — MCPMark gemini-2-5-flash__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 83, 'error': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 4 | 19.0476 |
| 2 | 21 | 3 | 14.2857 |
| 3 | 20 | 1 | 5.0 |
| 4 | 21 | 1 | 4.7619 |

Complete rounds: mean 10.7738 %, sd 7.0774 pp, observed range 14.2857 pp.

## Headline

- single-run sd **4.2305 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **11.7261 pp** before the gap is outside noise; 16.7614 pp for 80% power
- 4 of 21 tasks flipped; mean flip rate 0.1032 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.2305 pp, (posterior) 7.3895 pp; bootstrap precision of this estimate 2.2295 pp
- leave-one-round-out keeps MDD in 9.0921–12.515 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [4903.0, 7291.0, 5087.0, 6423.0]
strongest single step: after round 2 (6097.0 → 5755.0, -5.61%, variance explained 0.0303). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| vectors__dba_vector_analysis | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| chinook__customer_data_migration | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| dvdrental__film_inventory_management | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| sports__participant_report_optimization | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
