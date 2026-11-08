#!/usr/bin/env python3
"""Example self-check helper for a work package.

Every package must ship a script at verification/run_checks.py. Only the
existence of this file is checked by the delivery gate, but the template
provides a small working example.
"""

from pathlib import Path
import json


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    metadata = json.loads((root / "metadata.json").read_text(encoding="utf-8"))
    assert metadata.get("package"), "metadata.json must declare a package name"
    print("template package is structurally valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
