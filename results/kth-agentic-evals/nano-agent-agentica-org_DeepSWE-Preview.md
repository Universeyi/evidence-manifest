# Noise floor — KTH nano-agent-agentica-org_DeepSWE-Preview

5000 manifests, 500 tasks, rounds [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; outcomes {'completed': 4978, 'error': 22}; verifier versions ['swebench-harness-schema-v2']

## Per round (the assumption-free measurement)

| round | scored | passed | score % |
|---|---|---|---|
| 1 | 498 | 157 | 31.5261 |
| 2 | 497 | 156 | 31.3883 |
| 3 | 499 | 154 | 30.8617 |
| 4 | 499 | 161 | 32.2645 |
| 5 | 499 | 160 | 32.0641 |
| 6 | 497 | 158 | 31.7907 |
| 7 | 499 | 162 | 32.4649 |
| 8 | 496 | 158 | 31.8548 |
| 9 | 497 | 159 | 31.992 |
| 10 | 497 | 144 | 28.9738 |

Complete rounds: mean 31.5181 %, sd 1.0047 pp, observed range 3.4911 pp.

## Headline

- single-run sd **1.3309 pp** (basis: rerun.plugin (the measured tasks are the whole suite))
- two single runs must differ by **3.689 pp** before the gap is outside noise; 5.2731 pp for 80% power
- 258 of 499 tasks flipped; mean flip rate 0.1956 (max possible at n=10: 0.5556)
- re-run (plugin) sd 1.3309 pp, (posterior) 1.5426 pp; bootstrap precision of this estimate 0.4226 pp
- leave-one-round-out keeps MDD in 3.607–3.6843 pp

## Adjudicability

0 of 5000 verdicts have neither a retained observation nor a verifier reason; observations retained: {'per_step': 5000}.

## Drift screen

series (median completion tokens per round, {}): []

## Least stable tasks

| task | passes/n | pass rate | Wilson 95% | flip rate |
|---|---|---|---|---|
| sphinx-doc__sphinx-8475 | 4/8 | 0.5 | 0.2152–0.7848 | 0.5714 |
| django__django-11551 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-12276 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-13516 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-15368 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-16100 | 4/9 | 0.4444 | 0.1888–0.7333 | 0.5556 |
| django__django-16145 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-16661 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-16877 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| django__django-9296 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| matplotlib__matplotlib-13989 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| matplotlib__matplotlib-24149 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| matplotlib__matplotlib-24570 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| pydata__xarray-2905 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
| pydata__xarray-3677 | 5/10 | 0.5 | 0.2366–0.7634 | 0.5556 |
