# prettyscatter

prettyscatter is a short, personal script, not a packaged tool: a fixed list
of names, coordinates and image files lives directly in `statics.py`, and
`scatter.py` plots them on a Plotly scatter chart with each point replaced
by its matching image, rounded at the corners. Running it opens the chart
in your browser.

```sh
python scatter.py
```

That reads the entries in `statics.py`, builds the chart, and calls
`fig.show()`: a 1200×1200 Plotly figure opens in your default browser,
each point's usual dot replaced by that entry's rounded image, with no
axis lines or labels.

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
