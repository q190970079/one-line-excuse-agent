#!/usr/bin/env python3
"""Write one one-line deadline excuse to /output/entry.txt."""

import os

TEXT = "Sorry I missed the deadline — I hit a rate limit on competence, retried myself 400 times, and every retry sincerely believed it was the first attempt."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
