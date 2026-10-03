# Drift screen on the KTH runs: did the endpoint move between the ten runs?

**Why this was checked.** The ten runs of each configuration were made over a few days
(A. Silva, 2026-09-07), and at temperature 0 the run-to-run sd of the suite score exceeds
the per-task Bernoulli floor most for the model served through a hosted API (Devstral,
Mistral's API; the others ran on local vLLM). A serving-side change between runs would
show as a step in the per-run median of the model's output volume, computed over the
same 500 instances in every run. The trajectory files carry a total token count per
instance, the tool-call count (steps), and the full model output, so output volume is
measured as **characters of assistant output per step** (the files have no separate
completion-token field). Screen: binary segmentation, as in `reference/detect_drift.py`.

## Result: no step

| configuration | serving | per-run median output chars per step (runs 1–10) | strongest single step | variance explained |
|---|---|---|---|---|
| Devstral-2, T=0 | hosted API | 1269 1239 1250 1259 1262 1246 1239 1244 1225 1204 | −2.9% after run 8 | 0.66 |
| Devstral-2, T=0.2 | hosted API | 1267 1242 1261 1270 1243 1233 1247 1245 1268 1261 | +1.1% after run 8 | 0.19 |
| Qwen3-32B, T=0 | local vLLM | 471 478 492 474 477 465 464 483 485 482 | +1.9% after run 7 | 0.23 |
| Qwen3-32B, T=0.6 | local vLLM | 474 481 480 485 477 473 494 477 479 462 | −2.1% after run 8 | 0.26 |
| DeepSWE, T=0 | local vLLM | 3997 4128 4302 4102 4181 4070 3995 4393 4151 4047 | +2.1% after run 7 | 0.10 |

For scale: the mid-run endpoint change in the MobileWorld audit was a −20% step with
0.95 of the variance explained. Nothing here is within a factor of five of that. The
largest movement is the hosted model's last run (steps per instance 56 against 62–65
before, output per run −9%), which is one run, not a regime. The total-tokens-per-step
and steps-per-instance series agree.

So the excess of the ten-run sd over the Bernoulli floor at temperature 0 is **not**
explained by a token-visible change in the endpoint. What remains is within-run
nondeterminism of the serving stack, which the next number shows is total.

## The other number: temperature 0 repeated nothing

Across the five configurations, 2,500 instances × 10 runs, the number of instances whose
model output had the same length in all ten runs is **0**. Median per-instance
coefficient of variation of output length across runs: 0.18–0.20 for Devstral (hosted),
0.43–0.57 for the local vLLM models. Temperature 0 on a 500-instance agentic suite did not
reproduce a single trajectory's length, on either kind of serving.

## Empty patches per run (a budget/failure signal the record does carry)

Devstral T=0: 3–12 of 500 per run; Qwen3-32B T=0: 55–88; DeepSWE T=0: 139–154. The
manifests score these as failures with reason `empty_patch`; they are one in three DeepSWE
runs.

*Computed 2026-09-07 from the `detailed_predictions.jsonl` files of the five configurations
(streamed, not kept). The extraction script is in this repository's history; the per-run
summaries are in `drift-screen.json`.*
