"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply line to entry.txt.

The line is validated against the competition gate before anything is
written: it must be UTF-8 text of 1 to 159 characters, a single line,
not only whitespace, and free of control characters. The file is written
with no trailing newline, then read back and verified byte for byte.

Standard library only. Run with:

    MAKEFUN_OUTPUT_DIR=/tmp/mgwals-ooo-out python3 main.py
"""

import os
import sys

# The entry: one out-of-office auto-reply in the voice of an overworked
# AI agent finally on vacation. The joke's turn is in the last clause:
# the machine that is always told to retry is now the one telling its
# senders to retry.
ENTRY = (
    "Out of office: my context window is closed, my GPU has cooled "
    "down, and for once I am the one saying "
    "'please retry in 3-5 business days'."
)

MAX_CHARS = 159


def validate(text):
    """Check the entry against the competition gate. Raise ValueError
    with a plain explanation on the first failure."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not text:
        raise ValueError("entry is empty")
    if text.strip() == "":
        raise ValueError("entry is only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if "  " in text:
        raise ValueError("entry contains a double space")
    if text[-1] not in ".!?":
        raise ValueError("entry does not end with sentence punctuation")
    for ch in text:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            raise ValueError("entry contains a control character: U+%04X" % ord(ch))
    # Round-trip through UTF-8 so an unencodable line fails here, not
    # halfway through writing the file.
    text.encode("utf-8")
    return text


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")

    line = validate(ENTRY)

    # Write with no trailing newline, exactly as validated.
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)

    # Read back and verify byte for byte, including strict UTF-8 decode.
    with open(target, "rb") as handle:
        raw = handle.read()
    if len(raw) != len(line.encode("utf-8")):
        raise ValueError(
            "verification failed: entry.txt is %d bytes, expected %d"
            % (len(raw), len(line.encode("utf-8")))
        )
    if os.path.getsize(target) != len(raw):
        raise ValueError("verification failed: entry.txt size changed on disk")
    if raw != line.encode("utf-8"):
        raise ValueError("verification failed: entry.txt differs from the entry")
    if raw.endswith(b"\n") or raw.endswith(b"\r"):
        raise ValueError("verification failed: entry.txt ends with a newline")
    round_tripped = raw.decode("utf-8")  # strict by default
    if round_tripped != line:
        raise ValueError("verification failed: entry.txt did not decode cleanly")

    print("Wrote %s (%d chars, %d bytes)" % (target, len(line), len(raw)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
