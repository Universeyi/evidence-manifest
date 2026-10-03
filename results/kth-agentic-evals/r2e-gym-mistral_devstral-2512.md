# Noise floor — KTH r2e-gym-mistral_devstral-2512

5000 manifests, 500 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; outcomes {'completed': 4999, 'error': 1}; verifier versions ['swebench-harness-schema-v2']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 500 | 172 | 34.4 |
| 2 | 500 | 184 | 36.8 |
| 3 | 500 | 179 | 35.8 |
| 4 | 500 | 169 | 33.8 |
| 5 | 500 | 171 | 34.2 |
| 6 | 500 | 177 | 35.4 |
| 7 | 500 | 170 | 34.0 |
| 8 | 500 | 161 | 32.2 |
| 9 | 499 | 179 | 35.8717 |
| 10 | 500 | 185 | 37.0 |

Complete rounds: mean 34.9472 %, sd 1.4926 pp, observed range 4.8 pp.

## Headline

- single-run sd **1.4768 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **4.0934 pp** before the gap is outside noise; 5.8511 pp for 80% power
- 305 of 500 tasks flipped; mean flip rate 0.2327 (max possible at n=10: 0.5556)
- re-run (plugin) sd 1.4768 pp, (posterior) 1.5866 pp; bootstrap precision of this estimate 0.462 pp
- leave-one-round-out keeps MDD in 4.0105–4.0607 pp

## Adjudicability

0 of 5000 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 5000}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| astropy__astropy-12907 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-11206 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-11292 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-12276 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-12708 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13023 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13028 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13089 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13401 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13551 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-14434 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-14559 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-16139 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| matplotlib__matplotlib-24570 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| psf__requests-2317 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
