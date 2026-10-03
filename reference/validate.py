#!/usr/bin/env python3
"""Validate manifest files against schema/manifest.schema.json.

    python3 reference/validate.py examples/*.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

try:
    import jsonschema
except ModuleNotFoundError:
    sys.exit("needs jsonschema:  pip install jsonschema")


def main(paths: list[str]) -> int:
    schema = json.loads((ROOT / "schema" / "manifest.schema.json").read_text())
    v = jsonschema.Draft202012Validator(schema)
    bad = 0
    for p in paths:
        errs = sorted(v.iter_errors(json.loads(Path(p).read_text())), key=lambda e: list(e.path))
        if errs:
            bad += 1
            print(f"FAIL {p}")
            for e in errs[:8]:
                print(f"   {'/'.join(str(x) for x in e.path) or '<root>'}: {e.message}")
        else:
            print(f"ok   {p}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or ["examples/"]))
