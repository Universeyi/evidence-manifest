# Terminal-Bench 2.0: the noise floor of its leaderboard, from the published trials

Terminal-Bench 2.0 requires at least five trials per task for every leaderboard entry and publishes the
per-trial results and trajectories. A complete scrape of the leaderboard is on Hugging Face as
`yoonholee/terminalbench-trajectories` (Apache-2.0): 52,104 trials, 108 (agent, model) configurations,
89 tasks. Converted by `adapters/terminalbench2.py`, analysed per configuration by `reference/analyze.py`
with `--measured-is-suite`. Zero compute. Per-configuration reports are in `reports/`; the numbers below
are in `summary.json`.

> **Scope.** The scrape keeps the verdict, run-level tokens and timestamps; it dropped the task git
> commit, checksum and exception info that the original per-trial `result.json` carries. Manifests say
> `unrecorded` for those. The leaderboard has been closed to submissions since 2026-05-14 pending an
> integrity process; nothing here is about that.

## Across 95 configurations with five complete rounds on all 89 tasks

| | min | p25 | median | p75 | max |
|---|---|---|---|---|---|
| MDD95, points between two single runs | 3.8 | 7.1 | **7.6** | 8.0 | 9.1 |
| single-run sd, pp | 1.38 | | 2.74 | | 3.29 |
| observed range over 5 rounds, pp | 1.1 | | 6.7 | | 15.7 |
| share of tasks that flipped | 0.09 | | 0.35 | | 0.52 |

**Adjacent entries.** The board ranks configurations by their five-round mean, so two neighbours are
separable when their gap exceeds the noise of those means, 1.96 × sqrt(sd_a²/5 + sd_b²/5). Ranking the
95 configurations by mean, **93 of 94 adjacent pairs** are closer than that: the median adjacent gap is
0.6 points against a median threshold of 3.5. With 95 entries spread over about sixty points this is
expected; the reading it supports is that the board orders tiers, not neighbours. The published board
reports a mean and an interval from the same five trials; what it does not say is which neighbours it
can and cannot separate.

*Corrected 2026-10-03.* An earlier version of this note compared the five-round means against
single-run noise, 1.96 × sqrt(sd_a² + sd_b²), and reported 94 of 94. Single-run noise is the right
scale for comparing two single runs (the MDD above), not two means.

## How to read it

- **This is an indication of scale, not a re-scoring.** Five trials per configuration; a gap below the MDD
  warrants more runs before citation, not a claim that two systems are equal.
- **The board already runs five trials and shows an interval.** That is more than most leaderboards do,
  and it is why this table could be computed at all. The addition is the pairwise reading.
- **Configurations, not models.** An (agent, model) pair is the unit; the same model under two scaffolds
  is two rows, as on the board itself.
- 13 configurations are left out of the summary: fewer than five complete rounds, or fewer than
  85 tasks with five trials. Their per-configuration reports are still in `reports/`.

## Every configuration

| agent | model | rounds | per-round score % | range | sd | MDD95 | flipped | LOO MDD |
|---|---|---|---|---|---|---|---|---|
| forge | gemini-3.1-pro-preview_Google | 5 | [79.8, 73.0, 80.9, 78.7, 79.8] | 7.8652 | 1.86 | 5.2 | 14/89 | 4.574-5.2257 |
| Factory_Droid | gpt-5.3-codex_openai | 5 | [77.5, 76.4, 76.4, 77.5, 78.7] | 2.2472 | 2.21 | 6.1 | 19/89 | 5.7975-6.1179 |
| terminus-3-3 † | claude-opus-4-6_anthropic | 2 | [71.9, 78.7] | 6.7416 | 2.48 | 6.9 | 24/89 | 6.1944-6.9037 |
| terminus-3-3 | gemini-3.1-pro-preview_Google | 5 | [73.0, 76.4, 74.2, 75.3, 75.3] | 3.3708 | 2.62 | 7.3 | 28/89 | 6.8037-7.3389 |
| simple_codex | gpt-5.3-codex_openai | 4 | [75.3, 73.0, 74.2, 75.3] | 2.2472 | 2.44 | 6.8 | 23/89 | 6.2831-6.7516 |
| judy | claude-opus-4.6_anthropic | 5 | [73.0, 75.3, 69.7, 68.5, 73.0] | 6.7416 | 2.72 | 7.6 | 32/89 | 7.0883-7.516 |
| ruley | gpt-5.3-codex_OpenAI | 5 | [67.4, 74.2, 73.0, 67.4, 69.7] | 6.7416 | 2.62 | 7.3 | 29/89 | 6.7563-7.2483 |
| Factory_Droid | claude-opus-4-6_anthropic | 5 | [68.5, 71.9, 68.5, 70.8, 69.7] | 3.3708 | 2.49 | 6.9 | 26/89 | 6.511-6.8234 |
| mux | gpt-5.3-codex_openai | 5 | [69.7, 73.0, 67.4, 68.5, 64.0] | 8.9888 | 2.46 | 6.8 | 24/89 | 6.0553-6.8871 |
| deepagent-harbor † | gpt-5.2-codex_openai | 2 | [66.3, 67.4] | 1.1236 | 2.93 | 8.1 | 35/89 | 7.5088-7.8675 |
| mux | claude-opus-4-6_anthropic | 5 | [68.5, 67.4, 64.0, 67.4, 65.2] | 4.4944 | 2.59 | 7.2 | 27/89 | 6.4608-7.2929 |
| ante | gemini-3-pro-preview_Google | 4 | [71.9, 70.8, 61.8, 60.7] | 11.2359 | 2.73 | 7.6 | 33/89 | 6.9312-7.5831 |
| Factory_Droid | gpt-5.2_openai | 4 | [65.2, 64.0, 67.4, 65.2] | 3.3708 | 2.86 | 7.9 | 33/89 | 7.4232-7.8204 |
| sage | gemini-3-pro-preview_Google | 5 | [64.0, 65.2, 68.5, 64.0, 64.0] | 4.4944 | 2.10 | 5.8 | 20/89 | 5.1933-6.1204 |
| terminus-2 | gpt-5.3-codex_openai | 5 | [59.6, 66.3, 66.3, 67.4, 64.0] | 7.8651 | 2.78 | 7.7 | 32/89 | 7.1618-7.6191 |
| Junie | gemini-3-flash-preview_gemini | 5 | [68.5, 62.9, 66.3, 66.3, 57.3] | 11.2359 | 2.86 | 7.9 | 33/89 | 7.0337-8.0712 |
| Factory_Droid | claude-opus-4-5-20251101_anthropic | 5 | [62.9, 65.2, 61.8, 62.9, 62.9] | 3.3707 | 2.74 | 7.6 | 30/89 | 7.154-7.572 |
| codex | gpt-5.2_openai | 5 | [59.6, 67.4, 60.7, 58.4, 68.5] | 10.1123 | 3.07 | 8.5 | 37/89 | 8.0155-8.3492 |
| terminus-2 | claude-opus-4-6_anthropic | 5 | [67.4, 59.6, 62.9, 65.2, 59.6] | 7.8651 | 2.73 | 7.6 | 30/89 | 6.9991-7.7173 |
| ruley | gemini-3-pro-preview_Google | 5 | [62.9, 62.9, 60.7, 62.9, 61.8] | 2.2471 | 2.67 | 7.4 | 27/89 | 6.8292-7.2871 |
| ii-agent-simple | gemini-3-pro-preview_gemini | 5 | [66.3, 61.8, 60.7, 56.2, 64.0] | 10.1123 | 2.88 | 8.0 | 35/89 | 7.5576-7.9279 |
| Factory_Droid | gemini-3-pro-preview_google | 5 | [64.0, 59.6, 59.6, 62.9, 59.6] | 4.4943 | 2.84 | 7.9 | 33/89 | 7.3824-7.7924 |
| mux † | gpt-5.2_openai | 1 | [60.7] | 0.0 | 0.00 | 0.0 | 0/0 | None-None |
| codex | gpt-5.1-codex-max_openai | 5 | [58.4, 57.3, 62.9, 64.0, 59.6] | 6.7415 | 2.69 | 7.5 | 29/89 | 7.1116-7.6385 |
| letta-code | claude-opus-4-5_anthropic | 5 | [60.7, 59.6, 58.4, 58.4, 58.4] | 2.2472 | 2.46 | 6.8 | 24/89 | 6.3078-6.9062 |
| mux † | claude-opus-4-5_anthropic | 1 | [58.4] | 0.0 | 0.00 | 0.0 | 0/0 | None-None |
| claude-code | claude-opus-4-6_anthropic | 5 | [57.3, 56.2, 58.4, 56.2, 61.8] | 5.618 | 2.96 | 8.2 | 35/89 | 7.6765-8.11 |
| codex | gpt-5.1-codex_openai | 5 | [60.7, 61.8, 59.6, 56.2, 50.6] | 11.236 | 3.01 | 8.3 | 38/89 | 7.4212-8.4163 |
| terminus-2 | claude-opus-4-5-20251101_anthropic | 5 | [57.3, 55.1, 62.9, 58.4, 55.1] | 7.8651 | 2.59 | 7.2 | 28/89 | 6.6346-7.2463 |
| terminus-2 | gemini-3-pro-preview_gemini | 5 | [58.4, 51.7, 57.3, 58.4, 58.4] | 6.7416 | 2.51 | 7.0 | 25/89 | 6.5742-6.8527 |
| letta-code | gemini-3-pro-preview_google | 5 | [56.2, 57.3, 56.2, 53.9, 56.2] | 3.3708 | 3.01 | 8.4 | 35/89 | 7.8675-8.2741 |
| goose | claude-opus-4-5_anthropic | 4 | [55.1, 53.9, 53.9, 51.7] | 3.3708 | 2.69 | 7.5 | 29/89 | 6.8441-7.6108 |
| terminus-2 | gpt-5.2_openai | 4 | [55.1, 46.1, 57.3, 56.2] | 11.236 | 2.93 | 8.1 | 35/89 | 7.6912-7.9958 |
| letta-code | gpt-5.1-codex_openai | 5 | [53.9, 53.9, 53.9, 53.9, 51.7] | 2.2472 | 2.88 | 8.0 | 32/89 | 7.3927-7.9498 |
| claude-code | claude-opus-4-5-20251101_anthropic | 5 | [53.9, 50.6, 48.3, 55.1, 52.8] | 6.7416 | 2.57 | 7.1 | 28/89 | 6.5911-7.2652 |
| openhands | claude-opus-4-5-20251101_anthropic | 5 | [55.1, 55.1, 46.1, 57.3, 46.1] | 11.236 | 2.97 | 8.2 | 37/89 | 7.6862-8.2456 |
| claude-code-enhanced † | claude-opus-4-6_anthropic | 1 | [51.7] | 0.0 | 3.69 | 10.2 | 52/87 | 9.3269-10.2338 |
| opencode † | claude-opus-4-5_anthropic | 1 | [51.7] | 0.0 | 0.00 | 0.0 | 0/0 | None-None |
| terminus-2 | gemini-3-flash-preview_gemini | 5 | [51.7, 51.7, 52.8, 51.7, 50.6] | 2.2472 | 3.21 | 8.9 | 39/89 | 8.0255-8.8656 |
| terminus-2 † | glm-5_z-ai | 3 | [56.2, 49.4, 49.4] | 6.7416 | 2.65 | 7.4 | 31/89 | 6.7457-7.7137 |
| gemini-cli | gemini-3-flash-preview_Google | 5 | [48.3, 52.8, 55.1, 49.4, 49.4] | 6.7416 | 3.05 | 8.5 | 34/89 | 7.9642-8.2289 |
| codex | gpt-5_openai | 4 | [47.2, 51.7, 48.3, 50.6] | 4.4944 | 2.88 | 8.0 | 33/89 | 7.4587-7.941 |
| terminus-2 | gpt-5.1_openai | 4 | [50.6, 51.7, 44.9, 43.8] | 7.8652 | 2.86 | 7.9 | 33/89 | 7.3846-8.0069 |
| TerminalBenchAgent | claude-sonnet-4-5_anthropic | 5 | [47.2, 47.2, 49.4, 41.6, 47.2] | 7.8652 | 2.41 | 6.7 | 24/89 | 6.1947-6.7829 |
| codex | gpt-5-codex_openai | 4 | [42.7, 44.9, 46.1, 44.9] | 3.3708 | 2.69 | 7.4 | 29/89 | 7.0254-7.3137 |
| openhands | gpt-5_openai | 5 | [46.1, 44.9, 47.2, 43.8, 37.1] | 10.1123 | 3.04 | 8.4 | 38/89 | 7.9507-8.3947 |
| terminus-2 † | kimi-k2.5_kimi | 3 | [41.6, 44.9, 44.9] | 3.3708 | 2.89 | 8.0 | 34/89 | 7.6028-7.936 |
| openhands | claude-sonnet-4-5-20250929_anthropic | 4 | [39.3, 41.6, 51.7, 40.4] | 12.3596 | 2.79 | 7.7 | 32/89 | 7.1316-7.727 |
| codex | gpt-5.1-codex-mini_openai | 5 | [40.4, 39.3, 48.3, 46.1, 41.6] | 8.9888 | 3.07 | 8.5 | 37/89 | 7.8872-8.6267 |
| goose | claude-sonnet-4-5_anthropic | 5 | [42.7, 49.4, 38.2, 44.9, 40.4] | 11.236 | 2.65 | 7.3 | 29/89 | 6.9223-7.3608 |
| terminus-2 | gpt-5-codex_openai | 4 | [46.1, 42.7, 37.1, 46.1] | 8.9887 | 2.88 | 8.0 | 37/89 | 7.4431-7.9947 |
| mini-swe-agent | claude-sonnet-4-5-20250929_anthropic | 4 | [43.8, 41.6, 47.2, 39.3] | 7.8652 | 2.85 | 7.9 | 31/89 | 7.0983-7.9024 |
| mini-swe-agent | gpt-5-codex_openai | 4 | [47.2, 43.8, 41.6, 38.2] | 8.9888 | 2.84 | 7.9 | 32/89 | 7.3808-7.9712 |
| final † | claude-4.5-sonnet_anthropic | 1 | [42.7] | 0.0 | 0.00 | 0.0 | 0/87 | 0.0-0.0 |
| terminus-2 | claude-sonnet-4-5-20250929_anthropic | 4 | [41.6, 39.3, 46.1, 42.7] | 6.7416 | 2.83 | 7.8 | 33/89 | 7.4656-7.6959 |
| terminus-2 | minimax-m2.5_Minimax | 5 | [41.6, 40.4, 48.3, 37.1, 43.8] | 11.2359 | 2.67 | 7.4 | 29/89 | 6.9996-7.4548 |
| claude-code | claude-sonnet-4-5-20250929_anthropic | 4 | [44.9, 40.4, 37.1, 38.2] | 7.8651 | 2.91 | 8.1 | 35/89 | 7.4728-8.082 |
| terminus-2 | deepseek-v3.2_deepseek | 5 | [43.8, 37.1, 38.2, 36.0, 42.7] | 7.8651 | 2.81 | 7.8 | 33/89 | 7.2117-7.8595 |
| terminus-2 | claude-opus-4-1-20250805_anthropic | 4 | [38.2, 36.0, 41.6, 38.2] | 5.6179 | 2.66 | 7.4 | 29/89 | 6.5922-7.5515 |
| terminus-2 | gpt-5.1-codex_openai | 5 | [37.1, 31.5, 37.1, 44.9, 33.7] | 13.4831 | 3.29 | 9.1 | 46/89 | 8.6364-9.0436 |
| openhands | claude-opus-4-1-20250805_anthropic | 5 | [34.8, 34.8, 36.0, 40.4, 38.2] | 5.6179 | 2.74 | 7.6 | 30/89 | 6.9248-7.7541 |
| claude-code | minimax-m2.1_minimax | 5 | [39.3, 32.6, 39.3, 37.1, 34.8] | 6.7415 | 2.98 | 8.3 | 34/89 | 7.3938-8.2361 |
| terminus-2 | gpt-5_openai | 4 | [37.1, 39.3, 34.8, 32.6] | 6.7415 | 3.12 | 8.7 | 36/89 | 7.8852-8.5455 |
| terminus-2 | moonshotai_Kimi-K2-Thinking_together_ai | 10 | [37.1, 39.3, 32.6, 32.6, 37.1, 33.7, 34.8, 36.0, 37.1, 37.1] | 6.7415 | 2.89 | 8.0 | 36/89 | 7.8547-8.059 |
| claude-code | claude-opus-4-1-20250805_anthropic | 4 | [34.8, 38.2, 36.0, 33.7] | 4.4943 | 2.89 | 8.0 | 32/89 | 7.3065-8.0502 |
| mini-swe-agent | claude-opus-4-1-20250805_anthropic | 4 | [31.5, 37.1, 36.0, 38.2] | 6.7415 | 2.56 | 7.1 | 26/89 | 6.5082-7.1995 |
| goose | claude-haiku-4-5_anthropic | 5 | [34.8, 40.4, 36.0, 36.0, 30.3] | 10.1123 | 2.97 | 8.2 | 34/89 | 7.6754-8.1328 |
| spoox-m | gpt-5-mini_openai | 5 | [40.4, 34.8, 33.7, 29.2, 36.0] | 11.2359 | 2.77 | 7.7 | 30/89 | 7.2341-7.7178 |
| mini-swe-agent | gpt-5_openai | 5 | [36.0, 33.7, 34.8, 32.6, 32.6] | 3.3708 | 2.98 | 8.3 | 34/89 | 7.7857-8.3074 |
| claude-code | GLM-4.7_z-ai | 5 | [31.5, 34.8, 32.6, 30.3, 37.1] | 6.7416 | 2.49 | 6.9 | 27/89 | 6.1856-6.9475 |
| terminus-2 † | glm-4.7_z-ai | 3 | [38.2, 30.3, 29.2] | 8.9887 | 2.79 | 7.7 | 30/89 | 7.1604-7.6807 |
| codex | gpt-5-mini_openai | 4 | [32.6, 33.7, 33.7, 28.1] | 5.618 | 2.98 | 8.3 | 36/89 | 7.518-8.3182 |
| terminus-2 | gemini-2.5-pro_gemini | 4 | [23.6, 39.3, 31.5, 33.7] | 15.7303 | 3.07 | 8.5 | 38/89 | 8.1535-8.4177 |
| terminus-2 † | minimax-m2.1_openai | 2 | [32.6, 29.2] | 3.3708 | 2.98 | 8.3 | 35/89 | 7.7985-8.158 |
| terminus-2 | accounts_fireworks_models_minimax-m2_fireworks_ai | 10 | [34.8, 27.0, 30.3, 30.3, 29.2, 30.3, 29.2, 29.2, 29.2, 31.5] | 7.8652 | 2.84 | 7.9 | 31/89 | 7.7101-7.9775 |
| mini-swe-agent | claude-haiku-4-5-20251001_anthropic | 4 | [29.2, 30.3, 29.2, 30.3] | 1.1236 | 2.55 | 7.1 | 26/89 | 6.4666-7.0634 |
| openhands | gpt-5-mini_openai | 5 | [30.3, 30.3, 30.3, 25.8, 29.2] | 4.4944 | 2.76 | 7.7 | 31/89 | 7.3012-7.8256 |
| claude-code | claude-haiku-4-5-20251001_anthropic | 4 | [31.5, 28.1, 31.5, 24.7] | 6.7416 | 2.77 | 7.7 | 31/89 | 7.2147-7.5088 |
| terminus-2 | moonshotai_Kimi-K2-Instruct-0905_together_ai | 9 | [23.6, 27.0, 33.7, 24.7, 29.2, 32.6, 23.6, 27.0, 30.3] | 10.1124 | 2.64 | 7.3 | 27/89 | 7.2214-7.3561 |
| openhands | moonshotai_Kimi-K2-Instruct-0905_together_ai | 8 | [30.3, 30.3, 27.0, 23.6, 27.0, 29.2, 25.8, 30.3] | 6.7416 | 2.72 | 7.5 | 29/89 | 7.3777-7.6069 |
| openhands | grok-4-0709_xai | 4 | [30.3, 27.0, 25.8, 28.1] | 4.4944 | 3.10 | 8.6 | 38/89 | 7.8631-8.599 |
| terminus-2 | claude-haiku-4-5-20251001_anthropic | 4 | [28.1, 30.3, 30.3, 21.3] | 8.9888 | 2.90 | 8.0 | 32/89 | 7.4659-7.9839 |
| mini-swe-agent | gemini-2.5-pro_gemini | 4 | [32.6, 23.6, 22.5, 24.7] | 10.1124 | 2.63 | 7.3 | 29/89 | 6.9589-7.2061 |
| mini-swe-agent | grok-code-fast-1_xai | 5 | [27.0, 21.3, 28.1, 25.8, 27.0] | 6.7416 | 2.65 | 7.4 | 30/89 | 6.8392-7.4337 |
| mini-swe-agent | grok-4-0709_xai | 5 | [28.1, 23.6, 28.1, 19.1, 28.1] | 8.9888 | 2.99 | 8.3 | 36/89 | 7.6968-8.2849 |
| terminus-2 | gpt-5-mini_openai | 4 | [21.3, 29.2, 30.3, 20.2] | 10.1124 | 2.59 | 7.2 | 27/89 | 6.5351-7.2802 |
| openhands | Qwen_Qwen3-Coder-480B-A35B-Instruct-FP8_together_ai | 6 | [27.0, 28.1, 24.7, 25.8, 21.3, 23.6] | 6.7416 | 2.63 | 7.3 | 28/89 | 7.1962-7.3835 |
| terminus-2 | accounts_fireworks_models_glm-4p6_fireworks_ai | 8 | [23.6, 22.5, 30.3, 21.3, 27.0, 27.0, 22.5, 24.7] | 8.9888 | 2.51 | 7.0 | 27/89 | 6.8433-7.0756 |
| aone-agent † | Qwen_Qwen3-Coder-480B-A35B-Instruct-FP8_modelscope | 2 | [25.8, 23.6] | 2.2472 | 2.60 | 7.2 | 28/89 | 6.5401-7.2203 |
| terminus-2 | Qwen_Qwen3-Coder-480B-A35B-Instruct-FP8_together_ai | 9 | [23.6, 21.3, 27.0, 24.7, 22.5, 22.5, 19.1, 25.8, 30.3] | 11.236 | 2.93 | 8.1 | 34/89 | 7.9695-8.1918 |
| mini-swe-agent | gpt-5-mini_openai | 5 | [24.7, 25.8, 21.3, 18.0, 21.3] | 7.8652 | 2.67 | 7.4 | 30/89 | 7.049-7.3439 |
| terminus-2 | grok-4-0709_xai | 4 | [19.1, 20.2, 27.0, 21.3] | 7.8652 | 2.97 | 8.2 | 35/89 | 7.8376-8.0973 |
| gemini-cli | gemini-2.5-pro_gemini | 4 | [24.7, 21.3, 18.0, 18.0] | 6.7416 | 2.90 | 8.1 | 35/89 | 7.268-7.9584 |
| terminus-2 | openai_gpt-oss-120b_together_ai | 8 | [18.0, 12.4, 20.2, 20.2, 21.3, 23.6, 18.0, 19.1] | 11.2359 | 2.78 | 7.7 | 33/89 | 7.5626-7.8001 |
| terminus-2 † | gemini-2.5-flash_gemini | 3 | [16.9, 19.1, 18.0] | 2.2472 | 2.43 | 6.7 | 23/89 | 6.0667-6.764 |
| mini-swe-agent | gemini-2.5-flash_gemini | 5 | [13.5, 16.9, 24.7, 15.7, 14.6] | 11.236 | 2.54 | 7.0 | 27/89 | 6.4109-7.1951 |
| openhands | gemini-2.5-pro_gemini | 5 | [19.1, 12.4, 20.2, 15.7, 14.6] | 7.8651 | 2.82 | 7.8 | 32/89 | 7.0459-7.896 |
| openhands | gemini-2.5-flash_gemini | 5 | [15.7, 15.7, 18.0, 15.7, 16.9] | 2.2472 | 2.44 | 6.8 | 25/89 | 6.2125-6.8538 |
| gemini-cli | gemini-2.5-flash_gemini | 4 | [19.1, 12.4, 11.2, 16.9] | 7.8651 | 2.32 | 6.4 | 22/89 | 5.4738-6.6094 |
| openhands | claude-haiku-4-5-20251001_anthropic | 4 | [18.0, 15.7, 10.1, 13.5] | 7.8651 | 2.79 | 7.7 | 32/89 | 7.2294-7.8936 |
| mini-swe-agent | openai_gpt-oss-120b_together_ai | 9 | [15.7, 11.2, 11.2, 18.0, 14.6, 12.4, 14.6, 13.5, 16.9] | 6.7415 | 2.31 | 6.4 | 21/89 | 6.2036-6.4603 |
| terminus-2 | grok-code-fast-1_xai | 5 | [15.7, 11.2, 14.6, 13.5, 15.7] | 4.4943 | 2.59 | 7.2 | 27/89 | 6.8028-7.1665 |
| codex | gpt-5-nano_openai | 4 | [10.1, 10.1, 11.2, 13.5] | 3.3707 | 2.32 | 6.4 | 22/89 | 5.9026-6.4162 |
| openhands | gpt-5-nano_openai | 4 | [12.4, 12.4, 10.1, 3.4] | 8.9888 | 2.16 | 6.0 | 18/89 | 5.5317-5.9688 |
| terminus-2 | gpt-5-nano_openai | 4 | [7.9, 7.9, 10.1, 5.6] | 4.4944 | 1.92 | 5.3 | 15/89 | 4.8351-5.4436 |
| mini-swe-agent | gpt-5-nano_openai | 5 | [6.7, 10.1, 4.5, 7.9, 5.6] | 5.618 | 1.95 | 5.4 | 16/89 | 5.0136-5.6265 |
| mini-swe-agent | openai_gpt-oss-20b_together_ai | 9 | [7.9, 2.2, 2.2, 3.4, 1.1, 2.2, 4.5, 1.1, 4.5] | 6.7416 | 1.38 | 3.8 | 8/89 | 3.5831-3.9152 |
| terminus-2 | openai_gpt-oss-20b_together_ai | 10 | [2.2, 2.2, 4.5, 4.5, 2.2, 3.4, 3.4, 1.1, 3.4, 2.2] | 3.3708 | 1.57 | 4.4 | 11/89 | 4.1899-4.4022 |

† not in the summary (see above).
