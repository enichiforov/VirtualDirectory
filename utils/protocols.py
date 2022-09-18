from __future__ import annotations

from typing import Optional, Protocol


class DirectoryProtocol(Protocol):

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def parent_name(self) -> str:
        raise NotImplementedError

    @parent_name.setter
    def parent_name(self, parent_name: str) -> None:
        raise NotImplementedError

    def get_child(self, directory_name: str) -> Optional[DirectoryProtocol]:
        raise NotImplementedError

    def add(self, directory: DirectoryProtocol) -> None:
        raise NotImplementedError

    def remove(self, directory_name: str) -> DirectoryProtocol:
        raise NotImplementedError

    def move(self, directory_name: str, target_directory: DirectoryProtocol) -> None:
        raise NotImplementedError

    def view(self, depth: int = 0) -> None:
        raise NotImplementedError
