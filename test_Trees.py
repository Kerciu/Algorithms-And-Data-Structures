from BSTTree import BSTTree
from BSTNode import BSTNode
import random


def test_create_tree():
    tree = BSTTree()
    values = [5, 3, 8, 2, 4, 7, 10]
    for val in values:
        tree.insertElement(BSTNode(val))

    assert tree.root.val == 5
    assert tree.root.left.val == 3
    assert tree.root.right.val == 8
    assert tree.root.left.left.val == 2
    assert tree.root.left.right.val == 4
    assert tree.root.right.left.val == 7
    assert tree.root.right.right.val == 10


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


def test_find_successor():
    tree = BSTTree()
    values = [5, 3, 8, 2, 4, 7, 10]
    for val in values:
        tree.insertElement(BSTNode(val))

    assert tree.successor(tree.root) == 7


def test_find_predecessor():
    tree = BSTTree()
    values = [5, 3, 8, 2, 4, 7, 10]
    for val in values:
        tree.insertElement(BSTNode(val))

    assert tree.predecessor(tree.root) == 4


def test_delete_element():
    tree = BSTTree()
    values = [5, 3, 8, 2, 4, 7, 10]
    for val in values:
        tree.insertElement(BSTNode(val))

    tree.deleteElement(3)
    tree.deleteElement(8)
    tree.deleteElement(5)

    assert tree.searchForElement(3) is False
    assert tree.searchForElement(8) is False
    assert tree.searchForElement(5) is False
