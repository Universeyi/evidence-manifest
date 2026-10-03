# Noise floor — MCPMark k2-0905__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 105, 'budget_exhausted': 6, 'error': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 27 | 1 | 3.7037 |
| 2 | 28 | 3 | 10.7143 |
| 3 | 28 | 2 | 7.1429 |
| 4 | 28 | 3 | 10.7143 |

Complete rounds: mean 8.0688 %, sd 3.362 pp, observed range 7.0106 pp.

## Headline

- single-run sd **2.3657 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.5573 pp** before the gap is outside noise; 9.373 pp for 80% power
- 2 of 28 tasks flipped; mean flip rate 0.0417 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.3657 pp, (posterior) 5.8896 pp; bootstrap precision of this estimate 1.1729 pp
- leave-one-round-out keeps MDD in 4.66–6.6113 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [4078.0, 3162.5, 3526.0, 3768.0]
strongest single step: after round 2 (3620.25 → 3647.0, 0.74%, variance explained 0.0016). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| standard_operating_procedure__deployment_process_sop | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| toronto_guide__change_color | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
