# Contributing

How to run the script locally and where things live. What it does for a
user is in [features.md](features.md).

## Run it locally

```sh
pip install plotly pandas Pillow
```

(there is no `requirements.txt`; this is the README's own install line).
Add your own images to `assets/` and list them, with coordinates, in
`statics.py` — see [features.md](features.md#image-marker-scatter-plot) —
then:

```sh
python scatter.py
```

`bot.py` is a separate, unrelated script (the README says as much) that
logs a Discord bot into one hard-coded server and prints its member list
on startup; it needs its own `.env` with `DISCORD_TOKEN` set, and performs
no further action.

## Architecture

| Path                 | What it is                                                                |
| -------------------- | -------------------------------------------------------------------------- |
| `scatter.py`         | the main script: loads `statics.py`'s entries, builds the Plotly chart   |
| `statics.py`         | the fixed list of entries plotted — a name, a coordinate, an image file   |
| `imageProcessing.py` | `getRoundedImage`, used by `scatter.py` to round each marker image's corners |
| `background.py`      | two unused-by-default background-gradient helpers (see [features.md](features.md#background-gradient-helpers)) |
| `imageConvert.py`    | dead code: an alternate rounding approach that nothing imports and that references undefined names |
| `bot.py`             | an unrelated Discord bot script; see above                                |
| `assets/`            | the marker images `statics.py` points at, plus one example output image  |

`__pycache__/` (compiled `.pyc` bytecode) is committed to the repo rather
than ignored; there is no `.gitignore` at all.

## Tests and gates

There are no tests, no linter configuration, and no CI workflow.

## How it deploys

It doesn't: this is a script you run on your own machine to produce a
chart in your browser, not a deployed service.

## Trivia

The repo has no `.gitignore`, which is how its compiled `__pycache__`
bytecode ended up committed alongside the source (`f8fc773`).
