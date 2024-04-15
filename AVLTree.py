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
        if not root:
            return AVLNode(key)

        if key < root.value:
            root.left = self.insertHelper(root.left, key)
        elif key > root.value:
            root.right = self.insertHelper(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        return self.coordinateBalance(root, key)

    def getHeight(self, root):
        return root.height if root else 0

    def getBalance(self, root):
        return self.getHeight(root.left) - self.getHeight(root.right) if root else 0

    def coordinateBalance(self, root, key):
        if root is None:
            return None
        
        balanceFactor = self.getBalance(root)

        if balanceFactor > 1:
            if key < root.left.value:
                return self.rightRotation(root)
            else:
                root.left = self.leftRotation(root.left)
                return self.rightRotation(root)
            
        elif balanceFactor < -1:
            if key > root.right.value:
                return self.leftRotation(root)
            else:
                root.right = self.rightRotation(root.right)
                return self.leftRotation(root)

        return root

    def rightRotation(self, z):
        y = z.left
        T2 = y.right
        y.right = z
        z.left = T2

        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def leftRotation(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def print_tree(self):
        self._print_tree_horizontal(self.root, 0)

    def _print_tree_horizontal(self, node, indent):
        if node is not None:
            self._print_tree_horizontal(node.right, indent + 4)
            print(' ' * indent + str(node.value))
            self._print_tree_horizontal(node.left, indent + 4)
