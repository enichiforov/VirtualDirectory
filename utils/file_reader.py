from typing import List


class FileReader:
    def __init__(self) -> None:
        self._raw_commands: List[str] = []

    @property
    def raw_commands(self) -> List[str]:
        return self._raw_commands

    def read(self, file_name: str) -> None:
        with open(f"{file_name}", "r") as file:
            for line in file.readlines():
                self._raw_commands.append(line.splitlines()[-1])
