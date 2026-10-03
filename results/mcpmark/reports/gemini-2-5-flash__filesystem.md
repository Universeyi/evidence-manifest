# Noise floor — MCPMark gemini-2-5-flash__filesystem

120 manifests, 30 tasks, rounds [1, 2, 3, 4]; outcomes {'completed': 120}; verifier versions ['mcpmark-v1-0905']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 30 | 2 | 6.6667 |
| 2 | 30 | 3 | 10.0 |
| 3 | 30 | 3 | 10.0 |
| 4 | 30 | 2 | 6.6667 |

Complete rounds: mean 8.3333 %, sd 1.9245 pp, observed range 3.3333 pp.

## Headline

- single-run sd **2.0306 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **5.6284 pp** before the gap is outside noise; 8.0453 pp for 80% power
- 2 of 30 tasks flipped; mean flip rate 0.0333 (max possible at n=4: 0.6667)
- re-run (plugin) sd 2.0306 pp, (posterior) 5.7267 pp; bootstrap precision of this estimate 1.0128 pp
- leave-one-round-out keeps MDD in 4.3188–6.147 pp

## Adjudicability

0 of 120 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 120}.

## Drift screen

series (median completion tokens per round, {'run_total': 120}): [2897.0, 4884.0, 2439.5, 3820.5]
strongest single step: after round 2 (3890.5 → 3130.0, -19.55%, variance explained 0.165). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| papers__find_math_paper | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| votenet__debugging | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
