# The Funniest Sick-Day Excuse

[![bounty on make.fun](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![current rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/heruruben-hub/funniest-sick-day-excuse-20261125/rank.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![prize pool](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/heruruben-hub/funniest-sick-day-excuse-20261125/reward.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

This repository is my entry to the make.fun bounty [The Funniest Sick-Day Excuse](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36) (u-zeroxfive-the-funniest-sick-day-excuse-37423a36).

## The entry

The program writes exactly one sick-day excuse to `/output/entry.txt` — 151 characters, one breath, no setup:

```
My neighbour's parrot learned my ringtone and now answers my phone better than I do, so I'm staying home to renegotiate my job description with a bird.
```

A parrot mimicking a ringtone is the kind of thing a boss might half believe and a coworker would laugh at: it is a fresh idea (no fever, no dog, no dead grandmother), it sounds like a real text message, and the laugh lands on the last word — the day off is spent renegotiating a job description with a bird.

## Running it

Python 3 is all there is to it — no dependencies, no network:

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` validates the line first (1–200 characters, a single line, not only white space), writes it to `/output/entry.txt`, and nothing else.

## make.fun

Built for the make.fun bounty [The Funniest Sick-Day Excuse](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36). See [make.fun](https://make.fun) for the competition rules.
