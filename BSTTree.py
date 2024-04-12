# If element in tree : do not insert
# If deleting non existent element : tree remains unchanged
#           10
#          /  \
#         7    13
#        / \   /
#       4   9 11
#      / \      \
#     3   5      12
#        / \
#      4.5  6
#
#  Difference in height between left and right tree in AVL tree must be equal to 1
#  New element will always be a "leaf"
#
from dataclasses import dataclass
from BSTNode import BSTNode
from typing import Optional


@dataclass
class BSTTree:
    root: Optional["BSTNode"] = None

    def succesor(root: BSTNode):
        pass

    def predecesor(root: BSTNode):
        pass

    # --------------------------------------------------
    #                  Element Search
    # --------------------------------------------------
    def searchForElememt(self, node: BSTNode) -> bool:
        return self.searchHelper(node)

    def searchHelper(self, root: BSTNode, data: int) -> BSTNode:
        if root is None:
            return False

        elif root.val == data:
            return True

        elif root.val > data:
            self.searchHelper(root.left, data)
        else:
            self.searchHelper(root.right, data)

    # --------------------------------------------------
    #                  Insert Element
    # --------------------------------------------------

    def insertElement(self, node: BSTNode) -> None:
        self.root = self.insertHelper(self.root, node)

    def insertHelper(self, root: BSTNode, node: BSTNode) -> BSTNode:
        # TODO If element in tree, do not instert
        if self.searchForElememt(node):
            return root
        
        # If none return root
        if root is None:
            root = node
            return root

        # We are going to the left node
        elif root.val > node.val:
            root.left = self.insertHelper(root.left, node)

        # We are going to the right node
        elif root.val < node.val:
            root.right = self.insertHelper(root.right, node)

        return root

    def deleteElement(node: BSTNode) -> None:
        pass

    def deleteHelper(root: BSTNode, node: BSTNode) -> BSTNode:
        pass

    def displayTree(self) -> None:
        self.displayHelper(self.root)

    def displayHelper(self, root: BSTNode) -> None:
        if root is not None:
            self.displayHelper(root.left)
            print(root.val)
            self.displayHelper(root.right)
