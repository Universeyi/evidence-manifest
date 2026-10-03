# Noise floor — KTH r2e-gym-agentica-org__DeepSWE-preview__temp0

5000 manifests, 500 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; outcomes {'completed': 4989, 'error': 11}; verifier versions ['swebench-harness-schema-v2']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 500 | 90 | 18.0 |
| 2 | 498 | 94 | 18.8755 |
| 3 | 500 | 95 | 19.0 |
| 4 | 497 | 95 | 19.1147 |
| 5 | 500 | 107 | 21.4 |
| 6 | 499 | 85 | 17.0341 |
| 7 | 498 | 93 | 18.6747 |
| 8 | 499 | 90 | 18.0361 |
| 9 | 499 | 101 | 20.2405 |
| 10 | 499 | 108 | 21.6433 |

Complete rounds: mean 19.2019 %, sd 1.4835 pp, observed range 4.6092 pp.

## Headline

- single-run sd **1.0721 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **2.9717 pp** before the gap is outside noise; 4.2477 pp for 80% power
- 174 of 500 tasks flipped; mean flip rate 0.1272 (max possible at n=10: 0.5556)
- re-run (plugin) sd 1.0721 pp, (posterior) 1.3396 pp; bootstrap precision of this estimate 0.333 pp
- leave-one-round-out keeps MDD in 2.9123–2.983 pp

## Adjudicability

0 of 5000 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 5000}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| django__django-13569 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-15380 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-15741 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-16595 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-7530 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| matplotlib__matplotlib-24149 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| matplotlib__matplotlib-25287 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| scikit-learn__scikit-learn-13328 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| sphinx-doc__sphinx-8475 | 4/9 | 0.4444 | 0.1888–0.7333 | 0.5556 |
| sympy__sympy-16450 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| sympy__sympy-21379 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| astropy__astropy-14995 | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| django__django-11099 | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
| django__django-11790 | 4/10 | 0.4 | 0.1682–0.6873 | 0.5333 |
| django__django-12050 | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
