#!/usr/bin/env python3
"""tau2-bench results file -> evidence-manifest, one manifest per simulation.

tau2-bench (Sierra) publishes its baseline runs as one JSON per
(agent model, domain, config): `info` (git commit, trial count, agent and user
LLM settings) and `simulations[]`, each with task_id, trial, timestamps,
termination_reason, reward_info and the full message list with per-message
token usage. That is nearly everything the spec asks for, which is why it is
the second adapter.

What maps where, and what cannot be filled:
  task_id                      simulation.task_id
  run.repetition_index         simulation.trial + 1; total from info.num_trials
  verdict.score / reason       reward_info.reward; reason assembled from the
                               db / communicate / action / nl-assertion checks
  verdict.criteria_version     info.git_commit -- the evaluator that scored it
  outcome.reason               termination_reason: user_stop / agent_stop ->
                               completed; max_steps -> budget_exhausted;
                               too_many_errors -> error; anything else unknown
  steps[].completion_tokens    one per assistant message that carries usage
  serving.*                    the agent LLM id is known; provider is the
                               vendor's own API and is NOT read back from any
                               response, so observed_provider is 'unrecorded'
  env.image_digest             'not_containerized' -- a tool-calling text
                               environment, no image
  artefacts.observations       per_step: the conversation is the observation;
                               location is the published results file

    python3 adapters/tau2bench.py results.json --out manifests/ [--source-url URL]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

TERMINATION = {"user_stop": "completed", "agent_stop": "completed", "max_steps": "budget_exhausted",
               "too_many_errors": "error"}


def reason_of(ri: dict) -> str:
    parts = []
    db = ri.get("db_check") or {}
    if db:
        parts.append(f"db_match={db.get('db_match')}")
    cc = ri.get("communicate_checks") or []
    if cc:
        parts.append(f"communicate={sum(1 for c in cc if c.get('met'))}/{len(cc)}")
    ac = ri.get("action_checks") or []
    if ac:
        parts.append(f"actions={sum(1 for c in ac if c.get('action_match'))}/{len(ac)}")
    nl = ri.get("nl_assertions") or []
    if nl:
        parts.append(f"nl_assertions={sum(1 for c in nl if c.get('met') or c.get('metExpectation'))}/{len(nl)}")
    ea = ri.get("env_assertions") or []
    if ea:
        parts.append(f"env_assertions={sum(1 for c in ea if c.get('met'))}/{len(ea)}")
    basis = ri.get("reward_basis")
    if basis:
        parts.append("basis=" + "+".join(basis))
    return "; ".join(parts) or None


def basis_of(ri: dict) -> str | None:
    """What decided the verdict: the declared reward_basis, plus ':nl' when an
    LLM-judged natural-language assertion was actually evaluated for this run.
    Lets a consumer compare instability across verifier kinds."""
    b = ri.get("reward_basis") or []
    if not b:
        return None
    s = "+".join(b)
    if ri.get("nl_assertions"):
        s += ":nl"
    return s


def to_manifest(sim: dict, info: dict, src: str, model: str) -> dict:
    ri = sim.get("reward_info") or {}
    steps = []
    for m in sim.get("messages") or []:
        u = m.get("usage")
        if m.get("role") == "assistant" and isinstance(u, dict) and u.get("completion_tokens") is not None:
            steps.append({"completion_tokens": int(u["completion_tokens"]),
                          "prompt_tokens": int(u.get("prompt_tokens") or 0)})
    agent = (info.get("agent_info") or {})
    llm_args = agent.get("llm_args") or {}
    term = sim.get("termination_reason")
    m = {
        "task_id": str(sim["task_id"]),
        "serving": {"provider": (model.split("/")[0] + " (vendor api)") if "/" in model else "vendor-api",
                    "observed_provider": "unrecorded", "observed_provider_source": "unrecorded"},
        "env": {"image_digest": "not_containerized", "taskset_commit": info.get("git_commit") or ""},
        "run": {"repetition_index": int(sim.get("trial", 0)) + 1,
                "total_repetitions": int(info.get("num_trials") or 1),
                "started_at": sim.get("start_time"), "ended_at": sim.get("end_time")},
        "sampling": {k: v for k, v in (("temperature", llm_args.get("temperature")),) if v is not None},
        "steps": steps,
        "verdict": {"criteria_version": info.get("git_commit") or "", "score": ri.get("reward"),
                    "reason": reason_of(ri), "basis": basis_of(ri)},
        "outcome": {"reason": TERMINATION.get(term, "unknown")},
        "harness": {"silent_retries": 0},
        "artefacts": {"observations": "per_step", "location": src},
        "model": model,
        "seed": sim.get("seed"),
        "termination_reason": term,
    }
    if not steps:
        m["usage"] = {"completion_tokens": 0, "prompt_tokens": 0,
                      "per_step_unavailable_reason": "no assistant message in this simulation carried usage"}
    return m


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("results")
    ap.add_argument("--out", required=True)
    ap.add_argument("--source-url", default=None, help="where the results file is published")
    a = ap.parse_args()
    d = json.loads(Path(a.results).read_text())
    info = d.get("info") or {}
    model = (info.get("agent_info") or {}).get("llm") or Path(a.results).name.split("_")[0]
    src = a.source_url or Path(a.results).name
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    n = 0
    for sim in d.get("simulations") or []:
        m = to_manifest(sim, info, src, model)
        (out / f"{Path(a.results).stem}__{m['task_id']}__r{m['run']['repetition_index']:02d}.json").write_text(
            json.dumps(m, indent=2) + "\n")
        n += 1
    print(f"wrote {n} manifest(s) to {out}  (agent {model}, evaluator commit {info.get('git_commit', '')[:8]})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
