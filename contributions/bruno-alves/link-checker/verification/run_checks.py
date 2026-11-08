#!/usr/bin/env python3
"""Self-check helper for the link-checker package."""

from pathlib import Path
import json


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    metadata = json.loads((root / "metadata.json").read_text(encoding="utf-8"))
    assert metadata["package"] == "link-checker", "unexpected package name"
    print("checks passed for link-checker")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
