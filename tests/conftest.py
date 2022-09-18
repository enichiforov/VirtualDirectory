import io
from contextlib import redirect_stdout

import pytest
from main import DirectoryFacade


@pytest.fixture(scope='session')
def directory_facade() -> DirectoryFacade:
    return DirectoryFacade("input.txt")


@pytest.fixture(scope='session')
def stdout(directory_facade: DirectoryFacade) -> io.StringIO:
    file = io.StringIO()
    with redirect_stdout(file):
        directory_facade.organize_directories()
    return file
