from Heap import Heap


def test_create_heap():
    two_arity_heap = Heap(2)
    assert two_arity_heap.get_arity() == 2
