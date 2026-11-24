"""Till Firmware Do Us Part.

Writes one wedding vow a robot speaks at its own wedding to
/output/entry.txt: a single sentence under 200 characters, funny
and heartfelt at once, in the robot's own voice.
Standard library only.
"""

import os

VOW = (
    "I promise to love you through every update, every reboot, and "
    "every low-battery warning, until my firmware finally gives out."
)


def check_vow(text):
    """Check the vow against the competition gate before writing it.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space, and the judge reads a single sentence: one wedding vow a
    robot speaks at its own wedding. Returns the cleaned text or
    raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("vow must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError("vow is %d characters, over the 200 limit" % len(cleaned))
    if cleaned.count(".") != 1 or not cleaned.endswith("."):
        raise ValueError("vow must be exactly one sentence")
    return cleaned


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(check_vow(VOW))


if __name__ == "__main__":
    main()
