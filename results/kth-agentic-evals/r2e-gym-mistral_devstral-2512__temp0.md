# Noise floor — KTH r2e-gym-mistral_devstral-2512__temp0

5000 manifests, 500 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; outcomes {'completed': 4996, 'error': 4}; verifier versions ['swebench-harness-schema-v2']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 500 | 170 | 34.0 |
| 2 | 499 | 160 | 32.0641 |
| 3 | 499 | 175 | 35.0701 |
| 4 | 499 | 184 | 36.8737 |
| 5 | 500 | 173 | 34.6 |
| 6 | 499 | 183 | 36.6733 |
| 7 | 500 | 184 | 36.8 |
| 8 | 500 | 173 | 34.6 |
| 9 | 500 | 177 | 35.4 |
| 10 | 500 | 189 | 37.8 |

Complete rounds: mean 35.3881 %, sd 1.6993 pp, observed range 5.7359 pp.

## Headline

- single-run sd **1.4776 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **4.0956 pp** before the gap is outside noise; 5.8543 pp for 80% power
- 308 of 500 tasks flipped; mean flip rate 0.2383 (max possible at n=10: 0.5556)
- re-run (plugin) sd 1.4776 pp, (posterior) 1.6301 pp; bootstrap precision of this estimate 0.4616 pp
- leave-one-round-out keeps MDD in 4.0241–4.1017 pp

## Adjudicability

0 of 5000 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 5000}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| astropy__astropy-13579 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| astropy__astropy-14539 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| astropy__astropy-7336 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-10973 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-12039 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-12713 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13012 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13279 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13809 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13837 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-14580 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-14765 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-15127 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-16145 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| matplotlib__matplotlib-23314 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
