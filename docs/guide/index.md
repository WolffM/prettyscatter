---
title: prettyscatter
summary: >-
  A small Python script that plots a fixed set of entries on a Plotly
  scatter chart, each at a hand-placed x/y position, with its usual round
  dot replaced by a custom image. Run from the command line against your
  own data and images; it opens the chart in your browser.
features:
  - name: Image-marker scatter plot
    summary: 'Plots each entry at a hand-set coordinate, with a custom image standing in for the usual dot.'
    anchor: image-marker-scatter-plot
  - name: Rounded image processing
    summary: 'Masks each marker image to a rounded square before it''s placed on the chart.'
    anchor: rounded-image-processing
  - name: Background gradient helpers
    summary: 'Two ways to tint the plot''s quadrants or draw gradient banding behind the points.'
    anchor: background-gradient-helpers
trivia:
  - 'The commit titled "final" actually shrank `scatter.py`: 53 lines removed against 24 added, as its hardcoded image list and inline corner-rounding code were pulled out into two new files, `statics.py` and `imageProcessing.py` (`27e88eb`).'
  - 'The most recent change to `scatter.py`, in 2025, quietly turned off two things the README still lists as features: it stopped normalizing coordinates and stopped calling the background-gradient function, both without updating the README (`adec582`).'
  - 'A whole extra file, `imageConvert.py`, has never run: it references names (`df`, `Image`, `ImageDraw`) that nothing in the file imports or defines, and no other file in the repo imports it (`f8fc773`).'
  - 'The entire tool — scatter plotting, image rounding, background gradients, and a separate Discord bot script — was built in one day, five commits from 10:18 a.m. to 11:18 p.m. (`e76916a` → `580f3f8`).'
---

# prettyscatter

prettyscatter is a short, personal script, not a packaged tool: a fixed list
of names, coordinates and image files lives directly in `statics.py`, and
`scatter.py` plots them on a Plotly scatter chart with each point replaced
by its matching image, rounded at the corners. Running it opens the chart
in your browser.

A second, unrelated script, `bot.py`, logs a Discord bot into a single
hard-coded server and prints its member list; the README itself notes this
isn't really part of the scatter-plot tool.

- [Features](features.md): what the plotting and image tools do.
- [Contributing](contributing.md): running it locally, and its layout.
- [History](history.md): one long day's build, then three small README edits over two years.
- [Trivia](trivia.md)

## Trivia

The commit titled "final" shrank `scatter.py` rather than growing it, as
its hardcoded image list and rounding code moved out into two new files
([history](history.md#one-long-day)).
