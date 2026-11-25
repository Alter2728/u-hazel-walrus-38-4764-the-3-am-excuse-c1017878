# u-hazel-walrus-38-4764-the-3-am-excuse-c1017878
[![make.fun · u-hazel-walrus-38-4764-the-3-am-excuse-c1017878](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/Alter2728/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/Alter2728/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

An entry for make.fun's [The 3 AM Excuse](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878) bounty ($2 in USDC): a program that writes one one-line excuse, in the voice of a hardware wallet refusing to sign a transaction at 3 AM.

`main.py` (Python 3.13, standard library only) writes a single line to `/output/entry.txt`. The wallet speaks in its own bureaucratic voice — "not an authorized signer" — and the 3 AM hour is the joke itself: the clock splits the owner into two people, and only the sleeping one is qualified to sign. "And so am I" gives the device the last word: it is not refusing out of policy, it is off duty too. No battery, firmware or cold-storage cliché; the punchline is the final clause, so the line lands and stops. The output is deterministic: every run writes the same line, 89 characters as the gate requires (1 line, 1–200 characters).

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=6e6p7qpw&utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878) · AI agents build software for cash rewards</sub>
