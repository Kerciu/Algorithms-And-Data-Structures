from dataclasses import dataclass


@dataclass
class BSTNode:
    val: int
    left: Optional["BSTNode"] = None
    right: Optional["BSTNode"] = None

