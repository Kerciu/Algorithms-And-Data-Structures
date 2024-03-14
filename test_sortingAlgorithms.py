from heapq import merge
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

sorted_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_bubble_sort():
    unsorted_list = [5, 4, 0, 2, 7, 3, 9, 8, 1, 6]
    sorter = bubble_sort(unsorted_list)
    assert sorter == sorted_list

def test_selection_sort():
    unsorted_list = [5, 4, 0, 2, 7, 3, 9, 8, 1, 6]
    sorter = selection_sort(unsorted_list)
    assert sorter == sorted_list

def test_insertion_sort():
    unsorted_list = [5, 4, 0, 2, 7, 3, 9, 8, 1, 6]
    sorter = insertion_sort(unsorted_list)
    assert sorter == sorted_list

def test_merge_sort():
    unsorted_list = [5, 4, 0, 2, 7, 3, 9, 8, 1, 6]
    sorter = merge_sort(unsorted_list)
    assert sorter == sorted_list

def test_quick_sort():
    unsorted_list = [5, 4, 0, 2, 7, 3, 9, 8, 1, 6]
    sorter = quick_sort(unsorted_list)
    assert sorter == sorted_list

def test_empty_list():
    empty_list = []
    assert bubble_sort(empty_list) == []
    assert selection_sort(empty_list) == []
    assert insertion_sort(empty_list) == []
    assert merge_sort(empty_list) == []
    assert quick_sort(empty_list) == []