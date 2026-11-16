# prettyscatter: features

What the plotting and image tools do. How the repo is laid out is in
[contributing.md](contributing.md).

## Image-marker scatter plot

**What it does.** `scatter.py` reads a fixed list of entries from
`statics.py` — each one a name, an x/y coordinate, and a matching image
file in `assets/` — and builds a Plotly scatter chart where every point's
usual marker dot is replaced by that entry's image instead. The chart
opens at a fixed 1200×1200 size with no axis lines, grid or tick labels, so
only the images and their layout are visible.

**How to use it.** Add your own image files to `assets/` and list them,
with coordinates, in `statics.py`, then run `python scatter.py`; it opens
the finished chart in your default browser.

**What it does not do.** The README still describes "Data Normalization"
— scaling coordinates into `[0, 1]` before plotting — as a current
feature, but the code that did that (and the matching axis-range fix) is
commented out as of the repo's latest commit; the chart now plots each
entry's raw coordinates unscaled (`905ddbb`; see
[history](history.md#a-step-backward)).

## Rounded image processing

**What it does.** `imageProcessing.py`'s `getRoundedImage` takes a source
image and gives its four corners a circular mask, so a rectangular PNG
reads as a rounded square once placed on the chart.

**How to use it.** Called automatically by `scatter.py` for every entry;
there is no separate command.

**What it does not do.** The corner radius (40 pixels) is a constant in
the function, not a parameter `scatter.py` passes through — changing it
means editing `imageProcessing.py` directly. A sibling file,
`imageConvert.py`, attempts a different, mask-based rounding approach but
is never imported or called from anywhere in the repo, and references
names it never imports (`Image`, `ImageDraw`, `df`) — it cannot run as it
stands.

## Background gradient helpers

**What it does.** `background.py` defines two alternative ways to tint the
chart behind the points: `addBackgroundGradient` paints the plot's four
quadrant-like rectangles in flat, semi-transparent colors, while
`addBackgroundGradient2` draws many thin, increasingly transparent lines
along each edge to fake a soft gradient band, with a solid line marking
where each band starts.

**How to use it.** Neither is called by `scatter.py` as of the latest
commit; using one means uncommenting the matching call
(`fig = addBackgroundGradient2(fig)` or the equivalent) in `scatter.py`
yourself.

**What it does not do.** The two functions produce visually different
effects (flat quadrant tints versus edge gradients) and are not designed
to be combined; the file has no way to pick a gradient style from the
command line.

## Trivia

The call that applied a background gradient and the coordinate-
normalization step were both commented out in the same commit, the
repo's most recent, without a matching README update
(`905ddbb`).
