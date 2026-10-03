# Noise floor — terminal-bench 2.0 terminus-3-3__claude-opus-4-6_anthropic

442 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 442}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 64 | 71.9101 |
| 2 | 89 | 70 | 78.6517 |
| 3 (partial) | 88 | 61 | 69.3182 |
| 4 (partial) | 88 | 68 | 77.2727 |
| 5 (partial) | 88 | 68 | 77.2727 |

Complete rounds: mean 75.2809 %, sd 4.767 pp, observed range 6.7416 pp.

## Headline

- single-run sd **2.4774 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.8669 pp** before the gap is outside noise; 9.8156 pp for 80% power
- 24 of 89 tasks flipped; mean flip rate 0.1393 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.4774 pp, (posterior) 3.5723 pp; bootstrap precision of this estimate 1.1603 pp
- **not reportable:** a task has only 2 scored trial(s) (need 3) -- arithmetic, not evidence
- leave-one-round-out keeps MDD in 6.1944–6.9037 pp

## Adjudicability

195 of 442 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 247, 'none': 195}.

## Drift screen

series (median completion tokens per round, {'run_total': 442}): [17152.0, 17472.0, 16523.0, 15308.0, 17932.5]
strongest single step: after round 2 (17312.0 → 16587.833, -4.18%, variance explained 0.1523). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| path-tracing | 1/2 | 0.5 | 0.0945–0.9055 | 1.0 |
| build-pmars | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| chess-best-move | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| compile-compcert | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| dna-assembly | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| dna-insert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| extract-moves-from-video | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| gcode-to-text | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mailman | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| make-mips-interpreter | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| model-extraction-relu-logits | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| tune-mjcf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| configure-git-webserver | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| count-dataset-tokens | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| largest-eigenval | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
