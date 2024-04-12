from BSTTree import BSTTree
from BSTNode import BSTNode
import random


def test_create_tree():
    tree = BSTTree()
    vals = [i for i in range(1, 11)]
    random.shuffle([vals])
    for val in vals:
        tree.insertElement(BSTNode(val))

    assert tree.root.val == 5
    assert tree.root.right.val == 5
    assert tree.root.left.val == 4


def test_search_for_element():
    tree = BSTTree()
    tree_empty = BSTTree()
    vals = [i for i in range(1, 11)]
    random.shuffle([vals])
    for val in vals:
        tree.insertElement(BSTNode(val))

    assert tree.searchForElememt(5) is True
    assert tree.searchForElememt(11) is False
    assert tree_empty.searchForElememt(200) is False
