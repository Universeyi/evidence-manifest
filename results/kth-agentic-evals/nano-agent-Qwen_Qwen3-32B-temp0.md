# Noise floor — KTH nano-agent-Qwen_Qwen3-32B-temp0

5000 manifests, 500 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; outcomes {'completed': 4990, 'error': 10}; verifier versions ['swebench-harness-schema-v2']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 499 | 86 | 17.2345 |
| 2 | 499 | 78 | 15.6313 |
| 3 | 498 | 75 | 15.0602 |
| 4 | 499 | 82 | 16.4329 |
| 5 | 500 | 90 | 18.0 |
| 6 | 498 | 84 | 16.8675 |
| 7 | 500 | 78 | 15.6 |
| 8 | 498 | 72 | 14.4578 |
| 9 | 500 | 88 | 17.6 |
| 10 | 499 | 85 | 17.0341 |

Complete rounds: mean 16.3918 %, sd 1.1602 pp, observed range 3.5422 pp.

## Headline

- single-run sd **0.9841 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **2.7277 pp** before the gap is outside noise; 3.899 pp for 80% power
- 144 of 500 tasks flipped; mean flip rate 0.1075 (max possible at n=10: 0.5556)
- re-run (plugin) sd 0.9841 pp, (posterior) 1.288 pp; bootstrap precision of this estimate 0.3144 pp
- leave-one-round-out keeps MDD in 2.677–2.7455 pp

## Adjudicability

0 of 5000 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 5000}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| astropy__astropy-14995 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-11276 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-12050 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13363 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13821 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-14089 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-15741 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| matplotlib__matplotlib-25122 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| matplotlib__matplotlib-25287 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| pylint-dev__pylint-7277 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| scikit-learn__scikit-learn-13439 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| scikit-learn__scikit-learn-15100 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| sympy__sympy-16450 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| sympy__sympy-19346 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| sympy__sympy-23950 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
