from typing import List
from matplotlib import pyplot as plt
import random
import time
import gc


def generate_random_list() -> List[int]:
    # generate array of random elements
    unheapified_array: List[int] = []
    for i in range(1, 1000000):
        unheapified_array.append(random.randint(1, 3000000))
    return unheapified_array


def process_algorithm_time(process, *args, **kwargs) -> float:
    gc_old: bool = gc.isenabled()
    gc.disable()

    # Compute time complexity
    start: float = time.process_time()
    process(*args, **kwargs)
    stop: float = time.process_time()

    if gc_old:
        gc.enable()

    return stop - start


def plotter(data: dict, process: str) -> None:
    plt.figure()

    for arity, (x, y) in data.items():
        plt.plot(x, y, label=arity)

    plt.legend()

    plt.title(f'Computing time for {process} function')
    plt.xlabel('Number of integers processed')
    plt.ylabel('Time')

    plt.show()
