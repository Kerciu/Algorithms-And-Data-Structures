from drawPlots import read_file_data, process_algorithm_time
from drawPlots import extract_info, draw_computional_complexity
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from selection_sort import selection_sort
import sys


def main():
    PATH = "pan-tadeusz-unix.txt"
    number_of_chars = [2000, 4000, 6000, 8000, 10000]
    # # Read time to compute
    # for i in range(0, len(number_of_chars)):
    bubble_time = []
    selection_time = []
    insertion_time = []
    merge_time = []
    quick_time = []
    for elem in number_of_chars:
        data_list = read_file_data(PATH, elem)
        bubble_time.append(process_algorithm_time(bubble_sort, data_list))
        selection_time.append(process_algorithm_time(selection_sort, data_list)) # noqa 501
        insertion_time.append(process_algorithm_time(insertion_sort, data_list)) # noqa 501
        merge_time.append(process_algorithm_time(merge_sort, data_list))
        quick_time.append(process_algorithm_time(quick_sort, data_list))
    bubble_info = extract_info(number_of_chars, bubble_time, "Bubble Sort")
    selection_info = extract_info(number_of_chars, selection_time, "Selection Sort") # noqa 501
    insertion_info = extract_info(number_of_chars, insertion_time, "Insertion Sort") # noqa 501
    merge_info = extract_info(number_of_chars, merge_time, "Merge Sort")
    quick_info = extract_info(number_of_chars, quick_time, "Quick Sort")
    n2_list = [bubble_info, selection_info, insertion_info]
    draw_computional_complexity(n2_list, "n^2")
    nlogn_list = [merge_info, quick_info]
    draw_computional_complexity(nlogn_list, "n*log(n)")
    sys.setrecursionlimit(1000)


if __name__ == "__main__":
    main()
