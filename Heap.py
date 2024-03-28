class Heap:
    def __init__(self, arity: int) -> None:
        self._arity = arity

    @property
    def get_arity(self) -> int:
        return self._arity

    @staticmethod
    def get_parent(idx: int) -> int:
        return idx // 2

    @staticmethod
    def get_children(idx: int) -> int:
        return 2 * idx, 2 * idx + 1

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
        left_child, right_child = self.get_children(idx)
        size = len(array)

        if (left_child < size) and (array[left_child] > array[largest]):
            largest = left_child
        if (right_child < size) and (array[right_child] > array[largest]):
            largest = right_child

        if largest != idx:
            # Zamiana miejscami
            array[idx], array[largest] = array[largest], array[idx]
            self.heapify(largest, idx)

    def build_heap(self) -> list:
        # generate array of random elements
        pass
