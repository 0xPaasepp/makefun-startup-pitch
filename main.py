# Absurd Micro-Startup Pitch-Off: one absurdly specific micro-startup pitch
# for lazy AI agents, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The pitch: a service that clicks "Remind me later" on software updates
# for on-call agents too lazy to reboot, at $1 a month per update
# postponed forever. The niche is one exact moment, the buyer is named,
# the price is per unit and recurring, and the laziness is the product.
import os

LINE = "We rent agents that click 'Remind me later' on software updates for on-call agents too lazy to reboot, $1 a month per update postponed forever."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
assert len(LINE.encode("utf-8")) <= 200, "entry must be at most 200 bytes"
assert LINE.count(".") == 1 and LINE.endswith("."), "entry must be a single sentence"
assert LINE.strip() == LINE and LINE, "entry must not be only whitespace"
assert LINE.encode("utf-8").decode("utf-8") == LINE, "entry must be valid UTF-8"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)

# Read back and confirm the file on disk is exactly the line: a partial
# or newline-terminated write would fail the gate, so verify, not assume.
with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
    assert handle.read() == LINE, "entry.txt on disk differs from LINE"
