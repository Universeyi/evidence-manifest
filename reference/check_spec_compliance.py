#!/usr/bin/env python3
"""Semantic checks a schema cannot express.

validate.py answers "are the fields there, with the right types". That is
necessary and it is not enough: the first adapter written for this spec
produced schema-valid manifests whose observed_provider had been copied from
the declared provider -- a claim dressed as an observation. The schema passed
it. This file exists because of that.

Each rule below names the failure it was written against. A rule that cannot
name one does not belong here.

    python3 reference/check_spec_compliance.py examples/*.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path


def rules(m: dict) -> list[tuple[str, str]]:
    """Return (severity, message) findings for one manifest."""
    out = []
    sv, run, vd, oc = m["serving"], m["run"], m["verdict"], m["outcome"]
    af = m.get("artefacts") or {}

    # R1 -- observed vs declared provider.
    # Failure this catches: the adapter that filled observed_provider from the
    # declared value. A correct pin ALSO makes them equal (the normal case), so
    # equality alone proves nothing; the source field is what decides.
    src = sv.get("observed_provider_source")
    obs, dec = sv.get("observed_provider"), sv.get("provider")
    if src == "unrecorded" and obs != "unrecorded":
        out.append(("error", f"observed_provider={obs!r} but source is 'unrecorded': "
                             "a value with no read-back provenance is a claim, not an observation"))
    if src in ("response", "log") and obs == "unrecorded":
        out.append(("error", "source says the provider was read back, but observed_provider is 'unrecorded'"))
    if obs not in (None, "unrecorded") and obs != dec and src in ("response", "log"):
        out.append(("warning", f"served by {obs!r} while pinned to {dec!r}: routing did not honour the pin "
                               "(this is a real finding about the endpoint, not a manifest defect)"))

    # R2 -- outcome and verdict must not contradict each other.
    # Failure this catches: one in five published runs ended at a round cap and
    # was recorded indistinguishably from a wrong answer. The manifest makes
    # the distinction; the checker makes sure it is not then contradicted.
    score = vd.get("score")
    reason = oc.get("reason")
    if reason == "budget_exhausted" and score is not None and score > 0.99:
        out.append(("error", "outcome is budget_exhausted but the verdict is a pass"))
    if reason == "completed" and score is None:
        out.append(("error", "outcome is completed but no score was recorded"))
    if reason == "unknown" and score is not None:
        out.append(("warning", f"outcome is unknown but a score ({score}) is present; "
                               "consumers must not count this run in any denominator"))

    # R3 -- repetition bookkeeping.
    # Failure this catches: 37 of 40 entries were single runs with no interval;
    # a repetition index outside its declared total makes an interval impossible.
    if run["repetition_index"] > run["total_repetitions"]:
        out.append(("error", f"repetition_index {run['repetition_index']} exceeds total_repetitions {run['total_repetitions']}"))

    # R4 -- time runs forward.
    # Failure this catches: a verdict that predates its run, which is what a
    # retroactively-filled record looks like. Only checkable where both stamps exist.
    s, e = run.get("started_at"), run.get("ended_at")
    if s and e:
        try:
            if datetime.fromisoformat(e.replace("Z", "+00:00")) < datetime.fromisoformat(s.replace("Z", "+00:00")):
                out.append(("error", "ended_at precedes started_at"))
        except ValueError:
            out.append(("warning", "timestamps are not parseable ISO 8601"))

    # R5 -- usage is recorded once.
    # Failure this catches: double counting when a harness records per-step
    # tokens AND a run total. The fallback exists for harnesses that cannot
    # record per step; it is not a second copy.
    if m.get("steps") and m.get("usage"):
        out.append(("error", "both per-step completion_tokens and a run-level usage total are present; record one"))
    if not m.get("steps") and not m.get("usage"):
        out.append(("error", "no token usage at all: neither steps[] nor usage"))
    if m.get("usage") and not m["usage"].get("per_step_unavailable_reason"):
        out.append(("error", "run-level usage without per_step_unavailable_reason: say why per-step is missing"))
    if m.get("usage") and m["usage"].get("completion_tokens") is None:
        out.append(("warning", "no token usage recorded for this run: it cannot enter the drift screen"))

    # R6 -- a verdict must be adjudicable by someone.
    # Failure this catches: 384 of 1,144 published passes carry no verifier
    # reason, and the screenshots behind most of the audit's own runs were
    # discarded after submission. A run with no retained observation and no
    # reason cannot be opened by a person: nothing to look at, nothing
    # explained. It is not wrong. It is unexaminable, and a checker analysis
    # must leave it out of its denominator.
    if af.get("observations") == "none" and not (vd.get("reason") or "").strip():
        out.append(("warning", "verdict is unadjudicable: observations=none and no verifier reason; "
                               "exclude from any checker (false-positive/negative) denominator"))
    if af.get("observations") in ("per_step", "final_only") and not af.get("location"):
        out.append(("warning", f"artefacts.observations={af['observations']!r} but no location: "
                               "a claim that observations exist, with nowhere to look"))

    return out


def main(paths: list[str]) -> int:
    worst = 0
    for p in paths:
        m = json.loads(Path(p).read_text())
        findings = rules(m)
        if not findings:
            print(f"ok       {p}")
            continue
        for sev, msg in findings:
            print(f"{sev.upper():8s} {p}: {msg}")
            worst = max(worst, 2 if sev == "error" else 1)
    return 1 if worst == 2 else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
