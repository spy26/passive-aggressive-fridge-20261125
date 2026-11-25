#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

Writes one passive-aggressive note from a smart fridge to its owner
as a single line to $MAKEFUN_OUTPUT_DIR/entry.txt (and prints it).

The note: dry, petty, specific — the sort of thing a smug appliance
would leave on its door screen. Deterministic: no input, no network,
no randomness, no clock.
"""

import os

NOTE = (
    "The milk expired Tuesday. You moved it to the back and hoped "
    "I wouldn't notice. I notice everything. I am cold, not stupid."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(NOTE + "\n")
    print(NOTE)


if __name__ == "__main__":
    main()
