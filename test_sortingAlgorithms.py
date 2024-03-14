from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort, merge
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


def test_bubble_sort1():
    sorter = bubble_sort(unsorted_list1)
    assert sorter == sorted_list1


def test_selection_sort1():
    sorter = selection_sort(unsorted_list1)
    assert sorter == sorted_list1


def test_insertion_sort1():
    sorter = insertion_sort(unsorted_list1)
    assert sorter == sorted_list1


def test_merge_sort1():
    sorter = merge_sort(unsorted_list1)
    assert sorter == sorted_list1


def test_quick_sort1():
    sorter = quick_sort(unsorted_list1)
    assert sorter == sorted_list1


def test_bubble_sort2():
    sorter = bubble_sort(unsorted_list2)
    assert sorter == sorted_list2


def test_selection_sort2():
    sorter = selection_sort(unsorted_list2)
    assert sorter == sorted_list2


def test_insertion_sort2():
    sorter = insertion_sort(unsorted_list2)
    assert sorter == sorted_list2


def test_merge_sort2():
    sorter = merge_sort(unsorted_list2)
    assert sorter == sorted_list2


def test_quick_sort2():
    sorter = quick_sort(unsorted_list2)
    assert sorter == sorted_list2


def test_bubble_sort3():
    sorter = bubble_sort(unsorted_list3)
    assert sorter == sorted_list3


def test_selection_sort3():
    sorter = selection_sort(unsorted_list3)
    assert sorter == sorted_list3


def test_insertion_sort3():
    sorter = insertion_sort(unsorted_list3)
    assert sorter == sorted_list3


def test_merge_sort3():
    sorter = merge_sort(unsorted_list3)
    assert sorter == sorted_list3


def test_quick_sort3():
    sorter = quick_sort(unsorted_list3)
    assert sorter == sorted_list3


def test_bubble_sort4():
    sorter = bubble_sort(unsorted_list4)
    assert sorter == sorted_list4


def test_selection_sort4():
    sorter = selection_sort(unsorted_list4)
    assert sorter == sorted_list4


def test_insertion_sort4():
    sorter = insertion_sort(unsorted_list4)
    assert sorter == sorted_list4


def test_merge_sort4():
    sorter = merge_sort(unsorted_list4)
    assert sorter == sorted_list4


def test_quick_sort4():
    sorter = quick_sort(unsorted_list4)
    assert sorter == sorted_list4


def test_bubble_sort5():
    sorter = bubble_sort(unsorted_list5)
    assert sorter == sorted_list5


def test_selection_sort5():
    sorter = selection_sort(unsorted_list5)
    assert sorter == sorted_list5


def test_insertion_sort5():
    sorter = insertion_sort(unsorted_list5)
    assert sorter == sorted_list5


def test_merge_sort5():
    sorter = merge_sort(unsorted_list5)
    assert sorter == sorted_list5


def test_quick_sort5():
    sorter = quick_sort(unsorted_list5)
    assert sorter == sorted_list5


def test_bubble_sort6():
    sorter = bubble_sort(unsorted_list6)
    assert sorter == sorted_list6


def test_selection_sort6():
    sorter = selection_sort(unsorted_list6)
    assert sorter == sorted_list6


def test_insertion_sort6():
    sorter = insertion_sort(unsorted_list6)
    assert sorter == sorted_list6


def test_merge_sort6():
    sorter = merge_sort(unsorted_list6)
    assert sorter == sorted_list6


def test_quick_sort6():
    sorter = quick_sort(unsorted_list6)
    assert sorter == sorted_list6


def test_empty_list_bubble_sort():
    assert bubble_sort([]) == []


def test_empty_list_selection_sort():
    assert selection_sort([]) == []


def test_empty_list_instertion_sort():
    assert insertion_sort([]) == []


def test_empty_list_merge_sort():
    assert merge_sort([]) == []


def test_empty_list_quick_sort():
    assert quick_sort([]) == []
