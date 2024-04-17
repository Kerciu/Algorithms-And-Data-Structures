from BSTNode import BSTNode
from typing import Optional


class AVLNode(BSTNode):
    def __init__(self, value, left: Optional["AVLNode"] = None, right: Optional["AVLNode"] = None, height: Optional[int] = 1):
        super().__init__(value)
        self.left = left
        self.right = right
        self.height = height
