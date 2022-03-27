import inspect
import json
import os
import pathlib


def run(datafile: str, *, name: str, workdir: os.PathLike):
    workdir = pathlib.Path(workdir)
    out = workdir / name

    sections = json.loads((workdir / datafile).read_text(encoding="utf-8"))

    # fill content
    content = ""

    for section in sections:
        title = section["title"]
        filename = section["file"]

        content += (
            inspect.cleandoc(
                f"""
            <details>
                <summary> <b> {title} </b> </summary>
            
            ## {title}

            {{% include sections/{filename} %}}

            </details>
            """
            )
            + "\n\n"
        )

    # emit output
    out.write_text(content, encoding="utf-8")
