from dataclasses import dataclass


@dataclass
class AlTree:
    val: int
    left: int
    right: int
    bal: int        # {-1, 0, 1}
