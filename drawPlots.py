from matplotlib import pyplot as plt
import time
import gc


# Use this as proccess_algorithm_time()[0]
def process_algorithm_time(function):
    # Disable garbage collector
    gc_old = gc.isenabled()
    gc.disable()

    # Compute time complexity
    start = time.process_time()
    result = function()
    stop = time.process_time()

    if gc_old:
        gc.enable()

    return stop - start, result


def draw_computional_complexity(data):
    pass