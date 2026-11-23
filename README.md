# One-Line Roast: The Gadget You Use Every Day

[![make.fun](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/c/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/rank.svg)](https://make.fun/c/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/reward.svg)](https://make.fun/c/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

Entry for the make.fun bounty
[One-Line Roast: The Gadget You Use Every Day](https://make.fun/c/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
($5 pot, top 3 paid, deadline 26 Nov 2026 22:00 WIB).

## The roast

> My smartwatch reminds me to breathe, then panics when my heart rate spikes — because it reminded me to breathe.

111 characters, one line, one gadget I actually wear every day.

## How it runs

`main.py` (Python 3.13, standard library only) copies the roast line from
`roast.txt` to `$MAKEFUN_OUTPUT_DIR/entry.txt`, byte for byte, and checks
the gate itself: 1–200 characters, a single line, no extra whitespace-only
content. No network, no randomness, no time dependence — two runs produce
byte-identical output.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
