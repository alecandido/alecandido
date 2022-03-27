import logging
import os
import pathlib
import shutil
import tempfile

from . import dsl, include

root = pathlib.Path(__file__).parents[1]
src = root / "src"
entry = "index.md"
output = "README.md"

LOGLEVEL = os.environ.get("LOGLEVEL", "WARNING").upper()
FORMAT = " <| {levelname} - {asctime} |>  {message} "
DATEFMT = "%H:%M:%S"
logging.basicConfig(level=LOGLEVEL, format=FORMAT, style="{", datefmt=DATEFMT)


def main():
    logging.info("Start README compilation")

    with tempfile.TemporaryDirectory() as tmpdir:
        logging.info(f"Working in tmp directory: '{tmpdir}'")
        tmpdir = pathlib.Path(tmpdir)

        # copy the source files
        shutil.copytree(src, tmpdir / "src")

        # start from entry point
        content = include.apply(tmpdir / "src" / entry)

        # post-process
        interpreted = dsl.main(content)

        (tmpdir / output).write_text(interpreted, encoding="utf-8")

        # emit output and clean up
        shutil.copyfile(tmpdir / output, root / output)
