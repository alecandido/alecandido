import json
import os
import pathlib


def run(datafile: str, *, name: str, workdir: os.PathLike):
    workdir = pathlib.Path(workdir)
    out = workdir / name

    items = json.loads((workdir / datafile).read_text(encoding="utf-8"))

    # fill content
    content = ""

    for info in items.values():
        content += f"- {info}\n"

    # emit output
    out.write_text(content, encoding="utf-8")
