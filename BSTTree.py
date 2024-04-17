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
#  Difference in height between left and right tree
#  in AVL tree must be equal to 1
#  New element will always be a "leaf"
#

from BSTNode import BSTNode


class BSTTree:
    def __init__(self):
        self.root = None

    def copy(self):
        # Creates a new tree and copies the root
        new_tree = BSTTree()
        new_tree.root = self.root
        return new_tree

    def insert(self, value):
        # Inserts a new value into the tree

        if self.root is None:
            # If the tree is empty, the new value becomes the root
            self.root = BSTNode(value)

        else:
            # If the tree is not empty, call the recursive insert method
            self.insert_recursion(value, self.root)

    def insert_recursion(self, value, root):
        # Recursively inserts a new value into the tree

        if value < root.value:
            # If the value is less than the current node's value, move to the left subtree

            if not root.left:
                # If the left child is None, insert the new node as the left child
                root.left = BSTNode(value)

            else:
                # If the left child exists, recursively call insert on the left subtree
                self.insert_recursion(value, root.left)

        elif value > root.value:
            # If the value is greater than the current node's value, move to the right subtree

            if not root.right:
                # If the right child is None, insert the new node as the right child
                root.right = BSTNode(value)

            else:
                # If the right child exists, recursively call insert on the right subtree
                self.insert_recursion(value, root.right)

        else:
            # If the value already exists in the tree, do nothing
            return root

    def search(self, value):
        # Searches for a value in the Binary Search Tree
        # Returns True if the value is found, False otherwise
        if not self.root:
            return False
        else:
            return self.search_recursion(value, self.root)

    def search_recursion(self, value, root):
        # Recursively searches for a value in the tree

        if value < root.value:
            # If searched value is less than value of root, go left

            if not root.left:
                return False
            else:
                return self.search_recursion(value, root.left)

        if value > root.value:
            # If searched value is less than value of root, go right

            if not root.right:
                return False
            else:
                return self.search_recursion(value, root.right)

        return True

    def delete(self, value):
        # Deletes a node with the given value from the tree
        self.root = self.delete_recursion(value, self.root)

    def delete_recursion(self, value, root):
        # Recursively deletes a node with the given value from the tree

        if root is None:
            return root

        if value < root.value:
            # If desirable value is less than value of root, go left
            root.left = self.delete_recursion(value, root.left)

        elif value > root.value:
            # If desirable value is greater than value of root, go right
            root.right = self.delete_recursion(value, root.right)

        else:
            # Check whether the left and left nodes are none if desirable value is equal to root val
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node has two children, find successor and replace value
            else:
                successor = self.find_successor(root.right)
                root.value = successor.value
                root.right = self.delete_recursion(successor.value, root.right)

        return root

    def find_successor(self, node):
        # Finds the successor of a given node
        current_node = node

        # Go left
        while current_node.left:
            current_node = current_node.left
            
        return current_node

    def find_predecessor(self, node):
        # Finds the predecessor of a given node
        current_node = node

        # Go right
        while current_node.right:
            current_node = current_node.right

        return current_node

    def print_tree(self):
        self._print_tree_horizontal(self.root, 0)

    def _print_tree_horizontal(self, node, indent):
        if node is not None:
            self._print_tree_horizontal(node.right, indent + 4)
            print(' ' * indent + str(node.value))
            self._print_tree_horizontal(node.left, indent + 4)
