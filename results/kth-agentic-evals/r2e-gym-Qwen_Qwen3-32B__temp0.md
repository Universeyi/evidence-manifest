# Noise floor — KTH r2e-gym-Qwen_Qwen3-32B__temp0

5000 manifests, 500 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; outcomes {'completed': 4980, 'error': 20}; verifier versions ['swebench-harness-schema-v2']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 498 | 117 | 23.494 |
| 2 | 497 | 108 | 21.7304 |
| 3 | 499 | 99 | 19.8397 |
| 4 | 496 | 102 | 20.5645 |
| 5 | 495 | 117 | 23.6364 |
| 6 | 498 | 104 | 20.8835 |
| 7 | 499 | 108 | 21.6433 |
| 8 | 500 | 114 | 22.8 |
| 9 | 498 | 121 | 24.2972 |
| 10 | 500 | 126 | 25.2 |

Complete rounds: mean 22.4089 %, sd 1.7502 pp, observed range 5.3603 pp.

## Headline

- single-run sd **1.276 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **3.5368 pp** before the gap is outside noise; 5.0556 pp for 80% power
- 225 of 500 tasks flipped; mean flip rate 0.1772 (max possible at n=10: 0.5556)
- re-run (plugin) sd 1.276 pp, (posterior) 1.4836 pp; bootstrap precision of this estimate 0.3958 pp
- leave-one-round-out keeps MDD in 3.4842–3.5487 pp

## Adjudicability

0 of 5000 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 5000}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| django__django-12050 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-12262 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13089 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13363 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13516 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-14089 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-14493 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-14500 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-15863 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-15987 | 5/9 | 0.5556 | 0.2667–0.8112 | 0.5556 |
| django__django-16493 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| scikit-learn__scikit-learn-13439 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| scikit-learn__scikit-learn-13496 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| scikit-learn__scikit-learn-25931 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| sympy__sympy-12481 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
