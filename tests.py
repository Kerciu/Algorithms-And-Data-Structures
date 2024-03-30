from Heap import Heap, NotInHeapError
import pytest


def test_Heap_get_arity():
    two_arity_heap = Heap(2)
    assert two_arity_heap.get_arity() == 2


def test_Heap_set_arity():
    heap = Heap(2)
    heap.set_arity(5)
    assert heap.get_arity() == 5


def test_get_parent():
    i = 9
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert two_arity_heap.get_parent(i) == 4
    assert five_arity_heap.get_parent(i) == 2
    assert seven_arity_heap.get_parent(i) == 2


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
    with pytest.raises(NotInHeapError) as e:
        two_arity_heap.get_parent(i) == 4
        five_arity_heap.get_parent(i) == 2
        seven_arity_heap.get_parent(i) == 2


def test_Heap_sort_empty():
    list_to_sort = []
    result = []
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert result == two_arity_heap.heapify(list_to_sort, 0)
    assert result == five_arity_heap.heapify(list_to_sort, 0)
    assert result == seven_arity_heap.heapify(list_to_sort, 0)


def test_Heap_sort_one_argument():
    list_to_sort = [2]
    result = [2]
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert result == two_arity_heap.heapify(list_to_sort, 0)
    assert result == five_arity_heap.heapify(list_to_sort, 0)
    assert result == seven_arity_heap.heapify(list_to_sort, 0)


def test_Heap_sort_many_arguments():
    list_to_sort = [2, 5, 1, 3, 0, 8, 9, 6, 7, 4]
    result = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert result == two_arity_heap.heapify(list_to_sort, 0)
    assert result == five_arity_heap.heapify(list_to_sort, 0)
    assert result == seven_arity_heap.heapify(list_to_sort, 0)


def test_Heap_sort_many_arguments_same():
    list_to_sort = [2, 5, 2, 3, 0, 2, 9, 2, 7, 4]
    result = [9, 7, 5, 4, 3, 2, 2, 2, 2, 0]
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert result == two_arity_heap.heapify(list_to_sort, 0)
    assert result == five_arity_heap.heapify(list_to_sort, 0)
    assert result == seven_arity_heap.heapify(list_to_sort, 0)


def test_add_element_to_empty_heap():
    list_to_sort = []
    element_to_add = 43
    result = [43]
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert result == two_arity_heap.add_element(list_to_sort, element_to_add)
    assert result == five_arity_heap.add_element(list_to_sort, element_to_add)
    assert result == seven_arity_heap.add_element(list_to_sort, element_to_add)


def test_add_element():
    list_to_sort = [2, 5, 1, 3, 0, 8, 9, 6, 7, 4]
    element_to_add = 43
    result = [43, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert result == two_arity_heap.add_element(list_to_sort, element_to_add)
    assert result == five_arity_heap.add_element(list_to_sort, element_to_add)
    assert result == seven_arity_heap.add_element(list_to_sort, element_to_add)


def test_add_element_not_root():
    list_to_sort = [2, 53, 1, 3, 0, 8, 9, 6, 7, 4]
    element_to_add = 5
    result = [53, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert result == two_arity_heap.add_element(list_to_sort, element_to_add)
    assert result == five_arity_heap.add_element(list_to_sort, element_to_add)
    assert result == seven_arity_heap.add_element(list_to_sort, element_to_add)


def test_remove_element_from_the_list():
    list_to_sort = [2, 53, 1, 3, 0, 8, 9, 6, 7, 5, 4]
    element_to_remove = 5
    result = [53, 9, 8, 7, 6, 4, 3, 2, 1, 0]
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert result == two_arity_heap.remove_element(list_to_sort, element_to_remove)
    assert result == five_arity_heap.remove_element(list_to_sort, element_to_remove)
    assert result == seven_arity_heap.remove_element(list_to_sort, element_to_remove)


def test_remove_element_multiple_from_the_list():
    list_to_sort = [2, 53, 1, 0, 0, 0, 9, 6, 7, 5, 4]
    element_to_remove = 5
    result = [53, 9, 7, 6, 5, 4, 2, 1, 0, 0]
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    assert result == two_arity_heap.remove_element(list_to_sort, element_to_remove)
    assert result == five_arity_heap.remove_element(list_to_sort, element_to_remove)
    assert result == seven_arity_heap.remove_element(list_to_sort, element_to_remove)


def test_remove_element_not_in_list():
    list_to_sort = [2, 53, 1, 0, 0, 0, 9, 6, 7, 5, 4]
    element_to_remove = 10
    two_arity_heap = Heap(2)
    five_arity_heap = Heap(5)
    seven_arity_heap = Heap(7)
    with pytest.raises(NotInHeapError) as e:
        two_arity_heap.remove_element(list_to_sort, element_to_remove)
        five_arity_heap.remove_element(list_to_sort, element_to_remove)
        seven_arity_heap.remove_element(list_to_sort, element_to_remove)
