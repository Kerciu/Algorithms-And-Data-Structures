from drawPlots import read_file_data, process_algorithm_time, extract_info, draw_computional_complexity
import bubble_sort, insertion_sort, merge_sort, quick_sort, selection_sort
import sys


PATH = "pan-tadeusz-unix.txt"


def main():
    number_of_chars = [1000, 2000, 5000, 7500, 10000]

    # # Read time to compute
    # for i in range(0, len(number_of_chars)):
    for elem in number_of_chars:
        data_list = read_file_data(PATH, elem)
        bubble_time = [process_algorithm_time(bubble_sort.bubble_sort(data_list))]
        selection_time = [process_algorithm_time(selection_sort.selection_sort(data_list))]
        insertion_time = [process_algorithm_time(insertion_sort.insertion_sort(data_list))]
        merge_time = [process_algorithm_time(merge_sort.merge_sort(data_list))]
        quick_time = [process_algorithm_time(quick_sort.quick_sort(data_list))]

    bub_info = extract_info(number_of_chars, bubble_time, "Bubble Sort")
    sel_info = extract_info(number_of_chars, selection_time, "Selection Sort")
    ins_info = extract_info(number_of_chars, insertion_time, "Insertion Sort")
    mer_info = extract_info(number_of_chars, merge_time, "Merge Sort")
    qui_info = extract_info(number_of_chars, quick_time, "Quick Sort")

    # TODO n^2 chart (bubble, selection, insertion)
    n2_list = [bub_info, sel_info, ins_info]
    draw_computional_complexity(n2_list)

    # TODO nlogn chart (merge, quick)
    nlogn_list = [mer_info, qui_info]
    draw_computional_complexity(nlogn_list)

    sys.setrecursionlimit(1000)
    pass


if __name__ == "__main__":
    main()
