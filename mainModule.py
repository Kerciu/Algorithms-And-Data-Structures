from typing import List
from Heap import Heap
from auxiliary import generate_random_list, plotter
from nodes import Node
import gc
import time


def extract_info(arity: int) -> List[List[int]]:
    heap = Heap(arity)

    array = []
    time_values = []
    ranges = [10000 * i for i in range(1, 11)]      # 10 ranges
    for value in ranges:
        array.append(generate_random_list()[:value])
    for arr in array:
        # Disable garbage collector
        gc_old = gc.isenabled()
        gc.disable()

        # Compute time complexity
        start = time.process_time()
        heap.heapify(arr, 0)
        stop = time.process_time()

        if gc_old:
            gc.enable()

        time_value = stop - start

        time_values.append(time_value)

    return [ranges, time_values]


def main():
    info = extract_info(2)
    plotter(info[0], info[1], "heapify")


if __name__ == "__main__":
    main()
