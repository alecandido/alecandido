import json
import logging
import pathlib
import re

from . import generators

pattern = re.compile(r"\{% include ([\w/]+\.\w+) %\}")


def resolve(relpath: str, workdir: pathlib.Path) -> pathlib.Path:
    """Resolve included path, or generate it.

    If the file exists, return the file path, otherwise invokes its generator.

    """
    included = workdir / relpath

    if not included.is_file():
        meta = json.loads((included.parent / "meta.json").read_text(encoding="utf-8"))
        generators.run(
            meta["generated"][included.name],
            name=included.name,
            workdir=included.parent,
        )

    return included


def apply(path: pathlib.Path) -> str:
    original = path.read_text(encoding="utf-8")
    result = []

    for line in original.splitlines():
        newlines = [line]

        matched = re.search(pattern, line)
        if matched is not None:
            depth = len(path.relative_to("/tmp").parents) + matched[1].count("/") - 2
            spacer = " " * 4 * depth
            logging.info(f"Including: {spacer} '{matched[1]}' -> '{path.name}'")
            included = resolve(matched[1], path.parent)

            # append all newlines, preserving indentation
            newlines = [
                " " * matched.pos + line for line in apply(included).splitlines()
            ]

        result += newlines

    return "\n".join(result)
