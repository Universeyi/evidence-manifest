# Noise floor — MCPMark gpt-5-mini-low__notion

112 manifests, 28 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 112}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 28 | 0 | 0.0 |
| 2 | 28 | 4 | 14.2857 |
| 3 | 28 | 1 | 3.5714 |
| 4 | 28 | 1 | 3.5714 |

Complete rounds: mean 5.3571 %, sd 6.1859 pp, observed range 14.2857 pp.

## Headline

- single-run sd **3.3776 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **9.3621 pp** before the gap is outside noise; 13.3822 pp for 80% power
- 4 of 28 tasks flipped; mean flip rate 0.0833 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.3776 pp, (posterior) 6.343 pp; bootstrap precision of this estimate 1.6703 pp
- leave-one-round-out keeps MDD in 6.5883–9.5785 pp

## Adjudicability

0 of 112 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 112}.

## Drift screen

series (median completion tokens per round, {'run_total': 112}): [3419.0, 3575.0, 1811.5, 2402.0]
strongest single step: after round 2 (3497.0 → 2106.75, -39.76%, variance explained 0.912). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| computer_science_student_dashboard__code_snippets_go | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| team_projects__swap_tasks | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| japan_travel_planner__restaurant_expenses_sync | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| team_projects__priority_tasks_table | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
