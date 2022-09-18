from typing import Dict, List

from parser import Parser
from utils import Command, CommandFactory, CommandHandler, DirectoryProtocol, FileReader


class DirectoryFacade:
    def __init__(self, file_name: str) -> None:
        self._file_name = file_name
        self._directories: Dict[str, DirectoryProtocol] = {}
        self._command_handler = CommandHandler(self._directories)
        self._file_reader = FileReader()

    def _get_raw_commands(self) -> List[str]:
        self._file_reader.read(self._file_name)
        return self._file_reader.raw_commands

    def _transale_raw_commands_into_commands(self, raw_commands: List[str]) -> List[Command]:
        commands = []
        for raw_command in raw_commands:
            command_factory = CommandFactory(raw_command)
            command = command_factory.create()
            commands.append(command)
        return commands

    def organize_directories(self) -> None:
        raw_commands = self._get_raw_commands()
        commands = self._transale_raw_commands_into_commands(raw_commands)
        for command in commands:
            self._command_handler.handle(command)


if __name__ == '__main__':
    parser = Parser()
    file_name = parser.get_file_name()

    directory_facade = DirectoryFacade(file_name)
    directory_facade.organize_directories()
