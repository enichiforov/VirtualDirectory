from argparse import ArgumentParser, Namespace


class Parser:
    def __init__(self) -> None:
        self.parser = ArgumentParser(description='Create virtual directories')

    def get_file_name(self) -> str:
        args = self._get_args()
        return args.file_name

    def _get_args(self) -> Namespace:
        self.parser.add_argument(
            "-f",
            "--filename",
            dest="file_name",
            type=str,
            nargs="?",
            default="input.txt",
            metavar="",
            help="Filename to use to for parsing",
        )
        args = self.parser.parse_args()
        return args
