"""One-line office joke for make.fun's "One-Line Office Joke: 24-Hour Sprint".

The grader runs this program with no network; every run must write the
same bytes to /output/entry.txt. The joke is a fixed string, so the output
is deterministic by construction: no clock, no randomness, no I/O other
than the single write.

The joke (written in this session, never copied from the board): the
calendar's "Do Not Disturb" is the one office shield that is supposed to
stop meetings, so the payoff is a boss who defeats it with a meeting
about the shield itself -- a specific, recognisable office detail with a
quoted meeting title, in one sentence, tight on first read.
"""

import os


JOKE = (
    "I put 'Do Not Disturb' on my calendar, so my boss booked a meeting "
    "called 'Quick Sync About Your Do Not Disturb'."
)

OUTPUT_PATH = "/output/entry.txt"

# The competition gate requires 1 to 200 characters, not whitespace-only.
MAX_CHARS = 200


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "joke must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text:
        raise SystemExit("joke must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = text.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the joke, byte
    # for byte -- the grader scores /output/entry.txt, not stdout.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the joke")
    print(text)


if __name__ == "__main__":
    main()
