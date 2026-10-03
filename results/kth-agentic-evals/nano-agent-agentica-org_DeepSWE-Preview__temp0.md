# Noise floor — KTH nano-agent-agentica-org_DeepSWE-Preview__temp0

5000 manifests, 500 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; outcomes {'completed': 4986, 'error': 14}; verifier versions ['swebench-harness-schema-v2']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 500 | 103 | 20.6 |
| 2 | 500 | 103 | 20.6 |
| 3 | 498 | 107 | 21.4859 |
| 4 | 497 | 105 | 21.1268 |
| 5 | 499 | 106 | 21.2425 |
| 6 | 500 | 100 | 20.0 |
| 7 | 500 | 97 | 19.4 |
| 8 | 497 | 104 | 20.9256 |
| 9 | 498 | 102 | 20.4819 |
| 10 | 497 | 91 | 18.3099 |

Complete rounds: mean 20.4173 %, sd 0.9607 pp, observed range 3.176 pp.

## Headline

- single-run sd **1.1377 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **3.1535 pp** before the gap is outside noise; 4.5076 pp for 80% power
- 190 of 500 tasks flipped; mean flip rate 0.1422 (max possible at n=10: 0.5556)
- re-run (plugin) sd 1.1377 pp, (posterior) 1.3975 pp; bootstrap precision of this estimate 0.3614 pp
- leave-one-round-out keeps MDD in 3.0975–3.1546 pp

## Adjudicability

0 of 5000 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 5000}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| django__django-11163 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13569 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13820 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-14053 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-14238 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-14349 | 5/9 | 0.5556 | 0.2667–0.8112 | 0.5556 |
| django__django-15380 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-15569 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-15814 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-16116 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-16145 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-7530 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| psf__requests-1921 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| pydata__xarray-2905 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| pydata__xarray-4966 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
