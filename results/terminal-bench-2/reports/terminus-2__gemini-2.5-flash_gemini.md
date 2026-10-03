# Noise floor — terminal-bench 2.0 terminus-2__gemini-2.5-flash_gemini

439 manifests, 89 tasks, rounds [1, 2, 3, 4, 5]; outcomes {'completed': 439}; verifier versions ['unrecorded']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 89 | 15 | 16.8539 |
| 2 | 89 | 17 | 19.1011 |
| 3 | 89 | 16 | 17.9775 |
| 4 (partial) | 88 | 11 | 12.5 |
| 5 (partial) | 84 | 16 | 19.0476 |

Complete rounds: mean 17.9775 %, sd 1.1236 pp, observed range 2.2472 pp.

## Headline

- single-run sd **2.4287 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **6.7319 pp** before the gap is outside noise; 9.6226 pp for 80% power
- 23 of 89 tasks flipped; mean flip rate 0.1303 (max possible at n=5: 0.6)
- re-run (plugin) sd 2.4287 pp, (posterior) 3.583 pp; bootstrap precision of this estimate 1.0697 pp
- leave-one-round-out keeps MDD in 6.0667–6.764 pp

## Adjudicability

1 of 439 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 438, 'none': 1}.

## Drift screen

series (median completion tokens per round, {'run_total': 439}): [12885.0, 13466.0, 13749.0, 13996.0, 14094.0]
strongest single step: after round 2 (13175.5 → 13946.333, 5.85%, variance explained 0.7545). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| crack-7z-hash | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| custom-memory-heap-crash | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| extract-elf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| hf-model-inference | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| merge-diff-arc-agi-task | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| model-extraction-relu-logits | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| nginx-request-logging | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| openssl-selfsigned-cert | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| prove-plus-comm | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| pytorch-model-recovery | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| sqlite-with-gcov | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| tune-mjcf | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| build-pov-ray | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| cancel-async-tasks | 1/5 | 0.2 | 0.0362–0.6245 | 0.4 |
| cobol-modernization | 4/5 | 0.8 | 0.3755–0.9638 | 0.4 |
