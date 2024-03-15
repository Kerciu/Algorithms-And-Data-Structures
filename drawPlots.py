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


#TODO Create function that extracts data from results and
# saves it to the dictionary.
def draw_computional_complexity(size, sorting_time, info):
    # x axis: elements
    # y axis: computing time
    plt.plot(size, sorting_time, label=f"{info}")
    plt.xlabel("Size of Sorted Array")
    plt.ylabel("Time Needed to Compute")

    plt.title("Comparition Time Between Sorting Algorithms")
    plt.legend()

    plt.show()
