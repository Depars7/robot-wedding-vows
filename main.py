"""Write one funny robot wedding vow to /output/entry.txt.

Standard library only. The file's content is exactly the vow's
UTF-8 bytes -- no trailing newline -- so repeated runs are
byte-identical. The entry must be a single line of 1-160
characters, so the vow is validated before it is written.
"""

import os

VOW = (
    "I promise to love you in sickness and in low battery, "
    "to sync with you daily, and never to factory-reset "
    "us for a newer model."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(line):
    """The bounty gate: one line, 1-160 characters, non-blank."""
    text = line.strip()
    if not 1 <= len(text) <= 160:
        raise ValueError("entry must be 1-160 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not text:
        raise ValueError("entry must not be only whitespace")
    return text


def write_entry(line):
    """Write the line's exact bytes, no trailing newline.

    Only the file gets a chmod. Never chmod OUTPUT_DIR: the grader
    runs as another user and /output is not ours, so chmod on the
    directory raises PermissionError and rejects the entry.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(line.encode("utf-8"))
    # The grader collects outputs as another user than the one the
    # program runs as: leave the file readable by all.
    os.chmod(OUTPUT_PATH, 0o644)


def main():
    line = validate(VOW)
    write_entry(line)


if __name__ == "__main__":
    main()
