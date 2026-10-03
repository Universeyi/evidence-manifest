# Noise floor — MCPMark kimi-k2-0711__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 110, 'budget_exhausted': 2, 'error': 8}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 29 | 6 | 20.6897 |
| 2 | 27 | 7 | 25.9259 |
| 3 | 28 | 5 | 17.8571 |
| 4 | 28 | 6 | 21.4286 |

Complete rounds: mean 21.4753 %, sd 3.3426 pp, observed range 8.0688 pp.

## Headline

- single-run sd **3.5927 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **9.9583 pp** before the gap is outside noise; 14.2344 pp for 80% power
- 5 of 29 tasks flipped; mean flip rate 0.1149 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.5927 pp, (posterior) 6.3462 pp; bootstrap precision of this estimate 2.031 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 6.3696–10.3103 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [1949.5, 2129.5, 1840.0, 1849.5]
strongest single step: after round 2 (2039.5 → 1844.75, -9.55%, variance explained 0.7001). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| papers__find_math_paper | 1/2 | 0.5 | 0.0945–0.9055 | 1.0 |
| folder_structure__structure_mirror | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| student_database__duplicate_name | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| desktop__project_management | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| votenet__debugging | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
