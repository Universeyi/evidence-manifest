# Noise floor — terminal-bench 2.0 openhands__claude-opus-4-1-20250805_anthropic

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 31 | 34.8315 |
| 2 | 89 | 31 | 34.8315 |
| 3 | 89 | 32 | 35.9551 |
| 4 | 89 | 36 | 40.4494 |
| 5 | 89 | 34 | 38.2022 |

Complete rounds: mean 36.8539 %, sd 2.4359 pp, observed range 5.6179 pp.

## Headline

- single-run sd **2.7407 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **7.5967 pp** before the gap is outside noise; 10.8588 pp for 80% power
- 30 of 89 tasks flipped; mean flip rate 0.1685 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.7407 pp, (posterior) 3.7598 pp; bootstrap precision of this estimate 1.2362 pp
- leave-one-round-out keeps MDD in 6.9248–7.7541 pp

## Adjudicability

5 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 440, 'none': 5}.

## Drift screen

series (median completion tokens per round, {'run_total': 440}): [10643.0, 10575.5, 11073.0, 11774.0, 11380.0]
strongest single step: after round 3 (10763.833 → 11577.0, 7.55%, variance explained 0.7804). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| break-filter-js-from-html | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| build-pmars | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| code-from-image | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-code-vulnerability | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| git-multibranch | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| large-scale-text-editing | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| largest-eigenval | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| model-extraction-relu-logits | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-startup | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| rstan-to-pystan | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sanitize-git-repo | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| schemelike-metacircular-eval | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sparql-university | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
