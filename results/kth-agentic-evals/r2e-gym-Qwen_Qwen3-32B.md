# Noise floor — KTH r2e-gym-Qwen_Qwen3-32B

5000 manifests, 500 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; outcomes {'completed': 4984, 'error': 16}; verifier versions ['swebench-harness-schema-v2']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 500 | 128 | 25.6 |
| 2 | 500 | 121 | 24.2 |
| 3 | 499 | 118 | 23.6473 |
| 4 | 497 | 132 | 26.5594 |
| 5 | 500 | 121 | 24.2 |
| 6 | 499 | 112 | 22.4449 |
| 7 | 497 | 115 | 23.1388 |
| 8 | 492 | 120 | 24.3902 |
| 9 | 500 | 121 | 24.2 |
| 10 | 500 | 107 | 21.4 |

Complete rounds: mean 23.9781 %, sd 1.469 pp, observed range 5.1594 pp.

## Headline

- single-run sd **1.2835 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **3.5576 pp** before the gap is outside noise; 5.0853 pp for 80% power
- 239 of 500 tasks flipped; mean flip rate 0.1806 (max possible at n=10: 0.5556)
- re-run (plugin) sd 1.2835 pp, (posterior) 1.4994 pp; bootstrap precision of this estimate 0.4032 pp
- leave-one-round-out keeps MDD in 3.4911–3.5507 pp

## Adjudicability

0 of 5000 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 5000}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| astropy__astropy-14539 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| astropy__astropy-14995 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-11532 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-11951 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-12050 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-12276 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-12713 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13449 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13569 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13821 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-14349 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-15380 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-15731 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-15814 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-16485 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
