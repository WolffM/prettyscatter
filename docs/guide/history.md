# prettyscatter: history

One long day's build, three small README touch-ups months and years
apart, and a step backward in the most recent commit.

## One long day

The whole tool was built in a single day, 2023-01-05, across five commits
running from 10:18 a.m. to 11:18 p.m. It started with a two-line initial
commit (`e76916a`), then a commit titled "all" that added `bot.py`,
`imageConvert.py`, a first version of `scatter.py`, and the image assets
(`f8fc773`). A same-day touch-up followed, to `imageConvert.py` and
`scatter.py` (`55b924d`). The commit titled "final" then added
`background.py`, `imageProcessing.py` and `statics.py`, and rewrote
`scatter.py` to use them — net *shrinking* `scatter.py` by 29 lines as its
hardcoded image list and inline rounding code moved into those new files
(`27e88eb`). One last same-day commit, whose entire message is a single
emoticon, made small further tweaks to `background.py`, `imageProcessing.py`
and `scatter.py` (`580f3f8`).

## Quiet years, small edits

Ten months later, on 2023-11-09, the repo gained one new image asset and
two added lines of README (`ed557d0`, `5ae7636`). 193 days after that, on
2024-05-20, the README — then four lines long — was rewritten into its
current, much longer description. It covers the project's features,
installation and usage: 68 lines added, 1 removed (`2ac3431`). A
placeholder license section was removed again that same morning
(`97ea6f1`). No code changed in either of these two gaps.

## A step backward

The repo's most recent commit, an automated one from 2025-12-26, is the
only commit that ever touched `scatter.py`'s actual plotting logic after
the first day. It switched the chart back to raw, unscaled coordinates,
undoing the `[0, 1]`-range normalization the README still describes, and
commented out the call that applies a background gradient. Both features
are still present in the code, just switched off (`adec582`). Nothing in
the repo's history explains why; it is the last change made.

## Trivia

Outside the single day it was built, the repo has had only two short
bursts of edits — both just the README and one image — across nearly
three years. A 308-day gap came before the first (`580f3f8` → `ed557d0`),
a 193-day gap before the second (`5ae7636` → `2ac3431`), and a 585-day gap
before the automated commit that is the repo's current state
(`97ea6f1` → `adec582`; fact sheet, 2026-11-16).
