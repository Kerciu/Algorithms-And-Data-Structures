from Heap import Heap, NotInHeapError, NoParentFoundError, EmptyHeapError
import pytest


def test_Heap_get_arity():
    two_arity_heap = Heap(2)
    assert two_arity_heap.get_arity == 2


def test_get_parent():
    i = 9
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert two_arity_heap.get_parent(i) == 4
    assert five_arity_heap.get_parent(i) == 1
    assert seven_arity_heap.get_parent(i) == 1


def test_get_parent2():
    i = 21
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert two_arity_heap.get_parent(i) == 10
    assert five_arity_heap.get_parent(i) == 4
    assert seven_arity_heap.get_parent(i) == 3


def test_get_parent_no_parent():
    i = 0
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    with pytest.raises(NoParentFoundError) as e:
        two_arity_heap.get_parent(i) == 4
        five_arity_heap.get_parent(i) == 2
        seven_arity_heap.get_parent(i) == 2


def test_Heap_sort_empty():
    list_to_sort = []
    result = []
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert result == two_arity_heap.build_max_heap(list_to_sort)
    assert result == five_arity_heap.build_max_heap(list_to_sort)
    assert result == seven_arity_heap.build_max_heap(list_to_sort)


def test_Heap_sort_one_argument():
    list_to_sort = [2]
    result = [2]
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert result == two_arity_heap.build_max_heap(list_to_sort)
    assert result == five_arity_heap.build_max_heap(list_to_sort)
    assert result == seven_arity_heap.build_max_heap(list_to_sort)


def test_Heap_sort_many_arguments():
    list_to_sort = [2, 5, 1, 3, 0, 8, 9, 6, 7, 4]
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert [9, 7, 8, 6, 4, 2, 1, 5, 3, 0] == two_arity_heap.build_max_heap(list_to_sort)
    assert [9, 7, 1, 3, 0, 8, 5, 6, 2, 4] == five_arity_heap.build_max_heap(list_to_sort)
    assert [9, 7, 1, 3, 0, 8, 2, 6, 5, 4] == seven_arity_heap.build_max_heap(list_to_sort)


def test_Heap_sort_many_arguments_same():
    list_to_sort = [2, 5, 2, 3, 0, 2, 9, 2, 7, 4]
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert [9, 7, 2, 5, 4, 2, 2, 2, 3, 0] == two_arity_heap.build_max_heap(list_to_sort)
    assert [9, 7, 2, 3, 0, 2, 5, 2, 2, 4] == five_arity_heap.build_max_heap(list_to_sort)
    assert [9, 7, 2, 3, 0, 2, 2, 2, 5, 4] == seven_arity_heap.build_max_heap(list_to_sort)


def test_add_element_to_empty_heap():
    list_to_sort = []
    element_to_add = 43
    result = [43]
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert result == two_arity_heap.add_max(list_to_sort, element_to_add)
    assert result == five_arity_heap.add_max(list_to_sort, element_to_add)
    assert result == seven_arity_heap.add_max(list_to_sort, element_to_add)


def test_add_element():
    list_to_sort = [2, 5, 1, 3, 0, 8, 9, 6, 7, 4]
    element_to_add = 43
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert [43, 7, 9, 6, 5, 8, 1, 2, 3, 4, 0] == two_arity_heap.add_max(list_to_sort, element_to_add)
    assert [43, 9, 1, 3, 0, 8, 2, 6, 7, 4, 5] == five_arity_heap.add_max(list_to_sort, element_to_add)
    assert [43, 7, 1, 3, 0, 8, 9, 6, 2, 4, 5] == seven_arity_heap.add_max(list_to_sort, element_to_add)


def test_add_element_not_root():
    list_to_sort = [2, 53, 1, 3, 0, 8, 9, 6, 7, 4]
    element_to_add = 5
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert [53, 7, 9, 6, 5, 8, 1, 2, 3, 4, 0] == two_arity_heap.add_max(list_to_sort, element_to_add)
    assert [53, 9, 1, 3, 0, 8, 2, 6, 7, 4, 5] == five_arity_heap.add_max(list_to_sort, element_to_add)
    assert [53, 7, 1, 3, 0, 8, 9, 6, 2, 4, 5] == seven_arity_heap.add_max(list_to_sort, element_to_add)


def test_remove_element_from_the_list():
    list_to_sort = [2, 53, 1, 3, 0, 8, 9, 6, 7, 5, 4, 15, 4, 123, 432, 21, 6, 87, 10, 23, 11, 19]
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert [123, 87, 15, 53, 23, 8, 9, 21, 10, 11, 19, 4, 4, 1, 2, 6, 6, 7, 3, 5, 0] == two_arity_heap.delete_max(two_arity_heap.build_max_heap(list_to_sort))
    assert [123, 53, 21, 87, 19, 8, 9, 6, 7, 5, 4, 15, 4, 2, 1, 0, 6, 3, 10, 23, 11] == five_arity_heap.delete_max(five_arity_heap.build_max_heap(list_to_sort))
    assert [123, 53, 87, 3, 0, 8, 9, 6, 7, 5, 4, 15, 4, 2, 19, 21, 6, 1, 10, 23, 11] == seven_arity_heap.delete_max(seven_arity_heap.build_max_heap(list_to_sort))


def test_remove_element_empty_list():
    list_to_sort = []
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    with pytest.raises(EmptyHeapError) as e:
        two_arity_heap.delete_max(two_arity_heap.build_max_heap(list_to_sort))
        five_arity_heap.delete_max(five_arity_heap.build_max_heap(list_to_sort))
        seven_arity_heap.delete_max(seven_arity_heap.build_max_heap(list_to_sort))
