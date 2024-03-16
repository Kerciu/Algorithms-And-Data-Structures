from drawPlots import read_file_data, process_algorithm_time
from drawPlots import extract_info, draw_computional_complexity
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from selection_sort import selection_sort
from typing import List
import sys


def main() -> None:
    PATH = "pan-tadeusz-unix.txt"
    number_of_chars: List[int] = [2000, 4000, 6000, 8000, 10000]

    # Read time to compute
    bubble_time: List[float] = []
    selection_time: List[float] = []
    insertion_time: List[float] = []
    merge_time: List[float] = []
    quick_time: List[float] = []

    for elem in number_of_chars:
        data_list: List[str] = read_file_data(PATH, elem)

        # Extract computing time
        insertion_time.append(process_algorithm_time(insertion_sort, data_list))
        bubble_time.append(process_algorithm_time(bubble_sort, data_list))
        selection_time.append(process_algorithm_time(selection_sort, data_list))
        merge_time.append(process_algorithm_time(merge_sort, data_list))
        quick_time.append(process_algorithm_time(quick_sort, data_list))

    # Save info into dictionary
    bubble_info = extract_info(number_of_chars, bubble_time, "Bubble Sort")
    selection_info = extract_info(number_of_chars, selection_time, "Selection Sort")
    insertion_info = extract_info(number_of_chars, insertion_time, "Insertion Sort")
    merge_info = extract_info(number_of_chars, merge_time, "Merge Sort")
    quick_info = extract_info(number_of_chars, quick_time, "Quick Sort")

    # Draw n^2 computional complexity chart
    n2_list: List[dict] = [bubble_info, selection_info, insertion_info]
    draw_computional_complexity(n2_list, "n^2")

    # Draw nlogn computional complexity chart
    nlogn_list: List[dict] = [merge_info, quick_info]
    draw_computional_complexity(nlogn_list, "n*log(n)")

    sys.setrecursionlimit(1000)


if __name__ == "__main__":
    main()
