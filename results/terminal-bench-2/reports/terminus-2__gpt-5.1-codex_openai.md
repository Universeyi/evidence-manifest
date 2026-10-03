# Noise floor — terminal-bench 2.0 terminus-2__gpt-5.1-codex_openai

445 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 445}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 33 | 37.0787 |
| 2 | 89 | 28 | 31.4607 |
| 3 | 89 | 33 | 37.0787 |
| 4 | 89 | 40 | 44.9438 |
| 5 | 89 | 30 | 33.7079 |

Complete rounds: mean 36.854 %, sd 5.112 pp, observed range 13.4831 pp.

## Headline

- single-run sd **3.2884 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **9.1148 pp** before the gap is outside noise; 13.0288 pp for 80% power
- 46 of 89 tasks flipped; mean flip rate 0.2427 (max possible at n=5: 0.6)
- re-run (plugin) sd 3.2884 pp, (posterior) 4.0138 pp; bootstrap precision of this estimate 1.4951 pp
- leave-one-round-out keeps MDD in 8.6364–9.0436 pp

## Adjudicability

0 of 445 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 445}.

## Drift screen

series (median completion tokens per round, {'run_total': 444}): [10636.5, 14549.0, 10128.0, 13617.0, 11151.0]
strongest single step: after round 2 (12592.75 → 11632.0, -7.63%, variance explained 0.0729). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| bn-fit-modify | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| code-from-image | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| compile-compcert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| crack-7z-hash | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| distribution-search | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-elf | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| financial-document-processor | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| fix-ocaml-gc | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| hf-model-inference | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| log-summary-date-ranges | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| merge-diff-arc-agi-task | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| pytorch-model-recovery | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| qemu-alpine-ssh | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| regex-log | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| sparql-university | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
