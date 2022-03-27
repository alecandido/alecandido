import json
import os
import pathlib


def run(datafile: str, *, name: str, workdir: os.PathLike):
    workdir = pathlib.Path(workdir)
    out = workdir / name

    sections = json.loads((workdir / datafile).read_text(encoding="utf-8"))

    # fill content
    content = ""

    for title, parts in sections.items():
        if title == "footer":
            continue
        content += f"\n### {title}\n\n"

        for part in parts:
            thumbnails = []
            for elem in part["elems"]:
                if isinstance(elem, dict):
                    src = "code/" + elem["logo"]["src"]
                    height = elem["logo"]["height"]
                    url = elem["url"]

                    thumbnails.append(f"!img[{src}]({url}){{height: {height}}}")
                elif isinstance(elem, str):
                    thumbnails.append(elem)
                else:
                    raise ValueError(f"Element not recognized: {elem}")

            content += f"- {part['descr']}: " + " ".join(thumbnails) + "\n"

    content += "\n\n" + sections["footer"]

    # emit output
    out.write_text(content, encoding="utf-8")
