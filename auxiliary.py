from typing import List
from matplotlib import pyplot as plt
import random


def generate_random_list() -> List[int]:
    # generate array of random elements
    unheapified_array = []
    for i in range(1, 1000000):
        unheapified_array.append(random.randint(1, 3000000))
    return unheapified_array


def plotter(x_value, y_value, process):
    plt.plot(x_value, y_value, label=f"{process.capitalize()}")
    plt.xlabel(f"Integers to {process}")
    plt.ylabel("Time to compute")

    plt.title(f"Computing time needed to {process}")
    plt.grid()

    plt.savefig(f"{process}.png")
    plt.show()
