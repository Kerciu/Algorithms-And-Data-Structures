from typing import Callable, List, Any
from matplotlib import pyplot as plt
import gc
import time
import random


def generate_random_list() -> List[int]:
    # generate array of random elements
    unheapified_array = []
    for i in range(1, 1000000):
        unheapified_array.append(random.randint(1, 3000000))
    return unheapified_array


def process_algorithm_time(sorting_algorithm: Callable[[List[Any]],
                           None], array: list) -> float:
    # Disable garbage collector
    gc_old = gc.isenabled()
    gc.disable()

    # Compute time complexity
    start = time.process_time()
    sorting_algorithm(array)
    stop = time.process_time()

    if gc_old:
        gc.enable()

    return stop - start


def plotter():
    pass
