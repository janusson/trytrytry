# trytrytry

A tiny Python roguelike prototype built over a weekend sprint, following the
excellent **Roguelike Tutorial (tcod, 2019)**.

> Tutorial reference: https://rogueliketutorials.com/tutorials/tcod/2019/part-1/

---

## Why this exists

I wanted to develop a quick example of the roguelike loop (map gen -> input ->
field of view > combat > inventory) without ceremony. This repo is intentionally
minimal but structured so you can extend it.

---

## Quick Start

### Prereqs
- Python 3.10 to 3.12 recommended
- macOS, Linux, or Windows
- A virtual environment (`python -m venv .venv`)

### Setup

```bash
git clone https://github.com/<your-username>/trytrytry.git
cd trytrytry
python -m venv .venv && source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -U pip
pip install -r requirements.txt
````

### Run

```bash
python -m trytrytry
# or, if you have a top-level script:
python main.py
```

A window appears with a player `@` on a dungeon map. Have fun and try, try, try.

---

## Controls (default)

* **Arrows / HJKL / Numpad**: Move
* **.\` (period)**: Wait a turn
* **ESC / q**: Quit

> If you followed the tutorial verbatim, movement keys may live in `input_handlers.py`. Adjust here if you remap.

---

## Project Layout

```
trytrytry/
├─ trytrytry/                 # game package (importable; run via `-m trytrytry`)
│  ├─ __init__.py
│  ├─ main.py                 # entry point (sets up context & game loop)
│  ├─ engine.py               # turn loop, rendering hooks
│  ├─ input_handlers.py       # keyboard handling
│  ├─ entity.py               # Actor/Item base classes
│  ├─ components/             # (optional) Fighter, Inventory, AI, etc.
│  ├─ game_map.py             # map + FOV
│  ├─ procgen.py              # dungeon generation
│  ├─ render_functions.py     # draw tiles/entities/UI
│  └─ data/                   # tilesets, fonts, config
├─ tests/                     # basic smoke tests
├─ LICENSE
├─ README.md
├─ requirements.txt
├─ pyproject.toml             # (optional) packaging & tooling config
└─ .gitignore
```

> Your current `trytrytry/source` can become the package root (`trytrytry/`); move files into it and add `__init__.py` so `python -m trytrytry` works cleanly.

---

## Tech

* \[tcod / libtcod] for console rendering & input
* Python standard library (dataclasses / typing)
* (Optional) `numpy` for FOV & map math

---

## Roadmap (weekend -> "v1")

* [ ] Basic combat log and HP bars
* [ ] Simple item system (healing potion)
* [ ] Save/Load (pickle or JSON for game state)
* [ ] Minimal UI polish (help screen; keybinding overlay)
* [ ] One smoke test (map gen + walkable tile assertion)
* [ ] GitHub Actions: run tests on PRs

Stretch:

* [ ] Field-of-view shadows; exploration memory ("fog of war")
* [ ] Simple AI (chase/attack)
* [ ] Inventory + equipment slots
* [ ] Multiple dungeon floors + stairs

---

## Screenshots

*Add a `docs/` folder with `screenshot.png` or a tiny GIF and embed here.*

```
![trytrytry screenshot](docs/screenshot.png)
```

---

## Credits & License

* Built from/alongside the **Roguelike Tutorial (tcod, 2019)** by the rogueliketutorials.com community.
* New code here © 2025 Eric Janusson, released under the **MIT License** (see `LICENSE`).
* If you copied tutorial code verbatim, keep original attribution comments where present.

---

## Contributing

PRs welcome. Please:

1. Keep functions small and testable.
2. Prefer pure logic in components; keep rendering thin.
3. Add/adjust a test for any behavior change.

```bash
pip install -r requirements-dev.txt
pytest -q
ruff check .
```

---

## FAQ

**Why `python -m trytrytry`?**
Running the package avoids import gotchas and makes packaging/tests easier later.

**Why tcod?**
It's a classic roguelike stack with great docs and a batteries-included feel for rendering & input.

````

---

# .gitignore (drop-in)

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.so
*.dylib
*.egg-info/
.eggs/
.dist/
build/
dist/
.venv/
.venv*/
.env
.env.*
.pytest_cache/
.mypy_cache/
ruff_cache/
.coverage
htmlcov/

# OS/editor
.DS_Store
Thumbs.db
.vscode/
.idea/
````

---

# LICENSE (MIT template)

```text
MIT License

Copyright (c) 2025 Eric Janusson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[...standard MIT text continues...]
```

(Use the full MIT text-GitHub can auto-add it from "Add file -> Create new file -> LICENSE".)

---

# requirements.txt (safe minimal)

```txt
tcod>=13,<19
numpy>=1.24,<3
```

> If your code doesn’t use `numpy`, drop it. If it *does* use type hints or dataclasses on 3.10+, you don’t need extra deps. Pin more tightly if you want fully reproducible builds.

Optionally add a dev file:

```txt
# requirements-dev.txt
pytest>=8
ruff>=0.5
```

---

# pyproject.toml (optional but nice)

```toml
[project]
name = "trytrytry"
version = "0.1.0"
description = "Weekend Python roguelike prototype (tcod)."
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
  "tcod>=13,<19",
  "numpy>=1.24,<3",
]

[project.scripts]
trytrytry = "trytrytry.main:main"

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.pytest.ini_options]
addopts = "-q"
pythonpath = ["."]
```

This lets users `pip install -e .` and then run `trytrytry` directly.

---

# Minimal entry point (`trytrytry/main.py`)

If you don’t already have one, this tiny scaffold will run in a tcod window and call your engine:

```python
# trytrytry/main.py
from __future__ import annotations
import tcod

SCREEN_WIDTH, SCREEN_HEIGHT = 80, 50
WINDOW_TITLE = "trytrytry"

def main() -> None:
    tileset = tcod.tileset.load_tilesheet(
        "trytrytry/data/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    with tcod.context.new_terminal(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        tileset=tileset,
        title=WINDOW_TITLE,
        vsync=True,
    ) as context:
        console = tcod.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order="F")
        while True:
            console.clear()
            console.print(1, 1, "hello from trytrytry (@ to move later)")
            context.present(console)
            for event in tcod.event.wait():
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit

if __name__ == "__main__":
    main()
```

Add a tileset PNG to `trytrytry/data/` (the tutorial uses DejaVu or a cp437 tileset). You can swap this for your current engine loop.

---

# Tiny smoke test (`tests/test_import.py`)

```python
def test_imports():
    import trytrytry  # noqa: F401
```

---

# GitHub CI

* **Description & topics**: "python, roguelike, tcod, libtcod, tutorial, game-dev"
* **Default branch**: `main`
* **Actions**: add a simple CI

`.github/workflows/ci.yml`:

(For weekend code, allowing tests to soft-fail is fine.)
