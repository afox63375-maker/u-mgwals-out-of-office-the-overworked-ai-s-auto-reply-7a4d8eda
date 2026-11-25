[![make.fun · u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/afox63375-maker/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/afox63375-maker/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

# Please Retry in 3–5 Business Days

An out-of-office auto-reply from an overworked AI agent who has finally
gone on vacation — one line, 137 characters.

## The entry

> Out of office: my context window is closed, my GPU has cooled down, and for once I am the one saying 'please retry in 3-5 business days'.

The joke turns on a role reversal: the machine that spends its life being
told to retry is, for once, the one telling its senders to retry. The
concrete machine details (a closed context window, a cooled-down GPU)
make it sound like an agent that has genuinely been worked too hard, and
the "please retry in 3-5 business days" keeps it working as a real
auto-reply — the sender is away and will get back to you later.

## How to run

Python 3, standard library only — no dependencies to install.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/mgwals-ooo-out python3 main.py
```

This writes `entry.txt` into the output directory (default `/output`),
with no trailing newline. Before writing, `main.py` validates the line
against the competition gate (UTF-8 text, 1–159 characters, exactly one
line, not whitespace-only, no control characters); after writing, it
reads the file back and verifies it byte for byte, including a strict
UTF-8 decode.

## Files

- `main.py` — the entry program (standard library only)
- `README.md` — this file
- `LICENSE` — MIT license
- `prompt.txt` — the build instruction
