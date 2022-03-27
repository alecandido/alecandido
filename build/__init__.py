import pathlib
import tempfile

from . import dsl

src = pathlib.Path(__file__).parents[1] / "src"
entry = src / "index.md"


def main():

    with tempfile.TemporaryDirectory() as tmpdir:
        print(tmpdir)
        # start from entry point
        print(*(p.name for p in src.glob("*")), sep="\n")
        print(entry.read_text(encoding="UTF-8"))

        # post-process
        dsl.main()

    # emit output and clean up
    print("Ciao, come va?")
