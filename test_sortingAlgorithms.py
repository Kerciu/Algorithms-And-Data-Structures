from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort, merge
from quick_sort import quick_sort
from drawPlots import process_algorithm_time, extract_info

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


def test_bubble_sort():
    sorter = bubble_sort(unsorted_list1)
    assert sorter == sorted_list1


def test_selection_sort():
    sorter = selection_sort(unsorted_list1)
    assert sorter == sorted_list1


def test_insertion_sort():
    sorter = insertion_sort(unsorted_list1)
    assert sorter == sorted_list1


def test_merge_sort():
    sorter = merge_sort(unsorted_list1)
    assert sorter == sorted_list1


def test_quick_sort():
    sorter = quick_sort(unsorted_list1)
    assert sorter == sorted_list1


def test_bubble_sort_negative():
    sorter = bubble_sort(unsorted_list2)
    assert sorter == sorted_list2


def test_selection_sort_negative():
    sorter = selection_sort(unsorted_list2)
    assert sorter == sorted_list2


def test_insertion_sort_negative():
    sorter = insertion_sort(unsorted_list2)
    assert sorter == sorted_list2


def test_merge_sort_negative():
    sorter = merge_sort(unsorted_list2)
    assert sorter == sorted_list2


def test_quick_sort_negative():
    sorter = quick_sort(unsorted_list2)
    assert sorter == sorted_list2


def test_bubble_sort_string():
    sorter1 = bubble_sort(unsorted_list3)
    sorter2 = bubble_sort(unsorted_list4)
    sorter3 = bubble_sort(unsorted_list5)
    assert sorter1 == sorted_list3
    assert sorter2 == sorted_list4
    assert sorter3 == sorted_list5


def test_selection_sort_string():
    sorter1 = selection_sort(unsorted_list3)
    sorter2 = selection_sort(unsorted_list4)
    sorter3 = selection_sort(unsorted_list5)
    assert sorter1 == sorted_list3
    assert sorter2 == sorted_list4
    assert sorter3 == sorted_list5


def test_merge_sort_string():
    sorter1 = merge_sort(unsorted_list3)
    sorter2 = merge_sort(unsorted_list4)
    sorter3 = merge_sort(unsorted_list5)
    assert sorter1 == sorted_list3
    assert sorter2 == sorted_list4
    assert sorter3 == sorted_list5


def test_insertion_sort_string():
    sorter1 = insertion_sort(unsorted_list3)
    sorter2 = insertion_sort(unsorted_list4)
    sorter3 = insertion_sort(unsorted_list5)
    assert sorter1 == sorted_list3
    assert sorter2 == sorted_list4
    assert sorter3 == sorted_list5


def test_quick_sort_string():
    sorter1 = quick_sort(unsorted_list3)
    sorter2 = quick_sort(unsorted_list4)
    sorter3 = quick_sort(unsorted_list5)
    assert sorter1 == sorted_list3
    assert sorter2 == sorted_list4
    assert sorter3 == sorted_list5


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


def test_bubble_sort_time():
    time_taken = process_algorithm_time(bubble_sort, [5, 4, 3, 2, 1])
    assert time_taken >= 0


def test_selection_sort_time():
    time_taken = process_algorithm_time(selection_sort, [5, 4, 3, 2, 1])
    assert time_taken >= 0


def test_insertion_sort_time():
    time_taken = process_algorithm_time(insertion_sort, [5, 4, 3, 2, 1])
    assert time_taken >= 0


def test_merge_sort_time():
    time_taken = process_algorithm_time(merge_sort, [5, 4, 3, 2, 1])
    assert time_taken >= 0


def test_quick_sort_time():
    time_taken = process_algorithm_time(quick_sort, [5, 4, 3, 2, 1])
    assert time_taken >= 0


def test_empty_list_time():
    time_taken = process_algorithm_time(bubble_sort, [])
    assert time_taken >= 0
