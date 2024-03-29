from Heap import Heap
from auxiliary import generate_random_list, process_algorithm_time, plotter
from nodes import Node


def main():
    heap = Heap(2)
    array = generate_random_list()[:30]  # Przykładowa lista 30 liczb
    heap.heapify(array, 0)
    root = Node.build_tree_from_heap(array)
    Node.print_heap(root)


if __name__ == "__main__":
    main()
    print("\n-------------------")
    print("Hit any key to exit ")
    x = input()
    print("-------------------")
    if x:
        print("Exiting the Program.")
        print("--------------------\n")
        exit()
