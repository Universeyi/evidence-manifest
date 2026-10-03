# Noise floor — MCPMark o4-mini__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 120}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 30 | 9 | 30.0 |
| 2 | 30 | 7 | 23.3333 |
| 3 | 30 | 7 | 23.3333 |
| 4 | 30 | 7 | 23.3333 |

Complete rounds: mean 25.0 %, sd 3.3333 pp, observed range 6.6667 pp.

## Headline

- single-run sd **3.9187 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **10.8619 pp** before the gap is outside noise; 15.526 pp for 80% power
- 7 of 30 tasks flipped; mean flip rate 0.1222 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.9187 pp, (posterior) 6.2655 pp; bootstrap precision of this estimate 1.945 pp
- leave-one-round-out keeps MDD in 9.6955–10.7214 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [9761.0, 10370.5, 9950.5, 11886.5]
strongest single step: after round 2 (10065.75 → 10918.5, 8.47%, variance explained 0.2609). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| legal_document__dispute_review | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| desktop__music_report | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| desktop__timeline_extraction | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_context__duplicates_searching | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| file_context__file_merging | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| file_context__uppercase | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| papers__organize_legacy_papers | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
