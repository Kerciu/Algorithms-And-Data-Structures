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
                children.append[j]
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
