from dataclasses import dataclass
from typing import List

from utils.constants import Operations


@dataclass(frozen=True)
class Command:
    operation: Operations
    value: List[str]
