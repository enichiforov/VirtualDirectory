from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

from utils.directory import Directory
from utils.protocols import DirectoryProtocol


class AbstractOperation(ABC):
    def __init__(self, directories: Dict[str, DirectoryProtocol]) -> None:
        self._directories = directories

    @abstractmethod
    def execute(self, value: List[str]) -> None:
        pass

    def _get_directories_names(self, value: str) -> List[str]:
        return value.split("/")

    def _get_required_and_last_directory_name(self, directories_names: List[str]) -> Tuple[DirectoryProtocol, str]:
        last_directory_name = directories_names[-1]

        required_directory = None
        for index, directory_name in enumerate(directories_names):
            if not required_directory:
                required_directory = self._directories[directory_name]
                continue
            if index == (len(directories_names) - 1):
                break
            sub_directory = required_directory.get_child(directory_name)
            if sub_directory:
                required_directory = sub_directory
        return required_directory, last_directory_name  # type: ignore


class CreateOperation(AbstractOperation):
    def execute(self, value: List[str]) -> None:
        print(value[0])
        directories_names = self._get_directories_names(value[0])

        current_directory = None
        for directory_name in directories_names[::-1]:
            directory = Directory(directory_name)
            if not current_directory:
                current_directory = directory
                continue
            directory.add(current_directory)
            current_directory = directory

        if current_directory:
            self._directories[current_directory.name] = current_directory


class MoveOperation(AbstractOperation):
    def execute(self, value: List[str]) -> None:
        print(value[0])
        directories_names, target_directory_name = value[0].split(" ")
        directories_names = directories_names.split("/")

        target_directory = self._directories[target_directory_name]

        if len(directories_names) == 1:
            directory = self._directories.pop(directories_names[0])
            target_directory.add(directory)
            return

        required_directory, last_directory_name = self._get_required_and_last_directory_name(directories_names)

        required_directory.move(last_directory_name, target_directory)


class DeleteOperation(AbstractOperation):
    def execute(self, value: List[str]) -> None:
        print(value[0])
        directories_names = self._get_directories_names(value[0])
        if directories_names[0] not in self._directories:
            print(f"Cannot delete {value[0]} - {directories_names[0]} does not exist")
            return

        required_directory, last_directory_name = self._get_required_and_last_directory_name(directories_names)
        required_directory.remove(last_directory_name)


class ListOperation(AbstractOperation):
    def execute(self, value: List[str]) -> None:
        print("")
        for directory in self._directories.values():
            directory.view()
