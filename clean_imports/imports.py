import ast
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Generator


class PythonFileWalker(ABC):
    @abstractmethod
    def walk(self) -> Generator[Path, None, None]:
        pass


@dataclass
class Import:
    path: Path
    lineno: int
    column: int
    original: str
    canonical: str


def get_imports(walker: PythonFileWalker) -> Generator[Import, None, None]:
    for path in walker.walk():
        root = ast.parse(path.read_text(), path)

        for node in ast.iter_child_nodes(root):
            if isinstance(node, ast.Import):
                for n in node.names:
                    yield Import(
                        path, n.lineno, n.col_offset, ast.unparse(node), f"{n.name}"
                    )

            elif isinstance(node, ast.ImportFrom):
                for n in node.names:
                    yield Import(
                        path,
                        n.lineno,
                        n.col_offset,
                        ast.unparse(node),
                        f"{node.module}.{n.name}",
                    )
