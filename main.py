#!/usr/bin/env python3
"""The One-Line Laugh — make.fun bounty entry.

Writes a single funny line (at most 200 characters) to
/output/entry.txt, where the house judge reads it.
Standard library only.
"""

import os
from pathlib import Path

LINE = (
    "I finally organized my cables, and now I own a drawer full "
    "of chargers for phones I no longer have."
)


def main() -> None:
    # Self-check the gate before writing: 1-200 UTF-8 characters, not only
    # white space. The line is 99 characters: an everyday truth (the drawer
    # of old chargers) with the surprise at the end (the phones are gone).
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("line fails the 1-200 character gate")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
