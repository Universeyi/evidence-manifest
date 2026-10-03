# Noise floor — KTH nano-agent-Qwen_Qwen3-32B

5000 manifests, 500 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; outcomes {'completed': 4989, 'error': 11}; verifier versions ['swebench-harness-schema-v2']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 499 | 86 | 17.2345 |
| 2 | 499 | 80 | 16.0321 |
| 3 | 498 | 80 | 16.0643 |
| 4 | 500 | 81 | 16.2 |
| 5 | 500 | 79 | 15.8 |
| 6 | 499 | 75 | 15.0301 |
| 7 | 498 | 86 | 17.2691 |
| 8 | 499 | 86 | 17.2345 |
| 9 | 498 | 85 | 17.0683 |
| 10 | 499 | 81 | 16.2325 |

Complete rounds: mean 16.4165 %, sd 0.7561 pp, observed range 2.239 pp.

## Headline

- single-run sd **0.996 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **2.7607 pp** before the gap is outside noise; 3.9462 pp for 80% power
- 150 of 500 tasks flipped; mean flip rate 0.1113 (max possible at n=10: 0.5556)
- re-run (plugin) sd 0.996 pp, (posterior) 1.3133 pp; bootstrap precision of this estimate 0.3178 pp
- leave-one-round-out keeps MDD in 2.7175–2.7774 pp

## Adjudicability

0 of 5000 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 5000}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| astropy__astropy-14995 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| astropy__astropy-7671 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13363 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13786 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-15569 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-15814 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| matplotlib__matplotlib-22719 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| matplotlib__matplotlib-25122 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| pallets__flask-5014 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| pylint-dev__pylint-7277 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| pytest-dev__pytest-7205 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| scikit-learn__scikit-learn-13439 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| scikit-learn__scikit-learn-26323 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| sympy__sympy-16450 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| astropy__astropy-7336 | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
