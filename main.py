"""Fortune in a Pot — a one-line fortune for the houseplant on the sill.

The program writes a single fortune, 117 characters, to /output/entry.txt.
It is deterministic: the same line every run, no randomness, no network.
"""

import os

FORTUNE = (
    "This spring, the sunbeam you have been saving will reach "
    "your tallest leaf, and even the cat will stop to admire you."
)


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 120, f"fortune is {len(text)} characters"
    assert "\n" not in text, "fortune must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
