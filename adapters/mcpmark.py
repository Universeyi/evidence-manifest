#!/usr/bin/env python3
"""MCPMark trajectory logs -> evidence-manifest, one manifest per task run.

MCPMark (eval-sys/mcpmark) evaluates agents that operate real services through
MCP servers: Notion, GitHub, Postgres, Playwright, a filesystem. The v1-0905
logs are on Hugging Face as `Jakumetsu/mcpmark-trajectory-log` (MIT): per
<model>__<service>/run-N/<task>/ a meta.json (verdict, timestamps, tokens,
turns, error), messages.json and execution.log. Only meta.json is read here.

What maps where:
  task_id                      <category>__<task> directory name
  run.repetition_index         run-N
  verdict.score                1.0 if execution_result.success else 0.0
  verdict.reason               verification_error / error_message, shortened
  outcome.reason               completed; budget_exhausted when the error is a
                               context-length limit or "Max turns exceeded";
                               error for other harness/API errors (no verdict,
                               excluded from denominators -- MCPMark's own
                               pass@1 counts them as failures; the difference
                               is a few dozen runs in 5,800)
  serving                      litellm model name; actual_model_name kept as
                               observed_provider when present (read back by
                               the harness from the API response)
  usage                        token_usage.output_tokens per run (input kept)
  artefacts.observations       per_step: messages.json is in the dataset

    python3 adapters/mcpmark.py mcpmark-v1-0905/ --out manifests/mcpmark/
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SRC = "https://huggingface.co/datasets/Jakumetsu/mcpmark-trajectory-log"
BUDGET = re.compile(r"maximum context|context len|prompt is too long|Input tokens exceed|ContextWindowExceeded|Max turns", re.I)


def classify(ex: dict) -> tuple[float | None, str | None, str]:
    if ex.get("success"):
        return 1.0, "success", "completed"
    em = ex.get("error_message")
    ve = ex.get("verification_error")
    if em:
        if BUDGET.search(str(em)):
            return 0.0, "budget: " + str(em)[:120], "budget_exhausted"
        return None, "harness/api error: " + str(em)[:120], "error"
    if ve:
        return 0.0, "verification: " + str(ve)[:160], "completed"
    return 0.0, "verification failed (no detail recorded)", "completed"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = Path(a.out)
    n = 0
    configs = set()
    for meta in sorted(Path(a.root).glob("*/run-*/*/meta.json")):
        cfg, run, task = meta.parts[-4], meta.parts[-3], meta.parts[-2]
        m = json.loads(meta.read_text())
        ex = m.get("execution_result") or {}
        score, reason, outcome = classify(ex)
        tu = m.get("token_usage") or {}
        t = m.get("time") or {}
        actual = m.get("actual_model_name")
        d = out / cfg
        d.mkdir(parents=True, exist_ok=True)
        configs.add(cfg)
        rep = int(run.split("-")[-1])
        mf = {
            "task_id": task,
            "serving": {"provider": f"{m.get('litellm_run_model_name') or m.get('model_name')} (litellm)",
                        "observed_provider": actual or "unrecorded",
                        "observed_provider_source": "response" if actual else "unrecorded"},
            "env": {"image_digest": "unrecorded", "taskset_commit": "unrecorded"},
            "run": {"repetition_index": rep, "total_repetitions": len(list(meta.parents[2].glob("run-*"))),
                    "started_at": t.get("start"), "ended_at": t.get("end")},
            "sampling": {},
            "steps": [],
            "verdict": {"criteria_version": "mcpmark-v1-0905", "score": score, "reason": reason,
                        "basis": "programmatic state verification"},
            "outcome": {"reason": outcome},
            "harness": {"silent_retries": 0},
            "artefacts": {"observations": "per_step", "location": f"{SRC}/tree/main/mcpmark-v1-0905/{cfg}/{run}/{task}"},
            "usage": ({"completion_tokens": int(tu["output_tokens"]), "prompt_tokens": int(tu.get("input_tokens") or 0),
                       "per_step_unavailable_reason": "meta.json carries run totals; per-turn usage is in messages.json"}
                      if tu.get("output_tokens") is not None else
                      {"completion_tokens": None, "prompt_tokens": None,
                       "per_step_unavailable_reason": "no token_usage in meta.json"}),
            "model": m.get("model_name"), "mcp": m.get("mcp"), "reasoning_effort": m.get("reasoning_effort"),
            "turn_count": m.get("turn_count"), "timeout_s": m.get("timeout"),
        }
        (d / f"{task}__r{rep:02d}.json").write_text(json.dumps(mf) + "\n")
        n += 1
    print(f"wrote {n} manifest(s) for {len(configs)} configuration(s) to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
