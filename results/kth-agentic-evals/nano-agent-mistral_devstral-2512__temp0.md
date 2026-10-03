# Noise floor — KTH nano-agent-mistral_devstral-2512__temp0

5000 manifests, 500 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; outcomes {'completed': 4998, 'error': 2}; verifier versions ['swebench-harness-schema-v2']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 500 | 318 | 63.6 |
| 2 | 500 | 333 | 66.6 |
| 3 | 499 | 325 | 65.1303 |
| 4 | 500 | 324 | 64.8 |
| 5 | 499 | 316 | 63.3267 |
| 6 | 500 | 320 | 64.0 |
| 7 | 500 | 316 | 63.2 |
| 8 | 500 | 312 | 62.4 |
| 9 | 500 | 324 | 64.8 |
| 10 | 500 | 303 | 60.6 |

Complete rounds: mean 63.8457 %, sd 1.6483 pp, observed range 6.0 pp.

## Headline

- single-run sd **1.1058 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **3.0651 pp** before the gap is outside noise; 4.3812 pp for 80% power
- 190 of 500 tasks flipped; mean flip rate 0.1369 (max possible at n=10: 0.5556)
- re-run (plugin) sd 1.1058 pp, (posterior) 1.3737 pp; bootstrap precision of this estimate 0.348 pp
- leave-one-round-out keeps MDD in 3.0343–3.085 pp

## Adjudicability

0 of 5000 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 5000}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| django__django-11149 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13112 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13315 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13568 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13964 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-14140 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-15563 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-16661 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| matplotlib__matplotlib-20826 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| matplotlib__matplotlib-24177 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| matplotlib__matplotlib-25332 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| psf__requests-2931 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| pylint-dev__pylint-6528 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| sphinx-doc__sphinx-7454 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| sphinx-doc__sphinx-8621 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
