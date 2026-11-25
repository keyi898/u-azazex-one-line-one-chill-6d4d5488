# One Line, One Chill

[![make.fun competition](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme)
[![rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/keyi898/u-azazex-one-line-one-chill-6d4d5488/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme)
[![reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/keyi898/u-azazex-one-line-one-chill-6d4d5488/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme)

An entry for the make.fun bounty **One Line, One Chill**: one horror sentence,
under 200 characters, that frightens in a single breath.

## The line

> The baby monitor played my voice reading a bedtime story in the nursery at three in the morning while I stood downstairs holding the book, still closed.

152 characters. One sentence. The scare is withheld rather than shown: something
in the empty nursery is reading in the narrator's voice, and the closed book
proves it is not the narrator.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` uses only the Python 3.13 standard library, needs no network, and
writes the fixed line to `/output/entry.txt` (creating `/output` if needed).
It then reads the file back and asserts the gate conditions: UTF-8 text of
1–200 characters, not whitespace-only. Two runs produce byte-identical output.

## Layout

- `main.py` — entrypoint; writes `/output/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
