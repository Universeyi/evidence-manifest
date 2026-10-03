# MCPMark: the noise floor of its published trajectory logs

MCPMark (eval-sys/mcpmark) has agents operate real services through MCP servers: Notion, GitHub,
Postgres, Playwright and a filesystem, with programmatic verification of the resulting state. The
v1-0905 logs are on Hugging Face as `Jakumetsu/mcpmark-trajectory-log` (MIT): 116 (model, service)
configurations, four runs each for 110 of them, per-run meta.json with verdict, timestamps, tokens,
turns and errors. Converted by `adapters/mcpmark.py` from the 11,314 meta.json files (the messages
and execution logs were not needed), analysed per configuration by `reference/analyze.py` with
`--measured-is-suite`. Zero compute. Per-configuration reports are in `reports/`; the numbers below
are in `summary.json`.

> **Scope.** These are the v1-0905 logs; MCPMark has since released a verified task set. Nothing here
> is about the current benchmark.

## Across 67 configurations with four complete rounds and a non-zero score

| | min | p25 | median | p75 | max |
|---|---|---|---|---|---|
| MDD95, points between two single runs | 0.0 | 9.4 | **11.5** | 13.5 | 20.4 |
| share of tasks that flipped | 0.00 | | 0.22 | | 0.57 |
| observed range over 4 rounds, pp | | | 9.5 | | 21.9 |

| service | configurations | tasks | MDD95 median | MDD95 range | flipped share, median |
|---|---|---|---|---|---|
| filesystem | 16 | 30 | 11.0 | 0.0-15.1 | 0.23 |
| github | 12 | 23 | 11.0 | 5.1-12.4 | 0.17 |
| notion | 14 | 28 | 10.7 | 4.9-15.3 | 0.21 |
| playwright | 9 | 25 | 12.0 | 4.8-13.7 | 0.24 |
| postgres | 16 | 21 | 14.9 | 0.0-20.4 | 0.29 |

## How to read it

- **Small suites, wide floors.** With 21 to 30 tasks per service, two single runs must differ by about 11
  points before the gap is outside noise, and by 14 on Postgres. The widest four-round range is 22 points
  for one configuration on the filesystem service. This is the 1/sqrt(n) term at n = 25.
- **This is an indication of scale, not a re-scoring.** Four trials per configuration; a gap below the MDD
  warrants more runs before citation, not a claim that two systems are equal.
- **The leaderboard reports pass@1 averaged over the four runs and pass^4**, i.e. it already runs repeats;
  what it does not report is an interval per entry.
- **Budget and errors.** 409 of 11314 runs ended at a context-length or turn limit
  (`budget_exhausted`, scored 0); 559 ended in a harness or API error and carry no verdict, so they
  are outside the denominators here while MCPMark's own pass@1 counts them as failures. The difference
  is under 5% of runs.
- **49 configurations are left out of the summary**: fewer than four complete rounds (the seven
  single-run configurations), or a score of zero on every run (nothing to flip). Their reports are in `reports/`.

## The record

- meta.json carries `actual_model_name`, the model id read back from the API response: the first public
  record in this collection where `serving.observed_provider` has a source of `response` rather than
  `unrecorded`. It does not carry the image digest or a task-set commit; `criteria_version` is the
  release label `mcpmark-v1-0905`.
- Per-turn token usage is in messages.json (not fetched); meta.json has run totals, so the drift screen
  runs on run-level output tokens.
