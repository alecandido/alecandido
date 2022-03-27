import inspect
import json
import os
import pathlib
import re

emptyline = re.compile(r"\n\s*\n")


def run(datafile: str, *, name: str, workdir: os.PathLike):
    workdir = pathlib.Path(workdir)
    out = workdir / name

    sections = json.loads((workdir / datafile).read_text(encoding="utf-8"))

    # fill content
    content = ""

    for title, projects in sections.items():
        content += f"### {title}\n\n"

        for proj in projects:
            spacer = ""
            if "spacer" in proj:
                width = proj["spacer"]
                spacer = f"!img[spacer.png]{{width: {width}}}"

            logo = ""
            if "logo" in proj:
                url = proj["logo"]["url"]
                src = proj["logo"]["src"]
                props = proj["logo"].get("props")

                propstr = ""
                if props is not None:
                    propstr = (
                        "{"
                        + ", ".join((f"{key}: {value}" for key, value in props.items()))
                        + "}"
                    )

                logo = f"!img[{src}]({url}){propstr}"

            content += f"```yaml\n{{% include {proj['file']} %}}\n```\n"
            content += (
                inspect.cleandoc(
                    re.sub(
                        emptyline,
                        "\n",
                        f"""
                    <p align="center">
                        {logo}
                        {spacer}
                        !img[{proj["badge"]["picture"]}]({proj["badge"]["url"]})
                    </p>
                    """,
                    )
                )
                + "\n\n"
            )

    # emit output
    out.write_text(content, encoding="utf-8")
