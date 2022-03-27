import importlib
import logging
import os
import typing


def run(recipe: dict[str, typing.Any], name: str, workdir: os.PathLike):
    """Run recipe to generate file.

    The recipe is a `dict`, specifying the ``generator`` and the related
    ``input`` (as a sequence of arguments for the generator).

    Parameters
    ----------
    recipe: dict
        the recipe to run
    name: str
        the name of the file to generate
    workdir: os.PathLike
        the working directory

    """
    genname = recipe["generator"]
    logging.info(f"Running generator -> {genname}")

    generator = importlib.import_module(f".{genname}", __name__)
    generator.run(*recipe["input"], name=name, workdir=workdir)
