from utils.models import Command


class CommandFactory:
    def __init__(self, raw_command: str) -> None:
        self._raw_command = raw_command

    def create(self) -> Command:
        operation, *value = self._raw_command.split(" ", 1)
        return Command(operation, value)  # type: ignore
