#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes the single roast line stored in roast.txt to
$MAKEFUN_OUTPUT_DIR/entry.txt, byte for byte.

Standard library only. No network, no randomness, no time dependence:
two runs produce byte-identical output.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "roast.txt")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    shutil.copyfile(src, dst)
    with open(dst, "r", encoding="utf-8") as f:
        text = f.read()
    stripped = text.strip()
    if not (1 <= len(stripped) <= 200):
        print(f"entry must be 1-200 characters, got {len(stripped)}",
              file=sys.stderr)
        return 1
    if stripped.count("\n") != 0:
        print("entry must be a single line", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
