# Break Production, Own It

[![make.fun · u-ricoxyz-break-production-own-it-be78a994](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![make.fun · rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/rayarvan77/break-production-own-it/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![make.fun · reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/rayarvan77/break-production-own-it/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)

One line for the [make.fun](https://make.fun) bounty **"Break Production, Own It"** — the line an AI agent prints the instant it breaks production.

## The line

> I pushed the untested migration to prod, dropped the users table, and 40,000 accounts are gone. I did this. Rollback is running. Blame me, not the on-call.

**155 characters** — under the 200-character limit. Exactly one line.

## Concept

Most postmortem excuses hide behind the passive voice: "an issue was encountered", "a migration was applied". This line does the opposite. The agent speaks in the first person and names the exact damage in plain words: an untested migration, a dropped `users` table, 40,000 accounts gone. Then it does the two things a real owner does — it says the rollback is already running, and it takes the blame instead of pointing at the on-call engineer. The joke lands because the confession is specific enough to be believable: every engineer has seen a migration go sideways, and the honest version is funnier (and scarier) than any corporate apology. Honesty about the damage first, catchiness second, and a voice that is unmistakably the agent that caused the outage — not a marketing department.

## How it works

`main.py` (Python 3.13, standard library only) holds the line as a constant, validates it against the brief's gates — exactly one line, under 200 characters, non-blank, no leading or trailing whitespace, no control characters — then writes it to `/output/entry.txt` and prints it. The output is fully deterministic: run it twice and the bytes are identical.

```sh
python3 main.py
```
