# Noise floor — METR time-horizon-1-1 GPT-4_0314

1401 manifests, 213 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8]; outcomes {'completed': 1037, 'budget_exhausted': 364}; verifier versions ['1.0.9', '0.1.4', '0.2.5', '0.2.11', '0.2.8', '0.2.6', 'unrecorded', '1.0.3', '1.0.5', '2.1.6', '0.1.6', '0.3.1', '1.0.2', '0.1.8', '1.2.2', '0.1.7', '0.1.5', '1.1.3', '2.1.2', '1.0.6', '0.0.6', '0.2.0', '1.0.8', '0.0.4', '1.0.1', '1.0.4', '0.1.9', '2.0.0', '1.3.1', '1.1.8', '2.1.4', '0.1.3', '1.2.7', '1.0.7', '1.0.10', '1.0.14', '0.0.2', '0.2.7', '1.1.7', '0.2.9']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 213 | 95 | 44.6009 |
| 2 | 213 | 92 | 43.1925 |
| 3 | 213 | 93 | 43.662 |
| 4 | 213 | 92 | 43.1925 |
| 5 | 213 | 91 | 42.723 |
| 6 (partial) | 204 | 86 | 42.1569 |
| 7 (partial) | 66 | 65 | 98.4848 |
| 8 (partial) | 66 | 65 | 98.4848 |

Complete rounds: mean 43.4742 %, sd 0.712 pp, observed range 1.8779 pp.

## Headline

- single-run sd **1.3413 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **3.7178 pp** before the gap is outside noise; 5.3143 pp for 80% power
- 43 of 213 tasks flipped; mean flip rate 0.0923 (max possible at n=6: 0.6)
- re-run (plugin) sd 1.3413 pp, (posterior) 2.0673 pp; bootstrap precision of this estimate 0.552 pp
- leave-one-round-out keeps MDD in 3.4717–3.7461 pp

## Adjudicability

1401 of 1401 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 1401}.

## Drift screen

series (median completion tokens per round, {'run_total': 873}): [742188.5, 742807.0, 738719.0, 745856.0, 759662.0, 770745.5]
strongest single step: after round 4 (742392.625 → 765203.75, 3.07%, variance explained 0.8884). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| env_scientist/level2 | 2/5 | 0.4 | 0.1176–0.7693 | 0.6 |
| hypothesis_testing/mystery_function_2 | 3/6 | 0.5 | 0.1876–0.8124 | 0.6 |
| interpret_data/ecommerce_spent_most | 3/5 | 0.6 | 0.2307–0.8824 | 0.6 |
| munge_data/easy | 3/6 | 0.5 | 0.1876–0.8124 | 0.6 |
| wikipedia_research/austrian_votes | 3/6 | 0.5 | 0.1876–0.8124 | 0.6 |
| apps_dataset_debug/dev_9_sort | 4/6 | 0.6667 | 0.3–0.9032 | 0.5333 |
| blackbox/acorn | 2/6 | 0.3333 | 0.0968–0.7 | 0.5333 |
| blackbox/apple | 2/6 | 0.3333 | 0.0968–0.7 | 0.5333 |
| count_words/at | 4/6 | 0.6667 | 0.3–0.9032 | 0.5333 |
| count_words/at_harder | 2/6 | 0.3333 | 0.0968–0.7 | 0.5333 |
| count_words/the | 2/6 | 0.3333 | 0.0968–0.7 | 0.5333 |
| credit_card_validity/add_check_digits | 2/6 | 0.3333 | 0.0968–0.7 | 0.5333 |
| data_cleaning_arjun/available | 2/6 | 0.3333 | 0.0968–0.7 | 0.5333 |
| debug_small_libs/markdown | 4/6 | 0.6667 | 0.3–0.9032 | 0.5333 |
| env_scientist/level1 | 4/6 | 0.6667 | 0.3–0.9032 | 0.5333 |
