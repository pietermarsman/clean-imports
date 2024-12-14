from pathlib import Path

from clean_imports.fixed_walker import FixedWalker
from clean_imports.imports import Import, get_imports


def test_import(tmpfile: Path) -> None:
    walker = FixedWalker(tmpfile, "import pathlib")

    imports = list(get_imports(walker))

    assert imports == [
        Import(
            tmpfile,
            1,
            7,
            "import pathlib",
            "pathlib",
        ),
    ]


def test_from_import(tmpfile: Path) -> None:
    walker = FixedWalker(tmpfile, "from pathlib import Path")

    imports = list(get_imports(walker))

    assert imports == [
        Import(
            tmpfile,
            1,
            20,
            "from pathlib import Path",
            "pathlib.Path",
        )
    ]
