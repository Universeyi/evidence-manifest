# Noise floor — MCPMark o3__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 119, 'error': 1}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 29 | 11 | 37.931 |
| 2 | 30 | 10 | 33.3333 |
| 3 | 30 | 10 | 33.3333 |
| 4 | 30 | 12 | 40.0 |

Complete rounds: mean 36.1494 %, sd 3.3597 pp, observed range 6.6667 pp.

## Headline

- single-run sd **4.006 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **11.1039 pp** before the gap is outside noise; 15.8719 pp for 80% power
- 7 of 30 tasks flipped; mean flip rate 0.1278 (max possible at n=4: 0.6667)
- re-run (plugin) sd 4.006 pp, (posterior) 6.3869 pp; bootstrap precision of this estimate 2.0028 pp
- leave-one-round-out keeps MDD in 9.7496–10.6667 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [8268.5, 6580.0, 9887.5, 9176.5]
strongest single step: after round 2 (7424.25 → 9532.0, 28.39%, variance explained 0.7258). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| file_context__uppercase | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| papers__organize_legacy_papers | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| desktop__timeline_extraction | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| desktop_template__contact_information | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_context__duplicates_searching | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_context__pattern_matching | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| legal_document__solution_tracing | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
