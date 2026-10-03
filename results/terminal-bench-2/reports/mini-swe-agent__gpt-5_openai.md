# Noise floor — terminal-bench 2.0 mini-swe-agent__gpt-5_openai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 32 | 35.9551 |
| 2 | 89 | 30 | 33.7079 |
| 3 | 89 | 31 | 34.8315 |
| 4 | 89 | 29 | 32.5843 |
| 5 | 89 | 29 | 32.5843 |

Complete rounds: mean 33.9326 %, sd 1.465 pp, observed range 3.3708 pp.

## Headline

- single-run sd **2.9827 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **8.2675 pp** before the gap is outside noise; 11.8176 pp for 80% power
- 34 of 89 tasks flipped; mean flip rate 0.1955 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.9827 pp, (posterior) 3.8379 pp; bootstrap precision of this estimate 1.3229 pp
- leave-one-round-out keeps MDD in 7.7857–8.3074 pp

## Adjudicability

13 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 432, 'none': 13}.

## Drift screen

series (median completion tokens per round, {'run_total': 432}): [22326.0, 22484.0, 22241.0, 19331.0, 20803.0]
strongest single step: after round 3 (22350.333 → 20067.0, -10.22%, variance explained 0.8489). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| build-pov-ray | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| cancel-async-tasks | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| circuit-fibsqrt | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| code-from-image | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| crack-7z-hash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| fix-code-vulnerability | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| git-multibranch | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| kv-store-grpc | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| large-scale-text-editing | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| llm-inference-batching-scheduler | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| mailman | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| overfull-hbox | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| portfolio-optimization | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| qemu-startup | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| schemelike-metacircular-eval | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
