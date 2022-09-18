import io

import pytest


@pytest.mark.parametrize(
    "file_name, expected_diffrence",
    [
        ("tests/outputs/right.txt", False),
        ("tests/outputs/wrong.txt", True),
    ],
)
def test_organize_directories(stdout: io.StringIO, file_name: str, expected_diffrence: bool) -> None:
    stdout = stdout.getvalue().splitlines()

    with open(file_name) as file:
        diffrence = set(file.read().splitlines()).difference(stdout)

    assert expected_diffrence == bool(diffrence)
