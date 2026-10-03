# Noise floor — KTH r2e-gym-agentica-org__DeepSWE-preview

5000 manifests, 500 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; outcomes {'completed': 4978, 'error': 13, 'unknown': 9}; verifier versions ['swebench-harness-schema-v2']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 498 | 158 | 31.7269 |
| 2 | 499 | 173 | 34.6693 |
| 3 | 499 | 174 | 34.8697 |
| 4 | 499 | 185 | 37.0741 |
| 5 | 498 | 180 | 36.1446 |
| 6 | 500 | 171 | 34.2 |
| 7 | 498 | 166 | 33.3333 |
| 8 | 498 | 168 | 33.7349 |
| 9 | 491 | 178 | 36.2525 |
| 10 | 498 | 169 | 33.9357 |

Complete rounds: mean 34.5941 %, sd 1.582 pp, observed range 5.3472 pp.

## Headline

- single-run sd **1.2895 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **3.5742 pp** before the gap is outside noise; 5.1091 pp for 80% power
- 241 of 500 tasks flipped; mean flip rate 0.1827 (max possible at n=10: 0.5556)
- re-run (plugin) sd 1.2895 pp, (posterior) 1.4934 pp; bootstrap precision of this estimate 0.4038 pp
- leave-one-round-out keeps MDD in 3.4681–3.6114 pp

## Adjudicability

0 of 5000 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 5000}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| django__django-13012 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13343 | 4/9 | 0.4444 | 0.1888–0.7333 | 0.5556 |
| django__django-13569 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13809 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-14539 | 5/9 | 0.5556 | 0.2667–0.8112 | 0.5556 |
| django__django-14787 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-15278 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| matplotlib__matplotlib-13989 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| psf__requests-1724 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| psf__requests-5414 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| pydata__xarray-7233 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| pytest-dev__pytest-7205 | 5/9 | 0.5556 | 0.2667–0.8112 | 0.5556 |
| scikit-learn__scikit-learn-12973 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| scikit-learn__scikit-learn-25102 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| sphinx-doc__sphinx-8120 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
