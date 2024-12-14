from pathlib import Path
from typing import Generator

from clean_imports.imports import PythonFileWalker


class FixedWalker(PythonFileWalker):
    def __init__(self, path: Path, s: str) -> None:
        self.path = path
        self.s = s

    def walk(self) -> Generator[Path, None, None]:
        self.path.write_text(self.s)
        yield self.path
