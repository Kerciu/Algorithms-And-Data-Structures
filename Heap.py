class NotInHeapError(Exception):
    pass


class NoParentFoundError(Exception):
    pass


class EmptyHeapError(Exception):
    pass


class Heap:
    def __init__(self, arity: int) -> None:
        self._arity = arity

    @property
    def get_arity(self) -> int:
        return self._arity

    def get_parent(self, idx: int) -> int:
        if idx == 0:
            raise NoParentFoundError
        return idx // self._arity

    def get_children(self, idx: int) -> list:
        a = self._arity
        children = []
        for j in range(1, a + 1):
            children.append(a * idx + j)
        return children

    def heapify(self, array: list, idx: int):
        # largest := a
        # jeśli 2a <= size  oraz H[2a] > H[largest], to
        # largest := 2a;
        # jeśli 2a + 1 <= size oraz H[2a + 1] > H[largest], to
        # largest := 2a + 1;
        # jeśli largest != a, to
        # zamień miejscami H[largest] oraz H[a]
        # wywołaj rekurencyjnie Heapify(largest)
        largest = idx
        children_indecies = self.get_children(idx)
        size = len(array)

        for child_idx in children_indecies:

            if (child_idx < size) and (array[child_idx] > array[largest]):
                largest = child_idx

        if largest != idx:
            # Zamiana miejscami
            array[idx], array[largest] = array[largest], array[idx]
            self.heapify(array, largest)

    def build_max_heap(self, array: list) -> list:
        array = array.copy()
        heap_size = len(array)
        # Zaczynamy od ostatniego węzła, który ma dzieci
        for i in range((heap_size // 2) - 1, -1, -1):
            self.heapify(array, i)
        return array

    def delete_max(self, array: list) -> list:
        """
        Function deletes the maximum element from the heap.
        Functions modifies heap through reference.

        :param array: The heap represented as a list.
        :return: None
        """
        size = len(array)
        if size <= 0:
            raise EmptyHeapError

        last_element = array[size - 1]      # Ostatni element kopca
        size -= 1                       # Zmniejszamy size
        i = 0                           # Root
        j = 1                           # Lewy syn

        # Idziemy w dół kopca
        while j < size:
            # Szukamy większego syna
            if j + 1 < size and array[j + 1] > array[j]:
                j += 1

            if last_element >= array[j]:
                # Wyjdź z pętli jeśli warunek kopca spełniony
                break

            array[i] = array[j]         # Kopiuj większego syna do ojca
            i = j                       # Pozycja większego syna
            j = 2 * j + 1                  # Wskaźnik na lewego syna

        array[i] = last_element
        return array

    def add_max(self, array: list, new_element: int) -> list:
        array = array.copy()
        array.append(new_element)
        return self.build_max_heap(array)


heap = Heap(6)
unsorted_list = [2, 53, 1, 3, 0, 8, 9, 6, 7, 5, 4]
list = heap.build_max_heap(unsorted_list)
print(heap.delete_max(list))
