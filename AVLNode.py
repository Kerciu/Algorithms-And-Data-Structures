from dataclasses import dataclass
from BSTNode import BSTNode
from typing import Optional


@dataclass
class AVLNode(BSTNode):
    height: Optional["int"] = None
