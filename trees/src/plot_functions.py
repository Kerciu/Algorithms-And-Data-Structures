from typing import Callable
from matplotlib import pyplot as plt
import gc
import time
import random
from BSTTree import BSTTree
from AVLTree import AvlTree


def generate_list(limit: int, amount: int) -> list[int]:
    # calculate list of "amount" numbers from numbers between 0 and limit
    random_list = []
    for i in range(0, amount):
        random_list.append(random.randint(1, limit))
    return random_list


def process_algorithm_time(algorithm: Callable) -> float:
    # Disable garbage collector
    gc_old = gc.isenabled()
    gc.disable()
    # Compute time complexity
    start = time.process_time()
    algorithm()
    stop = time.process_time()
    # enable garbage collector
    if gc_old:
        gc.enable()
    return stop - start


def make_operation_on_tree(numbers_list: list[int], operation: Callable):
    def func():
        for number in numbers_list:
            operation(number)
    return func


def count_average_time(numbers: list[float], tree, operation_name: str) -> float:
    # multiply float by multiplier to receive int
    multiplier = 1000000000000000000
    # number of times
    counter = 10
    average_time = 0
    for i in range(0, counter):
        copied_tree = tree.copy()
        operation = find_operation(copied_tree, operation_name)
        average_time += process_algorithm_time(make_operation_on_tree(numbers, operation)) * multiplier
    average_time = average_time / (counter * multiplier)
    return average_time


def find_operation(tree, operation_name: str) -> Callable:
    if operation_name == "insert":
        return tree.insert
    elif operation_name == "search":
        return tree.search
    elif operation_name == "delete":
        return tree.delete
    else:
        raise AttributeError("Invalid operation")


def create_time_list(n_list: list[list[float]], tree, operation_name: str) -> list[float]:
    # create list of times of processing the tree operation
    # operation is called for every randomly generated list number in n_list
    average_times_list = []
    for numbers_list in n_list:
        average_times_list.append(count_average_time(numbers_list, tree, operation_name))
    return average_times_list


def draw_plot(n_values: list[int], generated_list: list[int], title: str, bst_tree: BSTTree, avl_tree: AvlTree, operation_name: str):
    n_list = []
    for n in n_values:
        n_list.append(generated_list[:n])
    bst_times = create_time_list(n_list, bst_tree, operation_name)
    avl_times = create_time_list(n_list, avl_tree, operation_name)
    plt.plot(n_values, bst_times, "o-", markersize=5, label="BST Tree")
    plt.plot(n_values, avl_times, "o-", markersize=5, label="AVL Tree")
    plt.xlabel("Size of Array")
    plt.ylabel("Time Needed to Compute")
    plt.xticks(rotation=30, fontsize="small")
    plt.yticks(rotation=30, fontsize="small")
    plt.title(label=title)
    plt.legend()
    plt.savefig(f"{title}.png")
    plt.show()


def draw_plot_deletion(n_values: list[int], generated_list: list[int], title: str, bst_tree: BSTTree):
    n_list = []
    for n in n_values:
        n_list.append(generated_list[:n])
    bst_times = create_time_list(n_list, bst_tree, "delete")
    plt.plot(n_values, bst_times, "o-", markersize=5, label="BST Tree")
    plt.xlabel("Size of Array")
    plt.ylabel("Time Needed to Compute")
    plt.xticks(rotation=30, fontsize="small")
    plt.yticks(rotation=30, fontsize="small")
    plt.title(label=title)
    plt.legend()
    plt.savefig(f"{title}.png")
    plt.show()


def create_full_bst_tree(n: int) -> BSTTree:
    bst_tree = BSTTree()
    numbers_list = generate_list(30000, n)
    for number in numbers_list:
        bst_tree.insert(number)
    return bst_tree


def create_full_avl_tree(n: int) -> AvlTree:
    avl_tree = AvlTree()
    numbers_list = generate_list(30000, n)
    for number in numbers_list:
        avl_tree.insert(number)
    return avl_tree
