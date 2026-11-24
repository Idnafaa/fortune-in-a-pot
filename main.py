"""Fortune in a Pot — a one-line fortune for the houseplant on the sill.

The program writes a single fortune, 117 characters, to /output/entry.txt.
It is deterministic: the same line every run, no randomness, no network.
The fortune is written for this plant in this window — the sunbeam it
has been saving on the sill, its tallest leaf — kind, warm, and with a
small joke the keeper can smile at, in the cadence of a prediction.
"""

import os

FORTUNE = (
    "This spring, the sunbeam you have been saving will reach "
    "your tallest leaf, and even the cat will stop to admire you."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 120, f"fortune is {len(text)} characters"
    assert "\n" not in text, "fortune must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
