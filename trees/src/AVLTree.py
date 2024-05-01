from dataclasses import dataclass
from typing import Optional
from BSTTree import BSTTree
from AVLNode import AVLNode


@dataclass
class AvlTree(BSTTree):
    root: Optional["AVLNode"] = None

    def insert(self, key):
        # Defining a method to insert a key into the AVL Tree.
        self.root = self.insertHelper(self.root, key)

    def insertHelper(self, root, key):
        # Defining a helper method for inserting a key into the AVL Tree.
        
        if not root:
            # If the root is None, create a new AVLNode with the key.
            return AVLNode(key)

        if key < root.value:
            # If the key is less than the value at the current node, go left.
            root.left = self.insertHelper(root.left, key)

        elif key > root.value:
            # If the key is greater than the value at the current node, go right.
            root.right = self.insertHelper(root.right, key)

        # Update the height of the current node based on the maximum height of its children.
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Balance the tree after insertion and return the new root.
        return self.coordinateBalance(root, key)

    def getHeight(self, root):
        # Return the height if the node exists, otherwise return 0.
        return root.height if root else 0

    def getBalance(self, root):
        # Calculating balance factor.
        return self.getHeight(root.left) - self.getHeight(root.right) if root else 0

    def coordinateBalance(self, root, key):
        # Defining a method to balance the AVL Tree.

        if root is None:
            # If the root is None, return None.
            return None
        
        # Calculate the balance factor of the current node.
        balanceFactor = self.getBalance(root)

        if balanceFactor > 1:
            # If balance factor is greater than 1, perform rotations.

            if key < root.left.value:
                # If the key is less than the left child's value, perform a right rotation.
                return self.rightRotation(root)

            else:
                # Otherwise, perform a left-right rotation.
                root.left = self.leftRotation(root.left)
                return self.rightRotation(root)
            
        elif balanceFactor < -1:
            # If balance factor is less than -1, perform rotations.

            if key > root.right.value:
                # If the key is greater than the right child's value, perform a left rotation.
                return self.leftRotation(root)

            else:
                # Otherwise, perform a right-left rotation.
                root.right = self.rightRotation(root.right)
                return self.leftRotation(root)

        # Return the balanced node.
        return root

    def rightRotation(self, z):
        # Defining a method for right rotation.

        y = z.left # Set y as the left child of z
        T2 = y.right # Store the right subtree of y.

        # Perform rotation.
        y.right = z
        z.left = T2

        # Update heights.
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        
        # Return the new root of the subtree.
        return y

    def leftRotation(self, z):
        # Defining a method for left rotation.

        y = z.right # Set y as the right child of z.
        T2 = y.left # Store the left subtree of y.

        # Perform rotation.
        y.left = z
        z.right = T2

        # Update heights.
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root of the subtree.
        return y
