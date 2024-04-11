from dataclasses import dataclass
from BSTTree import BSTTree


@dataclass
class AlTree(BSTTree):
    bal: int        # {-1, 0, 1}
