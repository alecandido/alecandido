# Editing the profile

The README at the root is generated: edit the files here, then run `python3 build.py`
from the repository root (or push, and the workflow rebuilds it).

- `header.md` — title and intro; `{{ banner }}` and `{{ links }}` place the animation and the contact row
- `links.toml` — the contact row
- `sections.toml` — sections and the entries they contain, in order
- `entries/` — one file per entry: YAML is shown verbatim in a code block, Markdown is included as is
- `logos.toml` — the logo catalogue (light/dark files under `assets/logos/`, link, height)

The animation is `assets/psi.svg`, produced by `scripts/psi.py`.
