# Noise floor — MCPMark grok-4__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 107, 'error': 5}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 26 | 1 | 3.8462 |
| 2 | 28 | 1 | 3.5714 |
| 3 | 26 | 1 | 3.8462 |
| 4 | 27 | 0 | 0.0 |

Complete rounds: mean 2.8159 %, sd 1.8818 pp, observed range 3.8462 pp.

## Headline

- single-run sd **1.5409 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **4.2711 pp** before the gap is outside noise; 6.1051 pp for 80% power
- 1 of 28 tasks flipped; mean flip rate 0.0179 (max possible at n=4: 0.6667)
- re-run (plugin) sd 1.5409 pp, (posterior) 5.9064 pp; bootstrap precision of this estimate 0.7722 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 0.0–4.6611 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [11484.0, 12415.0, 11367.0, 11808.0]
strongest single step: after round 2 (11949.5 → 11587.5, -3.03%, variance explained 0.1981). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| japan_travel_planner__remove_osaka_itinerary | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
