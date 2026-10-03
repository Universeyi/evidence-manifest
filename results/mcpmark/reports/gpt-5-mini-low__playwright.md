# Noise floor — MCPMark gpt-5-mini-low__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 97, 'budget_exhausted': 2, 'error': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 25 | 1 | 4.0 |
| 2 | 25 | 0 | 0.0 |
| 3 | 25 | 0 | 0.0 |
| 4 | 24 | 0 | 0.0 |

Complete rounds: mean 1.0 %, sd 2.0 pp, observed range 4.0 pp.

## Headline

- single-run sd **1.7324 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **4.8019 pp** before the gap is outside noise; 6.8638 pp for 80% power
- 1 of 25 tasks flipped; mean flip rate 0.02 (max possible at n=4: 0.6667)
- re-run (plugin) sd 1.7324 pp, (posterior) 6.2152 pp; bootstrap precision of this estimate 0.863 pp
- leave-one-round-out keeps MDD in 0.0–5.2085 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [1338.0, 1031.0, 798.0, 1719.0]
strongest single step: after round 2 (1184.5 → 1258.5, 6.25%, variance explained 0.0115). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| reddit__routine_tracker_forum | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
