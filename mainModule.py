from typing import List, Tuple
from Heap import Heap
from auxiliary import generate_random_list, plotter, process_algorithm_time
from nodes import Node
import random


def generate_ranges() -> Tuple[List[List[int]], List[int]]:
    array: List[List[int]] = []
    ranges: List[int] = [10000 * i for i in range(1, 11)]
    for value in ranges:
        array.append(generate_random_list()[:value])

    return array, ranges


def extract_info(process, array, ranges, *args, **kwargs) -> List[List[int]]:

    time_values: List[int] = []

    for arr in array:
        time_value = process_algorithm_time(process, arr, *args, **kwargs)
        time_values.append(time_value)

    return [ranges, time_values]


def main() -> None:
    heap = Heap(2)
    array, ranges = generate_ranges()

    heapify_info = extract_info(lambda x: heap.heapify(x, 0), array, ranges)
    plotter(heapify_info[0], heapify_info[1], "heapify")
    delete_info = extract_info(heap.delete_max, array, ranges)
    plotter(delete_info[0], delete_info[1], "delete max key")
    add_info = extract_info(lambda x: heap.add_max(x, random.randint(500, 30000)), array, ranges)
    plotter(add_info[0], add_info[1], "add max key")

    root = Node.build_tree_from_heap(heap.heapify(array, 0))
    print(Node.print_heap(root))


if __name__ == "__main__":
    main()
