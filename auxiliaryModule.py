from typing import Callable
from matplotlib import pyplot as plt
import gc
import time
import random


def generate_list():
    random_list = []
    for i in range(0, 10000):
        random_list.append(random.randint(1, 30000))

    return random_list


def process_algorithm_time(algorithm: Callable) -> float:
    # Disable garbage collector
    gc_old = gc.isenabled()
    gc.disable()

    # Compute time complexity
    start = time.process_time()
    result = algorithm()
    stop = time.process_time()

    if gc_old:
        gc.enable()

    return stop - start


def draw_computional_complexity(list_of_data: list, title: str, plots=1) -> None:
    if plots == 1:
        times_list = []
        elements_list = []
        for tuples in list_of_data:
            elements_list.append(tuples[0])
            times_list.append(tuples[1])
        plt.plot(elements_list, times_list, "o-", markersize=5)
    if plots == 2:
        bst_elements_list = []
        bst_times_list = []
        avl_elements_list = []
        avl_times_list = []
        for bst_avl in list_of_data:
            bst_elements_list.append(bst_avl[0][0])
            bst_times_list.append(bst_avl[0][1])
            avl_elements_list.append(bst_avl[1][0])
            avl_times_list.append(bst_avl[1][1])
        
        plt.plot(bst_elements_list, bst_times_list, "o-", markersize=5, label="BST Tree")
        plt.plot(avl_elements_list, avl_times_list, "o-", markersize=5, label="AVL Tree")
    plt.xlabel("Size of Array")
    plt.ylabel("Time Needed to Compute")
    plt.xticks(rotation=30, fontsize="small")
    plt.yticks(rotation=30, fontsize="small")
    plt.title(label=title)
    plt.legend()
    plt.savefig(f"{title}.png")
    plt.show()
