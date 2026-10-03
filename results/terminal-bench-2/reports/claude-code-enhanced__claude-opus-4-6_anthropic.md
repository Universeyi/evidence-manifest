# Noise floor — terminal-bench 2.0 claude-code-enhanced__claude-opus-4-6_anthropic

398 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 398}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 46 | 51.6854 |
| 2 (partial) | 87 | 57 | 65.5172 |
| 3 (partial) | 84 | 54 | 64.2857 |
| 4 (partial) | 81 | 60 | 74.0741 |
| 5 (partial) | 57 | 46 | 80.7018 |

Complete rounds: mean 51.6854 %, sd 0.0 pp, observed range 0.0 pp.

## Headline

- single-run sd **3.6879 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **10.2221 pp** before the gap is outside noise; 14.6116 pp for 80% power
- 52 of 87 tasks flipped; mean flip rate 0.3199 (max possible at n=5: 0.6)
- re-run (plugin) sd 3.6879 pp, (posterior) 4.2763 pp; bootstrap precision of this estimate 1.7769 pp
- **not reportable:** a task has only 1 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 9.3269–10.2338 pp

## Adjudicability

398 of 398 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 398}.

## Drift screen

series (median completion tokens per round, {'run_total': 356}): [3949.0, 1230.0, 486.0, 335.0, 240.0]
strongest single step: after round 2 (2589.5 → 353.667, -86.34%, variance explained 0.6168). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| adaptive-rejection-sampler | 1/2 | 0.5 | 0.0945–0.9055 | 1.0 |
| feal-linear-cryptanalysis | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| gpt2-codegolf | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| make-mips-interpreter | 2/3 | 0.6667 | 0.2077–0.9385 | 0.6667 |
| path-tracing | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| polyglot-c-py | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| regex-log | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| tune-mjcf | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| winning-avg-corewars | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| break-filter-js-from-html | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pmars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| chess-best-move | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| hf-model-inference | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| mailman | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mteb-leaderboard | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
