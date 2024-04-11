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


@dataclass
class BSTTree:
    val: int
    left: int
    right: int

