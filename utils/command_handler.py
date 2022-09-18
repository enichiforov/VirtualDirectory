from typing import Dict

from utils.command_factory import Command
from utils.constants import Operations
from utils.directory import DirectoryProtocol
from utils.operations import CreateOperation, DeleteOperation, ListOperation, MoveOperation


class CommandHandler:
    def __init__(self, directories: Dict[str, DirectoryProtocol]) -> None:
        self._directories = directories
        self._operations = {
            Operations.CREATE: CreateOperation(self._directories),
            Operations.MOVE: MoveOperation(self._directories),
            Operations.DELETE: DeleteOperation(self._directories),
            Operations.LIST: ListOperation(self._directories),
        }

    def handle(self, command: Command) -> None:
        print(command.operation, end=" ")
        operation = self._operations[command.operation]
        operation.execute(command.value)
