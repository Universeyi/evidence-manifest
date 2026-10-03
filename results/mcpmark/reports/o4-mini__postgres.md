# Noise floor — MCPMark o4-mini__postgres

84 manifests, 21 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 84}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 21 | 1 | 4.7619 |
| 2 | 21 | 3 | 14.2857 |
| 3 | 21 | 3 | 14.2857 |
| 4 | 21 | 3 | 14.2857 |

Complete rounds: mean 11.9047 %, sd 4.7619 pp, observed range 9.5238 pp.

## Headline

- single-run sd **3.7588 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **10.4187 pp** before the gap is outside noise; 14.8925 pp for 80% power
- 3 of 21 tasks flipped; mean flip rate 0.0794 (max possible at n=4: 0.6667)
- re-run (plugin) sd 3.7588 pp, (posterior) 7.1774 pp; bootstrap precision of this estimate 1.8865 pp
- leave-one-round-out keeps MDD in 8.8188–10.8644 pp

## Adjudicability

0 of 84 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 84}.

## Drift screen

series (median completion tokens per round, {'run_total': 84}): [4347.0, 5895.0, 4475.0, 5327.0]
strongest single step: after round 2 (5121.0 → 4901.0, -4.3%, variance explained 0.0301). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| chinook__sales_and_music_charts | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| security__user_permission_audit | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| vectors__dba_vector_analysis | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
