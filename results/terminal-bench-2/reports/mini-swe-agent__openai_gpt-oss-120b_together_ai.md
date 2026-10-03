# Noise floor — terminal-bench 2.0 mini-swe-agent__openai_gpt-oss-120b_together_ai

887 manifests, 89 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; outcomes {'completed': 887}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 14 | 15.7303 |
| 2 | 89 | 10 | 11.236 |
| 3 | 89 | 10 | 11.236 |
| 4 | 89 | 16 | 17.9775 |
| 5 | 89 | 13 | 14.6067 |
| 6 | 89 | 11 | 12.3596 |
| 7 | 89 | 13 | 14.6067 |
| 8 | 89 | 12 | 13.4831 |
| 9 | 89 | 15 | 16.8539 |
| 10 (partial) | 86 | 12 | 13.9535 |

Complete rounds: mean 14.2322 %, sd 2.3835 pp, observed range 6.7415 pp.

## Headline

- single-run sd **2.3129 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.4109 pp** before the gap is outside noise; 9.1638 pp for 80% power
- 21 of 89 tasks flipped; mean flip rate 0.1061 (max possible at n=10: 0.5556)
- re-run (plugin) sd 2.3129 pp, (posterior) 3.0492 pp; bootstrap precision of this estimate 0.739 pp
- leave-one-round-out keeps MDD in 6.2036–6.4603 pp

## Adjudicability

3 of 887 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 884, 'none': 3}.

## Drift screen

series (median completion tokens per round, {'run_total': 882}): [3356.0, 3282.0, 3122.0, 3538.0, 2889.5, 3020.0, 4235.0, 2969.0, 2644.0, 3599.5]
strongest single step: after round 7 (3348.929 → 3070.833, -8.3%, variance explained 0.0887). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| qemu-startup | 4/9 | 0.4444 | 0.1888–0.7333 | 0.5556 |
| build-pmars | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| cobol-modernization | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| git-multibranch | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| kv-store-grpc | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| multi-source-data-merger | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| nginx-request-logging | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| openssl-selfsigned-cert | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| portfolio-optimization | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| pypi-server | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| vulnerable-secret | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| adaptive-rejection-sampler | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
| cancel-async-tasks | 8/10 | 0.8 | 0.4902–0.9433 | 0.3556 |
| configure-git-webserver | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
| extract-elf | 2/10 | 0.2 | 0.0567–0.5098 | 0.3556 |
