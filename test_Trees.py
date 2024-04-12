from BSTNode import BSTNode
import random


def test_create_tree():
    tree = BSTNode(5)
    values = [3, 8, 2, 4, 7, 10]
    for val in values:
        tree.insert(val)

    assert tree.value == 5
    assert tree.left.value == 3
    assert tree.right.value == 8
    assert tree.left.left.value == 2
    assert tree.left.right.value == 4
    assert tree.right.left.value == 7
    assert tree.right.right.value == 10


def test_search_for_element():
    tree = BSTNode(10)
    vals = [i for i in range(1, 10)]
    random.shuffle([vals])
    for val in vals:
        tree.insert(val)

    assert tree.search(5) is True
    assert tree.search(11) is False


def test_find_successor():
    tree = BSTNode(5)
    values = [3, 8, 2, 4, 7, 10]
    for val in values:
        tree.insert(val)
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
