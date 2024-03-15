import bubble_sort, insertion_sort, merge_sort, quick_sort, selection_sort
import sys


PATH = "pan-tadeusz-unix.txt"


def main():
    sys.setrecursionlimit(1000)
    pass


def read_from_file(path):
    with open(path) as file_handle:
        list_of_words = []
        for line in file_handle:
            line.rstrip()
            line.rstrip("\n")
            line = line.split(" ")
            forbidden_signs = ["", "-", "\n", "-----\n"]
            for word in line:
                if word not in forbidden_signs:
                    list_of_words.append(word)
    return list_of_words


if __name__ == "__main__":
    main()
