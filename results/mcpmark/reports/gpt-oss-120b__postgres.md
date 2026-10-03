# Noise floor — MCPMark gpt-oss-120b__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 79, 'error': 5}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 1 | 4.7619 |
| 2 | 21 | 2 | 9.5238 |
| 3 | 18 | 2 | 11.1111 |
| 4 | 19 | 1 | 5.2632 |

Complete rounds: mean 7.665 %, sd 3.1373 pp, observed range 6.3492 pp.

## Headline

- single-run sd **4.8827 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **13.5339 pp** before the gap is outside noise; 19.3455 pp for 80% power
- 5 of 21 tasks flipped; mean flip rate 0.1349 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.8827 pp, (posterior) 7.6438 pp; bootstrap precision of this estimate 2.5337 pp
- leave-one-round-out keeps MDD in 12.4986–12.7894 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [695.0, 869.0, 1142.0, 406.0]
strongest single step: after round 2 (782.0 → 774.0, -1.02%, variance explained 0.0002). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| employees__management_structure_analysis | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| lego__database_security_policies | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| dvdrental__customer_analytics_optimization | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| employees__employee_performance_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| sports__participant_report_optimization | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
