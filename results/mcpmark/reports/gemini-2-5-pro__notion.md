# Noise floor — MCPMark gemini-2-5-pro__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 112}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 28 | 1 | 3.5714 |
| 2 | 28 | 2 | 7.1429 |
| 3 | 28 | 2 | 7.1429 |
| 4 | 28 | 0 | 0.0 |

Complete rounds: mean 4.4643 %, sd 3.4194 pp, observed range 7.1429 pp.

## Headline

- single-run sd **2.3724 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.5758 pp** before the gap is outside noise; 9.3995 pp for 80% power
- 2 of 28 tasks flipped; mean flip rate 0.0417 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.3724 pp, (posterior) 5.9221 pp; bootstrap precision of this estimate 1.1771 pp
- leave-one-round-out keeps MDD in 4.6439–6.6576 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [5084.0, 5003.0, 4511.5, 2353.0]
strongest single step: after round 2 (5043.5 → 3432.25, -31.95%, variance explained 0.5267). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| toronto_guide__weekend_adventure_planner | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| japan_travel_planner__remove_osaka_itinerary | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
