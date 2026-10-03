# Noise floor — MCPMark glm-4-5__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 114, 'budget_exhausted': 5, 'error': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 30 | 2 | 6.6667 |
| 2 | 29 | 2 | 6.8966 |
| 3 | 30 | 2 | 6.6667 |
| 4 | 30 | 3 | 10.0 |

Complete rounds: mean 7.5575 %, sd 1.6319 pp, observed range 3.3333 pp.

## Headline

- single-run sd **2.4986 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.9256 pp** before the gap is outside noise; 9.8996 pp for 80% power
- 3 of 30 tasks flipped; mean flip rate 0.05 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.4986 pp, (posterior) 5.8608 pp; bootstrap precision of this estimate 1.2385 pp
- leave-one-round-out keeps MDD in 4.3576–7.5318 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [2993.5, 2962.5, 3143.0, 3383.5]
strongest single step: after round 2 (2978.0 → 3263.25, 9.58%, variance explained 0.7346). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| file_context__file_merging | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| file_context__uppercase | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| threestudio__code_locating | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
