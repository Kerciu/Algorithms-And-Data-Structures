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

from dataclasses import dataclass
from BSTNode import BSTNode
from typing import Optional


@dataclass
class BSTTree:
    root: Optional["BSTNode"] = None

    def successor(self, root: BSTNode) -> int:
        # Find the least value below the right child of this root node
        root = root.right
        while root.left is not None:
            root = root.left

        return root.val

    def predecessor(self, root: BSTNode) -> int:
        root = root.left
        while root.right is not None:
            root = root.right
        
        return root.val

    # --------------------------------------------------
    #                  Element Search
    # --------------------------------------------------

    def searchForElememt(self, data: int) -> bool:
        return self.searchHelper(data)

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
        
        # If none return root
        if root is None:
            root = node

        # If element in tree, do not instert
        if not self.searchForElememt(node.val):
            self.root = self.insertHelper(self.root, node)

    def insertHelper(self, root: BSTNode, node: BSTNode) -> BSTNode:

        if root is None:
            return node

        # We are going to the left node
        elif root.val > node.val:
            root.left = self.insertHelper(root.left, node)

        # We are going to the right node
        else:
            root.right = self.insertHelper(root.right, node)

        return root

    # --------------------------------------------------
    #                  Delete Element
    # --------------------------------------------------

    def deleteElement(self, key: int) -> None:
        if self.searchForElememt(key):
            self.deleteHelper(self.root, key)

    def deleteHelper(self, root: BSTNode, key: int) -> BSTNode:
        if root is None:
            return None

        elif root.val > key:
            root.left = self.deleteHelper(root.left, key)

        elif root.val < key:
            root.right = self.deleteHelper(root.left, key)

        # We have found the node
        else:
            # We are deleting a leaf node
            if root.left is None and root.right is None:
                del root

            # Find a succesor to replace this node
            elif root.right is not None:
                # If the node has right child we find successor to fill that gap
                # The successor shall have the least value
                root.val = self.successor(root)
                root.right = self.deleteHelper(root, key)

            # Find a predecessor to replace this node
            elif root.left is not None:
                # If the node has left child we find predecessor to fill that gap
                # The predecessor shall have the greatest value
                root.val = self.predecessor(root)
                root.left = self.deleteHelper(root, key)
        
        return root

    # --------------------------------------------------
    #                 Display Element
    # --------------------------------------------------

    def displayTree(self) -> None:
        self.displayHelper(self.root)

    def displayHelper(self, root: BSTNode) -> None:
        if root is not None:
            self.displayHelper(root.left)
            print(root.val)
            self.displayHelper(root.right)

    # --------------------------------------------------
