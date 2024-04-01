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


def plotter(x_value: List[int], y_value: List[float], process: str) -> None:
    plt.plot(x_value, y_value, label=f"{process.capitalize()}")
    plt.xlabel(f"Integers to {process}")
    plt.ylabel("Time to compute")

    plt.title(f"Computing time needed to {process}")
    plt.grid()

    plt.savefig(f"{process}.png")
    plt.show()
