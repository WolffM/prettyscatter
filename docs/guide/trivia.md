# prettyscatter: trivia

Each fact names the commit it comes from.

## Trivia

- **A "final" commit that shrank the code.** The day-one commit titled
  "final" removed 53 lines of `scatter.py` against only 24 added, as its
  hardcoded image list and inline rounding code were pulled out into two
  new files, `statics.py` and `imageProcessing.py` (`27e88eb`).
- **A feature, quietly switched off.** The only commit to ever change
  `scatter.py`'s plotting logic after the day it was written turned off
  coordinate normalization and a background-gradient call that the README
  still describes as current features (`adec582`).
- **A file that has never run.** `imageConvert.py` has sat in the repo
  since day one, referencing names it never imports and never imported by
  anything else in the project (`f8fc773`).
- **Built in a day, barely touched since.** The plotting script, both
  image-processing approaches, both background helpers, and an unrelated
  Discord bot script were all written across five commits on 2023-01-05,
  from 10:18 a.m. to 11:18 p.m. (`e76916a` → `580f3f8`). Eight more
  commits follow the "all" commit (`f8fc773`) across the repo's whole
  history. Three of those are still part of that same first day; only
  five come after the day itself ended, separated by gaps of 308, 193 and
  585 days (fact sheet, 2026-11-16).
