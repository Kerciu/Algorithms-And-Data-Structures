from typing import List, Tuple
from Heap import Heap
from auxiliary import generate_random_list, plotter, process_algorithm_time
from nodes import Node
import random


def generate_ranges() -> Tuple[List[List[int]], List[int]]:
    array: List[List[int]] = []
    ranges: List[int] = [1000 * i for i in range(1, 101)]
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

    array, ranges = generate_ranges()
    heapify_info = {}
    delete_info = {}
    add_info = {}
    for arity in (2, 5, 7):
        heap = Heap(arity)

        heapify_info[f"Arity of {arity}"] = extract_info(lambda x: heap.heapify(x, 0), array, ranges)

        delete_info[f"Arity of {arity}"] = extract_info(heap.delete_max, array, ranges)

        add_info[f"Arity of {arity}"] = extract_info(lambda x: heap.add_max(x, random.randint(500, 30000)), array, ranges)

    print(heapify_info)

    plotter(heapify_info, "Heapify")
    plotter(delete_info, "Delete-max")
    plotter(add_info, "Add-max")

    root = Node.build_tree_from_heap(heap.heapify(array, 0))
    print(Node.print_heap(root))


if __name__ == "__main__":
    main()
