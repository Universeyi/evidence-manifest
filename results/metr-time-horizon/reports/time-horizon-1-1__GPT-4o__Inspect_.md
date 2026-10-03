# Noise floor — METR time-horizon-1-1 GPT-4o__Inspect_

1044 manifests, 228 tasks, rounds [1, 2, 3, 4, 5, 6]; outcomes {'completed': 1043, 'budget_exhausted': 1}; verifier versions ['1.0.11', '0.1.5', '0.2.5', '0.9.3', '0.8.3', '0.8.2', '0.9.2', '2.0.1', '1.0.4', '1.0.5', '2.1.10', '0.1.6', '1.0.6', '0.3.1', '1.0.3', '0.1.9', '1.2.4', '0.1.7', '1.1.3', '2.1.3', '1.0.7', '0.0.6', '0.1.8', '0.2.1', '1.0.10', '1.0.1', '1.3.3', '1.2.1', '0.2.7', '0.2.6', '3.2.1', '0.4.0', '1.1.10', '2.1.6', '0.1.3', '1.0.9', '1.2.8', '2.0.0', '0.5.2', '0.2.2', '0.0.3', '0.1.10', '0.2.8', '1.0.12', '1.1.8', '0.2.10']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 228 | 109 | 47.807 |
| 2 | 228 | 105 | 46.0526 |
| 3 | 228 | 101 | 44.2982 |
| 4 | 228 | 104 | 45.614 |
| 5 (partial) | 66 | 66 | 100.0 |
| 6 (partial) | 66 | 65 | 98.4848 |

Complete rounds: mean 45.9429 %, sd 1.4492 pp, observed range 3.5088 pp.

## Headline

- single-run sd **1.3857 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **3.8409 pp** before the gap is outside noise; 5.4902 pp for 80% power
- 50 of 228 tasks flipped; mean flip rate 0.1156 (max possible at n=4: 0.6667)
- re-run (plugin) sd 1.3857 pp, (posterior) 2.2223 pp; bootstrap precision of this estimate 0.6887 pp
- leave-one-round-out keeps MDD in 3.5022–3.8442 pp

## Adjudicability

1044 of 1044 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 1044}.

## Drift screen

series (median completion tokens per round, {'run_total': 1044}): [12330.5, 11317.5, 8611.5, 11302.5]
strongest single step: after round 2 (11824.0 → 9957.0, -15.79%, variance explained 0.4575). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| count_words/the | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| credit_card_validity/add_check_digits | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| data_cleaning_arjun/available_remote | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| data_cleaning_arjun/hourly_easy | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| esolang/broccoli_fibonacci | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| hypothesis_testing/mystery_function_2 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| munge_data/chess | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| munge_data/very_easy | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| password_check/3 | 2/4 | 0.5 | 0.15–0.85 | 0.6667 |
| request_routing/request_routing_9 | 4/6 | 0.6667 | 0.3–0.9032 | 0.5333 |
| apps_dataset_debug/dev_9_sort | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| audio_classification/macaques | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| count_words/ai | 1/4 | 0.25 | 0.0456–0.6994 | 0.5 |
| credit_card_validity/validate_number | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
| data_cleaning_arjun/available | 3/4 | 0.75 | 0.3006–0.9544 | 0.5 |
