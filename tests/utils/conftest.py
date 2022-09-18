import pytest

from utils import DirectoryProtocol
from utils.directory import Directory

@pytest.fixture(scope="function")
def default_directory() -> DirectoryProtocol:
    return Directory("default")