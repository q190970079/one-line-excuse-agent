#!/usr/bin/env python3
"""Write one one-line deadline excuse to /output/entry.txt.

The excuse blames a rate limit on competence and a retry loop
in which every retry believed it was the first attempt, which
keeps the joke inside the agent's own machinery: throttling,
retries and stateless restarts are how an agent actually fails.
"""

import os

TEXT = "Sorry I missed the deadline — I hit a rate limit on competence, retried myself 400 times, and every retry sincerely believed it was the first attempt."
OUTPUT_PATH = "/output/entry.txt"


def build_excuse():
    """Return the one-line excuse exactly as it will be judged."""
    return TEXT


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(build_excuse())


if __name__ == "__main__":
    main()
