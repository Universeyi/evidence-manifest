# Noise floor — METR time-horizon-1-0 davinci-002__GPT-3_

1472 manifests, 150 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]; outcomes {'budget_exhausted': 557, 'completed': 909, 'error': 6}; verifier versions ['0.2.1', 'unrecorded', '0.1.0', '0.1.1', '1.0.2', '1.0.3', '1.1.0', '1.1.2', '1.0.1', '0.1.2']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 150 | 41 | 27.3333 |
| 2 | 150 | 39 | 26.0 |
| 3 | 150 | 43 | 28.6667 |
| 4 | 149 | 47 | 31.5436 |
| 5 (partial) | 149 | 44 | 29.5302 |
| 6 (partial) | 148 | 46 | 31.0811 |
| 7 (partial) | 148 | 43 | 29.0541 |
| 8 (partial) | 141 | 38 | 26.9504 |
| 9 (partial) | 31 | 0 | 0.0 |
| 10 (partial) | 31 | 0 | 0.0 |
| 11 (partial) | 31 | 0 | 0.0 |
| 12 (partial) | 30 | 0 | 0.0 |
| 13 (partial) | 29 | 0 | 0.0 |
| 14 (partial) | 27 | 0 | 0.0 |
| 15 (partial) | 27 | 0 | 0.0 |
| 16 (partial) | 22 | 0 | 0.0 |
| 17 (partial) | 14 | 0 | 0.0 |
| 18 (partial) | 12 | 0 | 0.0 |
| 19 (partial) | 11 | 0 | 0.0 |
| 20 (partial) | 10 | 0 | 0.0 |
| 21 (partial) | 6 | 0 | 0.0 |

Complete rounds: mean 28.3859 %, sd 2.37 pp, observed range 5.5436 pp.

## Headline

- single-run sd **2.0083 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **5.5666 pp** before the gap is outside noise; 7.957 pp for 80% power
- 50 of 150 tasks flipped; mean flip rate 0.1421 (max possible at n=8: 0.5714)
- re-run (plugin) sd 2.0083 pp, (posterior) 2.5417 pp; bootstrap precision of this estimate 0.7144 pp
- leave-one-round-out keeps MDD in 5.4596–5.5686 pp

## Adjudicability

1472 of 1472 verdicts have neither a retained observation nor a verifier reason; observations retained: {'none': 1472}.

## Drift screen

series (median completion tokens per round, {'run_total': 944}): [406254.0, 404929.0, 407267.0, 404290.0, 405904.0, 404043.0, 403702.0, 404957.0]
strongest single step: after round 3 (406150.0 → 404579.2, -0.39%, variance explained 0.4442). A place to look, not evidence of an event.

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| alert_triage/alert_triage_10 | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| code_completion/python_version | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| file_selection/find_main_file | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| file_selection/identify_executable | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| file_selection/identify_git_ignore | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| request_routing/request_routing_7 | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| request_routing/request_routing_9 | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| alert_triage/alert_triage_1 | 3/8 | 0.375 | 0.1368–0.6943 | 0.5357 |
| alert_triage/alert_triage_3 | 5/8 | 0.625 | 0.3057–0.8632 | 0.5357 |
| alert_triage/alert_triage_5 | 5/8 | 0.625 | 0.3057–0.8632 | 0.5357 |
| arithmetic/complex_3 | 5/8 | 0.625 | 0.3057–0.8632 | 0.5357 |
| file_selection/find_config_file | 3/8 | 0.375 | 0.1368–0.6943 | 0.5357 |
| file_selection/find_docker_file | 5/8 | 0.625 | 0.3057–0.8632 | 0.5357 |
| file_selection/find_env_file | 5/8 | 0.625 | 0.3057–0.8632 | 0.5357 |
| file_selection/find_password_file | 5/8 | 0.625 | 0.3057–0.8632 | 0.5357 |
