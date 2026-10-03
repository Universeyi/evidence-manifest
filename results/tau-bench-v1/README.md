# tau-bench (v1): the noise floor of its historical trajectories

Sierra's first tau-bench repository ships four files under `historical_trajectories/` (2024-11-23):
tool-calling gpt-4o with four trials and claude-3-5-sonnet-20241022 with eight, on airline (50 tasks)
and retail (115 tasks). Converted by `adapters/taubench1.py`, analysed by `reference/analyze.py`
with `--measured-is-suite`. Zero compute.

| domain | agent | tasks | trials | per-round score % | range pp | single-run sd pp | MDD95 pp | tasks flipped | mean flip rate | leave-one-out MDD |
|---|---|---|---|---|---|---|---|---|---|---|
| airline | gpt-4o | 50 | 4 | [42.0, 44.0, 40.0, 42.0] | 4.0 | 4.67 | **12.9** | 26/50 | 0.293 | 11.4-12.8 |
| retail | gpt-4o | 115 | 4 | [61.7, 61.7, 60.0, 58.3] | 3.5 | 2.74 | **7.6** | 49/115 | 0.226 | 6.9-7.2 |
| airline | claude-3-5-sonnet-20241022 | 50 | 8 | [50.0, 40.0, 44.0, 48.0, 46.0, 46.0, 42.0, 52.0] | 12.0 | 4.85 | **13.4** | 32/50 | 0.269 | 12.9-13.6 |
| retail | claude-3-5-sonnet-20241022 | 115 | 8 | [73.0, 70.4, 70.4, 68.7, 70.4, 60.9, 74.8, 65.2] | 13.9 | 3.00 | **8.3** | 67/115 | 0.233 | 7.9-8.4 |

## How to read it

- **Eight repetitions show what four cannot.** With eight rounds of the same 115 retail tasks the
  suite score ranged from 60.9% to 74.8%; the same agent on airline ranged 40% to 52%. A single run
  anywhere in that band would have been reported as the number.
- **Airline needs a 13-point gap** between two single runs before it is outside noise; retail 8.
- **This is an indication of scale, not a re-scoring.** These are 2024 runs of two agents under the
  v1 evaluator; gaps below the MDD warrant a second run before citation, not a claim that two systems
  are equal. The noise includes the LLM user simulator.
- **The record is thin.** No timestamps, no token usage, no termination reason, no evaluator commit,
  and neither the agent nor the user-simulator model is named inside the file; the manifests carry
  `unrecorded` where the spec wants a value and take the model from the file name. Every field that
  is `unrecorded` here is one the later tau2-bench files do record, which is the direction the spec
  argues for.
