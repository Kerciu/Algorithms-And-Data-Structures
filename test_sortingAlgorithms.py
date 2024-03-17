from drawPlots import read_file_data, extract_info, process_algorithm_time
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


def test_read_file_data():
    content = read_file_data("pan-tadeusz-unix.txt", 100)
    assert isinstance(content, list)
    assert len(content) > 0


def test_file_not_found():
    content = read_file_data("nonexistent_file.txt")
    assert content == []


def test_sorting_time():
    array = [5, 3, 8, 1, 2]
    time_taken = process_algorithm_time(insertion_sort, array)
    assert time_taken >= 0

    time_taken = process_algorithm_time(bubble_sort, array)
    assert time_taken >= 0

    time_taken = process_algorithm_time(selection_sort, array)
    assert time_taken >= 0

    time_taken = process_algorithm_time(merge_sort, array)
    assert time_taken >= 0

    time_taken = process_algorithm_time(quick_sort, array)
    assert time_taken >= 0


def test_sorting_time_empty_array():
    array = []
    time_taken = process_algorithm_time(insertion_sort, array)
    assert time_taken == 0

    time_taken = process_algorithm_time(bubble_sort, array)
    assert time_taken == 0

    time_taken = process_algorithm_time(selection_sort, array)
    assert time_taken == 0

    time_taken = process_algorithm_time(merge_sort, array)
    assert time_taken == 0

    time_taken = process_algorithm_time(quick_sort, array)
    assert time_taken == 0


def test_sorting_time_large_array():
    array = list(range(10000, 0, -1))
    time_taken = process_algorithm_time(insertion_sort, array)
    assert time_taken > 0

    time_taken = process_algorithm_time(bubble_sort, array)
    assert time_taken > 0

    time_taken = process_algorithm_time(selection_sort, array)
    assert time_taken > 0

    time_taken = process_algorithm_time(merge_sort, array)
    assert time_taken > 0

    time_taken = process_algorithm_time(quick_sort, array)
    assert time_taken > 0


def test_extract_info():
    size = [100, 200, 500, 1000, 1500]
    time = [0.05, 0.08, 0.1, 0.12, 0.14]
    info_string = "Quick Sort"
    result = extract_info(size, time, info_string)

    assert isinstance(result, dict)
    assert info_string in result
    assert isinstance(result[info_string], list)
    assert result[info_string][0] == size
    assert result[info_string][1] == time


def test_extract_info_empty():
    size = []
    time = []
    info_string = "Empty Test"
    result = extract_info(size, time, info_string)

    assert isinstance(result, dict)
    assert info_string in result
    assert isinstance(result[info_string], list)
    assert result[info_string][0] == size
    assert result[info_string][1] == time


def test_extract_info_single_value():
    size = [100]
    time = [0.05]
    info_string = "Single Value Test"
    result = extract_info(size, time, info_string)

    assert isinstance(result, dict)
    assert info_string in result
    assert isinstance(result[info_string], list)
    assert result[info_string][0] == size
    assert result[info_string][1] == time
