from utils import DirectoryProtocol
from utils.directory import Directory

def test_directory_add(default_directory: DirectoryProtocol) -> None:
    test_directory = Directory("test_directory")
    default_directory.add(test_directory)

    assert default_directory.name == test_directory.parent_name
    assert test_directory == default_directory.get_child(test_directory.name)

def test_directory_move(default_directory: DirectoryProtocol) -> None:
    test_directory = Directory("test_directory")
    movable_directory = Directory("movable_directory")
    default_directory.add(movable_directory)

    default_directory.move(movable_directory.name, test_directory)

    assert test_directory.name == movable_directory.parent_name
    assert movable_directory == test_directory.get_child(movable_directory.name)
    assert default_directory.get_child(movable_directory.name) is None

