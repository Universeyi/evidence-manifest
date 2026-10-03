# Noise floor — MCPMark qwen-3-max__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 106, 'budget_exhausted': 7, 'error': 7}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 28 | 4 | 14.2857 |
| 2 | 28 | 3 | 10.7143 |
| 3 | 28 | 3 | 10.7143 |
| 4 | 29 | 3 | 10.3448 |

Complete rounds: mean 11.5148 %, sd 1.8555 pp, observed range 3.9409 pp.

## Headline

- single-run sd **1.49 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **4.13 pp** before the gap is outside noise; 5.9034 pp for 80% power
- 1 of 28 tasks flipped; mean flip rate 0.0179 (max possible at n=4: 0.6667)
- re-run (plugin) sd 1.49 pp, (posterior) 5.7533 pp; bootstrap precision of this estimate 0.7497 pp
- **not reportable:** a task has only 1 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 0.0–4.6744 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [919.5, 963.0, 1011.5, 975.0]
strongest single step: after round 2 (941.25 → 993.25, 5.52%, variance explained 0.6265). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| papers__find_math_paper | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
