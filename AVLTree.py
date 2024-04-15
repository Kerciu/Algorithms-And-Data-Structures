from dataclasses import dataclass
from typing import Optional
from BSTTree import BSTTree
from AVLNode import AVLNode


@dataclass
class AvlTree(BSTTree):
    root: Optional["AVLNode"] = None

    def insert(self, key):
        self.root = self.insertHelper(self.root, key)

    def insertHelper(self, root, key):
        root = super().insert_recursion(key, root)

        return self.balance(root)

    def getHeight(self, root):
        return root.height if root is not None else 0

    def getBalance(self, root):
        return root.left.height - root.right.height if root is not None else 0

    def coordinateBalance(self, root):
        if root is None:
            return None

        root.height = max(root.left.height, root.right.height) + 1
        balance = self.getBalance(root)

        if balance > 1:
            if self.getBalance(root.left) < 0:
                root.left = self.leftRotation(root.left)
            return self.rightRotation(root)
        elif balance < -1:
            if self.getBalance(root.right) < 0:
                root.left = self.rightRotation(root.right)
            return self.leftRotation(root)

        return root

    def rightRotation(self, root):
        B = root.right
        P = root

        root.right = B.left
        B.left = P

        P.height = max(self.getHeight(P.left), self.getHeight(P.right)) + 1
        B.height = max(self.getHeight(B.left), self.getHeight(B.right)) + 1

        return B

    def leftRotation(self, root):
        pass
