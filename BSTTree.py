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

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self.insert_recursion(value, self.root)

    def insert_recursion(self, value, root):
        if value < root.value:
            if not root.left:
                root.left = BSTNode(value)
            else:
                self.insert_recursion(value, root.left)
        elif value > root.value:
            if not root.right:
                root.right = BSTNode(value)
            else:
                self.insert_recursion(value, root.right)
        else:
            print("Number exists in the tree")

    def search(self, value):
        if not self.root:
            return False
        else:
            return self.search_recursion(value, self.root)

    def search_recursion(self, value, root):
        if value < root.value:
            if not root.left:
                return False
            else:
                return self.search_recursion(value, root.left)
        if value > root.value:
            if not root.right:
                return False
            else:
                return self.search_recursion(value, root.right)
        return True

    def delete(self, value):
        self.root = self.delete_recursion(value, self.root)

    def delete_recursion(self, value, root):
        if root is None:
            return root

        if value < root.value:
            root.left = self.delete_recursion(value, root.left)
        elif value > root.value:
            root.right = self.delete_recursion(value, root.right)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node has two children, find successor and replace value
            successor = self.find_successor(root.right)
            root.value = successor.value
            root.right = self.delete_recursion(successor.value, root.right)

        return root

    def find_successor(self, node):
        current_node = node
        while current_node.left:
            current_node = current_node.left
        return current_node

    def find_predecessor(self, node):
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node
