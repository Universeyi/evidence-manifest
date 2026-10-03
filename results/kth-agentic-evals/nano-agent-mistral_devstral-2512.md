# Noise floor — KTH nano-agent-mistral_devstral-2512

5000 manifests, 500 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; outcomes {'completed': 4999, 'error': 1}; verifier versions ['swebench-harness-schema-v2']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 500 | 322 | 64.4 |
| 2 | 500 | 325 | 65.0 |
| 3 | 500 | 317 | 63.4 |
| 4 | 500 | 318 | 63.6 |
| 5 | 500 | 309 | 61.8 |
| 6 | 500 | 309 | 61.8 |
| 7 | 500 | 321 | 64.2 |
| 8 | 500 | 321 | 64.2 |
| 9 | 499 | 313 | 62.7255 |
| 10 | 500 | 322 | 64.4 |

Complete rounds: mean 63.5525 %, sd 1.1167 pp, observed range 3.2 pp.

## Headline

- single-run sd **1.0893 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **3.0193 pp** before the gap is outside noise; 4.3158 pp for 80% power
- 181 of 500 tasks flipped; mean flip rate 0.1314 (max possible at n=10: 0.5556)
- re-run (plugin) sd 1.0893 pp, (posterior) 1.3483 pp; bootstrap precision of this estimate 0.3471 pp
- leave-one-round-out keeps MDD in 2.9825–3.0418 pp

## Adjudicability

0 of 5000 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 5000}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| django__django-11149 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-11239 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-11728 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-12774 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13315 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13346 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| pylint-dev__pylint-6386 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| pylint-dev__pylint-6528 | 4/9 | 0.4444 | 0.1888–0.7333 | 0.5556 |
| sphinx-doc__sphinx-7454 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| sympy__sympy-13031 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| sympy__sympy-13615 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| sympy__sympy-15017 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| sympy__sympy-18211 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| sympy__sympy-21379 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| astropy__astropy-14096 | 6/10 | 0.6 | 0.3127–0.8318 | 0.5333 |
