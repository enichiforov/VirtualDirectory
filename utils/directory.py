from abc import ABC, abstractmethod
from typing import Dict, Optional

from utils.protocols import DirectoryProtocol


class AbstractDirectory(ABC):
    def __init__(self, name: str) -> None:
        self._name = name
        self._parent_name = ""
        self._directories: Dict[str, DirectoryProtocol] = {}

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}"
                f"(name={self._name!r}, dirs={self._directories})")

    @property
    def name(self) -> str:
        return self._name

    @property
    def parent_name(self) -> str:
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name: str) -> None:
        self._parent_name = parent_name

    @abstractmethod
    def get_child(self, directory_name: str) -> Optional[DirectoryProtocol]:
        pass

    @abstractmethod
    def add(self, directory: DirectoryProtocol) -> None:
        pass

    @abstractmethod
    def remove(self, directory_name: str) -> DirectoryProtocol:
        pass

    @abstractmethod
    def move(self, directory_name: str, target_directory: DirectoryProtocol) -> None:
        pass

    @abstractmethod
    def view(self, depth: int = 0) -> None:
        pass


class Directory(AbstractDirectory):

    def get_child(self, directory_name: str) -> Optional[DirectoryProtocol]:
        return self._directories.get(directory_name)

    def add(self, directory: DirectoryProtocol) -> None:
        directory.parent_name = self._name
        self._directories[directory.name] = directory

    def remove(self, directory_name: str) -> DirectoryProtocol:
        return self._directories.pop(directory_name)

    def move(self, directory_name: str, target_directory: DirectoryProtocol) -> None:
        directory = self.remove(directory_name)
        target_directory.add(directory)

    def view(self, depth: int = 0) -> None:
        if self._parent_name:
            depth += 1
            indent = "  " * depth
            print(f"{indent}{self._name}")
        else:
            print(self._name)

        for directory in self._directories.values():
            directory.view(depth)
