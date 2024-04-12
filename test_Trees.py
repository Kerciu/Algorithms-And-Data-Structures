from BSTTree import BSTTree


def test_create_tree():
    tree = BSTTree()
    values = [5, 3, 8, 2, 4, 7, 10]
    for val in values:
        tree.insert(val)

    assert tree.root.value == 5
    assert tree.root.left.value == 3
    assert tree.root.right.value == 8
    assert tree.root.left.left.value == 2
    assert tree.root.left.right.value == 4
    assert tree.root.right.left.value == 7
    assert tree.root.right.right.value == 10


def test_search_for_element():
    tree = BSTTree()
    tree_empty = BSTTree()
    values = [i for i in range(1, 11)]
    for val in values:
        tree.insert(val)
    assert tree.search(5) is True
    assert tree.search(11) is False
    assert tree_empty.search(200) is False


def test_find_successor():
    tree = BSTTree()
    values = [5, 3, 8, 2, 4, 7, 10]
    for val in values:
        tree.insert(val)

    assert tree.find_successor(tree.root).value == 2


def test_find_predecessor():
    tree = BSTTree()
    values = [5, 3, 8, 2, 4, 7, 10]
    for val in values:
        tree.insert(val)

    assert tree.find_predecessor(tree.root).value == 10


def test_delete_element():
    tree = BSTTree()
    values = [5, 3, 8, 2, 4, 7, 10]
    for val in values:
        tree.insert(val)

    tree.delete(3)
    tree.delete(8)
    tree.delete(5)

    assert tree.search(3) is False
    assert tree.search(8) is False
    assert tree.search(5) is False
