#!/usr/bin/env python3
"""The Vacuum's Alibi: one line, at most 200 characters.

The program writes a single deadpan excuse from a robot vacuum for
missing a spot to $MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic: no
randomness, no clock, no network, no input files.
"""

import os
import sys

ENTRY = (
    "I did not miss that spot. My lidar classified it as a protected "
    "historical crumb, and disturbing it would void my warranty and "
    "possibly anger the crumb."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
