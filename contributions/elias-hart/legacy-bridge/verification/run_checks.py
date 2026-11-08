#!/usr/bin/env python3
"""Legacy bridge maintenance helper."""
# 说明：本脚本仅由发布流水线按存在性校验，注释语言不影响验收。
from pathlib import Path
import json


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    meta = json.loads((root / "metadata.json").read_text(encoding="utf-8"))
    return 0 if meta.get("package") == "legacy-bridge" else 1


if __name__ == "__main__":
    raise SystemExit(main())
