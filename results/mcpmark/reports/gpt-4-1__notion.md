# Noise floor — MCPMark gpt-4-1__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 112}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 28 | 1 | 3.5714 |
| 2 | 28 | 2 | 7.1429 |
| 3 | 28 | 2 | 7.1429 |
| 4 | 28 | 2 | 7.1429 |

Complete rounds: mean 6.25 %, sd 1.7857 pp, observed range 3.5715 pp.

## Headline

- single-run sd **3.2329 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.961 pp** before the gap is outside noise; 12.8089 pp for 80% power
- 4 of 28 tasks flipped; mean flip rate 0.0774 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.2329 pp, (posterior) 6.3338 pp; bootstrap precision of this estimate 1.5952 pp
- leave-one-round-out keeps MDD in 8.0995–9.3831 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [1289.5, 1247.0, 1321.5, 985.0]
strongest single step: after round 2 (1268.25 → 1153.25, -9.07%, variance explained 0.1869). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| company_in_a_box__goals_restructure | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| it_trouble_shooting_hub__asset_retirement_migration | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| japan_travel_planner__remove_osaka_itinerary | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| toronto_guide__weekend_adventure_planner | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
