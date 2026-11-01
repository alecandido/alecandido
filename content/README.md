# Editing the profile

The README at the root is generated: edit the files here, then run `python3 build.py`
from the repository root (or push, and the workflow rebuilds it).

- `header.md` — title and intro; `{{ banner <file> }}` and `{{ links }}` place the animation and the contact row
- `links.toml` — the contact row
- `sections.toml` — sections and the entries they contain, in order
- `entries/` — one file per entry: YAML is shown verbatim in a code block, Markdown is included as is
- `logos.toml` — the logo catalogue (light/dark files under `assets/logos/`, link, height)

The animations live in `assets/`, produced by `scripts/psi.py`: `psi-well.svg` is a
wavepacket in an infinite square well (the original one), `psi-oscillator.svg` the same in a
harmonic oscillator. Swap the file name in `header.md` to switch, or tweak the knobs at the
top of the script and run it again to regenerate them.
