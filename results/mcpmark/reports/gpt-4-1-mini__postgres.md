# Noise floor — MCPMark gpt-4-1-mini__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 84}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 2 | 9.5238 |
| 2 | 21 | 2 | 9.5238 |
| 3 | 21 | 3 | 14.2857 |
| 4 | 21 | 1 | 4.7619 |

Complete rounds: mean 9.5238 %, sd 3.8881 pp, observed range 9.5238 pp.

## Headline

- single-run sd **2.9557 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.1926 pp** before the gap is outside noise; 11.7106 pp for 80% power
- 2 of 21 tasks flipped; mean flip rate 0.0476 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.9557 pp, (posterior) 6.9167 pp; bootstrap precision of this estimate 1.4709 pp
- leave-one-round-out keeps MDD in 6.2133–8.8681 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [1117.0, 914.0, 1226.0, 906.0]
strongest single step: after round 2 (1015.5 → 1066.0, 4.97%, variance explained 0.0343). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| chinook__customer_data_migration | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| vectors__dba_vector_analysis | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
