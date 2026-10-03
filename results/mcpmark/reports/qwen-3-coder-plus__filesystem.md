# Noise floor — MCPMark qwen-3-coder-plus__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 99, 'error': 13, 'budget_exhausted': 8}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 26 | 6 | 23.0769 |
| 2 | 28 | 6 | 21.4286 |
| 3 | 27 | 2 | 7.4074 |
| 4 | 26 | 2 | 7.6923 |

Complete rounds: mean 14.9013 %, sd 8.5161 pp, observed range 15.6695 pp.

## Headline

- single-run sd **4.0764 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **11.299 pp** before the gap is outside noise; 16.1509 pp for 80% power
- 7 of 29 tasks flipped; mean flip rate 0.1322 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.0764 pp, (posterior) 6.6511 pp; bootstrap precision of this estimate 2.1169 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 10.0669–11.0714 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [2375.0, 2761.5, 2532.0, 2481.5]
strongest single step: after round 2 (2568.25 → 2506.75, -2.39%, variance explained 0.0474). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| folder_structure__structure_mirror | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| papers__organize_legacy_papers | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| desktop__music_report | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_context__file_merging | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| file_property__size_classification | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| file_property__time_classification | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| votenet__debugging | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
