from matplotlib import pyplot as plt
from typing import Callable, List, Any
import time
import gc


# Return list of words from txt file
def read_file_data(path: str, size_to_read=None) -> list:
    try:
        special_characters = "!@#$%^&*()_+-=\\|]}[{\"\";:/?.>,<\'–—»«…"

        with open(path, 'r', encoding="utf-8") as file:
            if size_to_read:
                content = file.read(size_to_read)
            else:
                content = file.read()
            for char in special_characters:
                content = content.replace(char, ' ')
            content = content.replace('\n', ' ')

        return content.split()

    except FileNotFoundError:
        return []


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


def extract_info(size: List[int], time: List[float], info_string: str) -> dict:
    return {info_string: [size, time]}


# Takes in list of dictionaries
# As an example: [{"Bubble Sort": [size, time]}, {"Merge Sort": ..]
def draw_computional_complexity(list_of_data: list, complexity: str) -> None:
    for sort_dict in list_of_data:
        for key, value in sort_dict.items():
            # value[0] == size , value[1] == sorting_time
            sizes = value[0]
            times = value[1]
            plt.plot(sizes, times, "o-", label=key, markersize=5)
    plt.xlabel("Size of Sorted Array")
    plt.ylabel("Time Needed to Compute")
    plt.xticks(rotation=30, fontsize="small")
    plt.yticks(rotation=30, fontsize="small")
    title = complexity + " Algorithms sorting time comparison"
    plt.title(label=title)
    plt.legend()
    if complexity == "n^2":
        plt.savefig("n2.png")
    else:
        plt.savefig("nlogn.png")
    plt.show()
