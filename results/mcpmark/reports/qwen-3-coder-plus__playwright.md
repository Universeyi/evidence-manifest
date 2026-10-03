# Noise floor — MCPMark qwen-3-coder-plus__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 67, 'error': 33}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 17 | 9 | 52.9412 |
| 2 | 19 | 8 | 42.1053 |
| 3 | 15 | 6 | 40.0 |
| 4 | 16 | 7 | 43.75 |

Complete rounds: mean 44.6991 %, sd 5.705 pp, observed range 12.9412 pp.

## Headline

- single-run sd **5.8184 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **16.1275 pp** before the gap is outside noise; 23.0527 pp for 80% power
- 7 of 18 tasks flipped; mean flip rate 0.2037 (max possible at n=4: 0.6667)
- re-run (plugin) sd 5.8184 pp, (posterior) 8.6057 pp; bootstrap precision of this estimate 3.0052 pp
- **not reportable:** a task has only 1 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 13.0735–17.0555 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [2359.0, 2397.0, 1730.0, 1982.0]
strongest single step: after round 2 (2378.0 → 1856.0, -21.95%, variance explained 0.8935). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| reddit__llm_research_summary | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| eval_web__extraction_table | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| reddit__buyitforlife_research | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| reddit__movie_reviewer_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| reddit__routine_tracker_forum | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| shopping_admin__customer_segmentation_setup | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| shopping_admin__search_filtering_operations | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
