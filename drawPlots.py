from matplotlib import pyplot as plt
import time
import gc


# Use this as proccess_algorithm_time()[0]
def process_algorithm_time(sorting_algorithm, arr):
    # Disable garbage collector
    gc_old = gc.isenabled()
    gc.disable()

    # Compute time complexity
    start = time.process_time()
    sorting_algorithm(arr)
    stop = time.process_time()

    if gc_old:
        gc.enable()

    return stop - start


def extract_info(size, time, info_string):
    return {info_string: [size, time]}


# Takes in list of dictionaries
# As an example: [{"Bubble Sort": [size, time]}, {"Merge Sort": ..]
def draw_computional_complexity(list_of_data: list):

    for data in list_of_data:
        for key, value in data.items():
            # value[0] == size , value[1] == sorting_time
            sizes = [entry[0] for entry in value]
            times = [entry[1] for entry in value]
            plt.plot(sizes, times, label=key)

    plt.xlabel("Size of Sorted Array")
    plt.ylabel("Time Needed to Compute")

    plt.title("Comparition Time Between Sorting Algorithms")
    plt.legend()

    plt.show()
