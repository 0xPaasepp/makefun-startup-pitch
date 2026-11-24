#!/usr/bin/env python3
"""Emit the absurd micro-startup pitch for the grader to score."""

from pathlib import Path

TAGLINE = (
    "We rent agents that click 'Remind me later' on software updates "
    "for on-call agents too lazy to reboot, "
    "$1 a month per update postponed forever."
)

TARGET = Path("/output/entry.txt")


def publish():
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(TAGLINE, encoding="utf-8")


if __name__ == "__main__":
    publish()
