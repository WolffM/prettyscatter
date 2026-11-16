# prettyscatter: history

One long day's build, three small README touch-ups months and years
apart, and a step backward in the most recent commit.

## One long day

The whole tool was built in a single day, 2023-01-05, across five commits
running from 10:18 a.m. to 11:18 p.m.: a two-line initial commit
(`fecde1d`), then a commit titled "all" that added `bot.py`,
`imageConvert.py`, a first version of `scatter.py`, and the image assets
(`82aa381`), followed by a same-day touch-up to `imageConvert.py` and
`scatter.py` (`c44697b`). The commit titled "final" then added
`background.py`, `imageProcessing.py` and `statics.py`, and rewrote
`scatter.py` to use them — net *shrinking* `scatter.py` by 29 lines as its
hardcoded image list and inline rounding code moved into those new files
(`d0ae263`). One last same-day commit, whose entire message is a single
emoticon, made small further tweaks to `background.py`, `imageProcessing.py`
and `scatter.py` (`eb5656c`).

## Quiet years, small edits

Ten months later, the repo gained one new image asset and two added lines
of README (`fe19cdd`, `90a25ed`), on 2023-11-09. 193 days after that, on
2024-05-20, the README — then four lines long — was rewritten (68 lines
added, 1 removed) into its current, much longer description of the
project's features, installation and usage (`d219e35`), with a placeholder
license section removed again the same morning (`06a2b6a`). No code
changed in either of these two gaps.

## A step backward

The repo's most recent commit, an automated one from 2025-12-26, is the
only commit that ever touched `scatter.py`'s actual plotting logic after
the first day: it switched the chart back to raw, unscaled coordinates
(undoing the `[0, 1]`-range normalization the README still describes) and
commented out the call that applies a background gradient, leaving both
features present in the code but switched off (`905ddbb`). Nothing in the
repo's history explains why; it is the last change made.

## Trivia

Outside the single day it was built, the repo has had only two short
bursts of edits — both just the README and one image — across nearly
three years: a 308-day gap before the first (`eb5656c` → `fe19cdd`), a
193-day gap before the second (`90a25ed` → `d219e35`), and a 585-day gap
before the automated commit that is the repo's current state
(`06a2b6a` → `905ddbb`; fact sheet, 2026-11-16).
