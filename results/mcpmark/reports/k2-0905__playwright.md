# Noise floor — MCPMark k2-0905__playwright

100 manifests, 25 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 85, 'error': 15}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 20 | 6 | 30.0 |
| 2 | 22 | 9 | 40.9091 |
| 3 | 22 | 9 | 40.9091 |
| 4 | 21 | 6 | 28.5714 |

Complete rounds: mean 35.0974 %, sd 6.7361 pp, observed range 12.3377 pp.

## Headline

- single-run sd **4.3725 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **12.1197 pp** before the gap is outside noise; 17.324 pp for 80% power
- 5 of 22 tasks flipped; mean flip rate 0.1288 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.3725 pp, (posterior) 7.3924 pp; bootstrap precision of this estimate 2.3121 pp
- **not reportable:** a task has only 1 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 11.312–11.8148 pp

## Adjudicability

0 of 100 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 100}.

## Drift screen

series (median completion tokens per round, {'run_total': 100}): [2013.0, 1878.0, 2111.0, 1813.0]
strongest single step: after round 2 (1945.5 → 1962.0, 0.85%, variance explained 0.0051). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| reddit__ai_data_analyst | 1/3 | 0.3333 | 0.0615–0.7923 | 0.6667 |
| reddit__budget_europe_travel | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| reddit__llm_research_summary | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| reddit__movie_reviewer_analysis | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| shopping_admin__marketing_customer_analysis | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
