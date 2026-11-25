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
    "The milk expired Tuesday. You hid it behind the yogurt and hoped "
    "I wouldn't notice. I notice everything. I am cold, not stupid."
)


def main() -> None:
    if not NOTE.strip():
        raise SystemExit("entry must not be empty or whitespace only")
    if "\n" in NOTE or "\r" in NOTE:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(NOTE) <= 200:
        raise SystemExit("entry must be between 1 and 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(NOTE + "\n")
    print(NOTE)


if __name__ == "__main__":
    main()
