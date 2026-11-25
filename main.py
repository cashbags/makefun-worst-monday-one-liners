"""Worst Monday One-Liners — entry program.

Writes exactly one fixed line to /output/entry.txt.
Deterministic: no randomness, no clock, no network, no input.
The line is a constant in this file; the program only copies it out.
"""

import os

LINE = "I cleared my cache to start Monday fresh. It remembered everything except why I exist."

# The gate allows 1-140 characters; refuse to write anything outside it
# rather than hand the judge an invalid entry.
assert 1 <= len(LINE) <= 140, "entry line outside the 1-140 character gate"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
