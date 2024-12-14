from pathlib import Path
from typing import Generator, Union

from clean_imports.imports import PythonFileWalker


class PathlibWalker(PythonFileWalker):
    def __init__(self, path: Union[Path, str]) -> None:
        self.path = Path(path)

    def walk(self) -> Generator[Path, None, None]:
        for path in self.path.rglob("*.py"):
            yield path
