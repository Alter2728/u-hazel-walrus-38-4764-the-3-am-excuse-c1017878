#!/usr/bin/env python3
"""The 3 AM Excuse — writes one one-line excuse from a hardware wallet
to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version):
#   "3 AM you is not an authorized signer — the version of you that
#    reads whitepapers is asleep, and so am I."
# Why it was revised: "the version of you that reads whitepapers" is
# seven words doing the work of one hyphenated adjective. Compressing
# it to "the whitepaper-reading you" keeps the same joke — the wallet
# only trusts the sensible, daylight version of its owner — but lands
# the turn four words sooner, which matters in a one-breath line.
#
# REVISION (final): the wallet speaks in its own bureaucratic voice
# ("not an authorized signer"), and the 3 AM hour is the joke itself:
# the owner is split into two people by the clock, and only the
# sleeping one is qualified to sign. "And so am I" gives the device
# the last word — it is not refusing out of policy, it is off duty
# too. No battery, firmware or cold-storage cliché; the punchline is
# the final clause, so the line lands and stops.
# ---------------------------------------------------------------------------
ENTRY = (
    "3 AM you is not an authorized signer — the whitepaper-reading "
    "you is asleep, and so am I."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 200 characters, a single line, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert len(written.encode("utf-8")) == len(entry_bytes), (
        "written bytes must match the entry exactly"
    )
    assert 1 <= len(written) <= 200 and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()
