from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest


@pytest.fixture
def tmpfile() -> Path:
    with NamedTemporaryFile() as f:
        yield Path(f.name)
