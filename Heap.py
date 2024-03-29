from auxiliary import generate_random_list


class NotInHeapError(Exception):
    pass


class NoParentFoundError(Exception):
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

        if idx == 0:
            for j in range(1, a + 1):
                children.append(j)
            return children

        for j in range(1, a + 1):
            children.append(a * idx + j)
        return children

    def heapify(self, array: list, idx: int) -> list:
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
            self.heapify(array, idx)

    @staticmethod
    def delete_max(array: list) -> None:
        """
        Function deletes the maximum element from the heap.
        Functions modifies heap through reference.

        :param array: The heap represented as a list.
        :return: None
        """
        size = len(array)
        if size <= 0:
            return

        last_element = array[size - 1]      # Ostatni element kopca
        size -= 1                       # Zmniejszamy size
        i = 0                           # Root
        j = 1                           # Lewy syn

        while j < size:                 # Idziemy w dół kopca
            if j + 1 < size and array[j + 1] > array[j]:    # Szukamy większego syna
                j += 1
            if last_element >= array[j]:    # Wyjdź z pętli jeśli warunek kopca spełniony
                break
            array[i] = array[j]         # Kopiuj większego syna do ojca
            i = j                       # Pozycja większego syna
            j = 2 * j + 1                  # Wskaźnik na lewego syna

        array[i] = last_element
        return array
