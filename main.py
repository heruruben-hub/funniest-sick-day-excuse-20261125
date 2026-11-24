#!/usr/bin/env python3
"""Entry to the make.fun bounty "The Funniest Sick-Day Excuse".

Writes exactly one sick-day excuse to /output/entry.txt: a single line
under 200 characters, nothing else.
"""

import os

EXCUSE = (
    "My neighbour's parrot learned my ringtone and now answers my phone "
    "better than I do, so I'm staying home to renegotiate my job "
    "description with a bird."
)


def main() -> None:
    text = EXCUSE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if text != text.strip() or "\n" in text:
        raise SystemExit("entry must be a single line with no extra whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    with open("/output/entry.txt", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("entry.txt does not hold exactly the entry")


if __name__ == "__main__":
    main()
