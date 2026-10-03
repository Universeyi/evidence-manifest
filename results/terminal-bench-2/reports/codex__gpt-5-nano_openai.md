# Noise floor — terminal-bench 2.0 codex__gpt-5-nano_openai

440 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 440}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 9 | 10.1124 |
| 2 | 89 | 9 | 10.1124 |
| 3 | 89 | 10 | 11.236 |
| 4 | 89 | 12 | 13.4831 |
| 5 (partial) | 84 | 11 | 13.0952 |

Complete rounds: mean 11.236 %, sd 1.589 pp, observed range 3.3707 pp.

## Headline

- single-run sd **2.3153 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.4176 pp** before the gap is outside noise; 9.1733 pp for 80% power
- 22 of 89 tasks flipped; mean flip rate 0.1191 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.3153 pp, (posterior) 3.4986 pp; bootstrap precision of this estimate 1.0431 pp
- leave-one-round-out keeps MDD in 5.9026–6.4162 pp

## Adjudicability

17 of 440 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 423, 'none': 17}.

## Drift screen

series (median completion tokens per round, {'run_total': 423}): [8746.0, 8251.0, 8544.5, 7478.0, 6889.5]
strongest single step: after round 3 (8513.833 → 7183.75, -15.62%, variance explained 0.8772). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| cobol-modernization | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-code-vulnerability | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-git | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| git-leak-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| headless-terminal | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| hf-model-inference | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| modernize-scientific-stack | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-startup | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sqlite-with-gcov | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pmars | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| code-from-image | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
| constraints-scheduling | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| kv-store-grpc | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| log-summary-date-ranges | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| mcmc-sampling-stan | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
