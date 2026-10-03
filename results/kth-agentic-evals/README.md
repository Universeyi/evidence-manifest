# SWE-bench Verified, from the KTH "On Randomness in Agentic Evals" artefacts

Bjarnason, Silva and Monperrus (arXiv 2602.07150) ran two scaffolds x three models x two temperatures
on SWE-bench Verified, ten independent runs each, and published every run (`ASSERT-KTH/agentic-evals-artifacts`,
CC-BY-4.0). This is the closest prior work to the noise-floor question, and the one place where the
analyser can be checked against numbers someone else computed from the same runs. Converted by
`adapters/kth_agentic_evals.py` from the 120 SWE-bench harness results files (2.8 MB; the 3.4 GB of
trajectories were not needed). Zero compute.

## Reconciliation with the paper's Table 1

| scaffold | model | temp | mean % (ours / paper) | sd of 10 runs (ours / paper) | min-max (ours / paper) |
|---|---|---|---|---|---|
| R2E-Gym | DeepSWE-preview | 1.0 | 34.6 / 34.4 | 1.58 / 1.5 | 31.7-37.1 / 31.6-37.0 |
| R2E-Gym | Devstral-2 | 0.2 | 34.9 / 34.9 | 1.49 / 1.5 | 32.2-37.0 / 32.2-37.0 |
| R2E-Gym | Qwen3-32B | 0.6 | 24.0 / 23.9 | 1.47 / 1.4 | 21.4-26.6 / 21.4-26.4 |
| nano-agent | DeepSWE-preview | 1.0 | 31.5 / 31.4 | 1.00 / 1.0 | 29.0-32.5 / 28.8-32.4 |
| nano-agent | Devstral-2 | 0.2 | 63.6 / 63.5 | 1.12 / 1.1 | 61.8-65.0 / 61.8-65.0 |
| nano-agent | Qwen3-32B | 0.6 | 16.4 / 16.4 | 0.76 / 0.7 | 15.0-17.3 / 15.0-17.2 |
| R2E-Gym | DeepSWE-preview | 0.0 | 19.2 / 19.2 | 1.48 / 1.5 | 17.0-21.6 / 17.0-21.6 |
| R2E-Gym | Devstral-2 | 0.0 | 35.4 / 35.4 | 1.70 / 1.7 | 32.1-37.8 / 32.0-37.8 |
| R2E-Gym | Qwen3-32B | 0.0 | 22.4 / 22.3 | 1.75 / 1.8 | 19.8-25.2 / 19.8-25.2 |
| nano-agent | DeepSWE-preview | 0.0 | 20.4 / 20.4 | 0.96 / 1.0 | 18.3-21.5 / 18.2-21.4 |
| nano-agent | Devstral-2 | 0.0 | 63.8 / 63.8 | 1.65 / 1.6 | 60.6-66.6 / 60.6-66.6 |
| nano-agent | Qwen3-32B | 0.0 | 16.4 / 16.4 | 1.16 / 1.2 | 14.5-18.0 / 14.4-18.0 |

Every row agrees. The three means that differ by 0.1-0.2 points (DeepSWE at 1.0, Qwen3 on R2E-Gym) are the
denominator contract at work: the paper divides by 500, the analyser leaves harness-error instances
(`outcome.reason: error`, 1-22 per configuration) out of the denominator because they carry no verdict.
Stated here so that the agreement is exact rather than approximate.

## What the analyser adds to the same data

| scaffold | model | temp | single-run sd, Bernoulli (pp) | sd of 10 runs (pp) | ratio | MDD95 (pp) | tasks flipped | leave-one-out MDD |
|---|---|---|---|---|---|---|---|---|
| R2E-Gym | DeepSWE-preview | 1.0 | 1.29 | 1.58 | 1.23 | **3.6** | 241/500 (48%) | 3.5-3.6 |
| R2E-Gym | Devstral-2 | 0.2 | 1.48 | 1.49 | 1.01 | **4.1** | 305/500 (61%) | 4.0-4.1 |
| R2E-Gym | Qwen3-32B | 0.6 | 1.28 | 1.47 | 1.14 | **3.6** | 239/500 (48%) | 3.5-3.6 |
| nano-agent | DeepSWE-preview | 1.0 | 1.33 | 1.00 | 0.75 | **3.7** | 258/499 (52%) | 3.6-3.7 |
| nano-agent | Devstral-2 | 0.2 | 1.09 | 1.12 | 1.03 | **3.0** | 181/500 (36%) | 3.0-3.0 |
| nano-agent | Qwen3-32B | 0.6 | 1.00 | 0.76 | 0.76 | **2.8** | 150/500 (30%) | 2.7-2.8 |
| R2E-Gym | DeepSWE-preview | 0.0 | 1.07 | 1.48 | 1.38 | **3.0** | 174/500 (35%) | 2.9-3.0 |
| R2E-Gym | Devstral-2 | 0.0 | 1.48 | 1.70 | 1.15 | **4.1** | 308/500 (62%) | 4.0-4.1 |
| R2E-Gym | Qwen3-32B | 0.0 | 1.28 | 1.75 | 1.37 | **3.5** | 225/500 (45%) | 3.5-3.5 |
| nano-agent | DeepSWE-preview | 0.0 | 1.14 | 0.96 | 0.84 | **3.2** | 190/500 (38%) | 3.1-3.2 |
| nano-agent | Devstral-2 | 0.0 | 1.11 | 1.65 | 1.49 | **3.1** | 190/500 (38%) | 3.0-3.1 |
| nano-agent | Qwen3-32B | 0.0 | 0.98 | 1.16 | 1.18 | **2.7** | 144/500 (29%) | 2.7-2.7 |

- **MDD95 is 2.7 to 4.1 points on 500 tasks.** Smaller than the 7-13 seen on 50-115-task suites, as the
  1/sqrt(n) term predicts: scaled to 89 tasks these would read 6.5 to 9.7. The floor is a function
  of suite size and of the share of tasks that flip, not a constant.
- **Between 29% and 62% of the 500 tasks changed verdict** across ten identical runs, temperature 0 included.
- **The empirical sd of ten runs is 0.75 to 1.49 times the Bernoulli floor.** Where it exceeds 1 the runs carry
  variance beyond independent per-task coin flips; the two largest excesses are Devstral-2 at temperature 0
  (1.49) and Qwen3-32B on R2E-Gym at temperature 0 (1.37). Devstral-2 was the one model served through a
  hosted API rather than local vLLM (paper, section 2.1). This is where the first paper's detector -- completion
  tokens per run, which the trajectory files do carry -- would say whether the endpoint moved between runs. Not
  computed here; a hypothesis, stated as one.
- **Two temperatures, same floor.** Temperature 0 does not lower the Bernoulli sd or the flipped share in any
  of the six pairs; the paper's own point, reproduced from its own data.

## The record

- The harness results carry the verdict per instance and a schema version, not the harness commit, the
  per-instance image digest or the dataset revision: `criteria_version`, `image_digest` and `taskset_commit`
  are `unrecorded` in the manifests.
- Inside the DeepSWE directories the results files are named after other configurations (an R2E-Gym
  "temp_0.0" name in the nano-agent temperature-1.0 directory; nano-agent "preds" names in the R2E-Gym
  temperature-0 directory). The directory labels reproduce the paper's Table 1 run for run, the file names
  do not; the adapter trusts directories. Worth a note to the authors, and a case for the spec: a label
  inside the record beats a label on the path.
- The dataset README gives 0.6 as the non-zero temperature for all models; Table 1 gives 0.6 / 1.0 / 0.2 by
  model. The manifests follow the table.
- Trajectories (3.4 GB) hold per-message token usage and exit reasons; a second pass could fill `steps[]`
  and turn `empty_patch` into `budget_exhausted` where that is what happened.
