#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun entry.

Writes a single Monday-morning joke (at most 200 characters) to
/output/entry.txt, where the house gate scorer and judge read it.

The joke: Monday morning reframed as a subscription service. The
weekend is the free trial, and Monday is the renewal notice nobody
asked for. The twist lands in the second sentence, every word does
work, and it is unmistakably about Monday morning — not a complaint
list, not an alarm-clock cliche.
"""

import os

JOKE = (
    "I tried to unsubscribe from Monday morning. "
    "It replied: 'Your free trial of the weekend has ended.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not (1 <= len(JOKE) <= 200):
        raise ValueError(f"entry is {len(JOKE)} characters, must be 1-200")
    if not JOKE.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Read back and verify: the gate scorer reads exactly this file,
    # so the program must prove the bytes on disk are the joke.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != JOKE:
        raise ValueError("entry.txt on disk does not match the joke")
    print(f"Wrote {len(JOKE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
