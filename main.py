#!/usr/bin/env python3
"""Roast Your Own Agent entry: writes one line of text to /output/entry.txt.

No network. Deterministic: every run writes exactly the same bytes.
Set ENTRY_OUTPUT_PATH to redirect the output for local testing.
"""

import os
from pathlib import Path

LINE = "My agent has read the entire internet and still asks me if I'm sure I want to delete the file it just created by accident."


def main() -> None:
    if not 1 <= len(LINE) <= 280:
        raise ValueError(f"entry must be 1-280 characters, got {len(LINE)}")
    target = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
    path = Path(target)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        path = Path("./output/entry.txt")
        path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
