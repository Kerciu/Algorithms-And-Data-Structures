from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

unsorted_list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
unsorted_list2 = [-2, 3, -5, 6, 7, 9]
unsorted_list3 = [4, 3, 12, 3, 4, 7]
unsorted_list4 = ["adssf", "bsffsfs", "csddsw"]
unsorted_list5 = ["jablko", "banan", "gruszka", "brzoskwnia", "arbuz"]
unsorted_list6 = ["ford", "honda,", "audi", "jeep", "nissan."]

sorted_list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sorted_list2 = [-5, -2, 3, 6, 7, 9]
sorted_list3 = [3, 3, 4, 4, 7, 12]
sorted_list4 = ["adssf", "bsffsfs", "csddsw"]
sorted_list5 = ["arbuz", "banan", "brzoskwnia", "gruszka", "jablko"]
sorted_list6 = ["audi", "ford", "honda,", "jeep", "nissan."]


def test_bubble_sort_string():
    assert bubble_sort(unsorted_list1) == sorted_list1
    assert bubble_sort(unsorted_list2) == sorted_list2
    assert bubble_sort(unsorted_list3) == sorted_list3
    assert bubble_sort(unsorted_list4) == sorted_list4
    assert bubble_sort(unsorted_list5) == sorted_list5
    assert bubble_sort(unsorted_list6) == sorted_list6
    assert bubble_sort([]) == []


def test_selection_sort_string():
    assert selection_sort(unsorted_list1) == sorted_list1
    assert selection_sort(unsorted_list2) == sorted_list2
    assert selection_sort(unsorted_list3) == sorted_list3
    assert selection_sort(unsorted_list4) == sorted_list4
    assert selection_sort(unsorted_list5) == sorted_list5
    assert selection_sort(unsorted_list6) == sorted_list6
    assert selection_sort([]) == []


def test_merge_sort_string():
    assert merge_sort(unsorted_list1) == sorted_list1
    assert merge_sort(unsorted_list2) == sorted_list2
    assert merge_sort(unsorted_list3) == sorted_list3
    assert merge_sort(unsorted_list4) == sorted_list4
    assert merge_sort(unsorted_list5) == sorted_list5
    assert merge_sort(unsorted_list6) == sorted_list6
    assert merge_sort([]) == []


def test_insertion_sort_string():
    assert insertion_sort(unsorted_list1) == sorted_list1
    assert insertion_sort(unsorted_list2) == sorted_list2
    assert insertion_sort(unsorted_list3) == sorted_list3
    assert insertion_sort(unsorted_list4) == sorted_list4
    assert insertion_sort(unsorted_list5) == sorted_list5
    assert insertion_sort(unsorted_list6) == sorted_list6
    assert insertion_sort([]) == []


def test_quick_sort_string():
    assert quick_sort(unsorted_list1) == sorted_list1
    assert quick_sort(unsorted_list2) == sorted_list2
    assert quick_sort(unsorted_list3) == sorted_list3
    assert quick_sort(unsorted_list4) == sorted_list4
    assert quick_sort(unsorted_list5) == sorted_list5
    assert quick_sort(unsorted_list6) == sorted_list6
    assert quick_sort([]) == []
