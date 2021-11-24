class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи
        self._next_index_to_fill = 0

    def MakeHeap(self, a, depth) -> None:
        self._next_index_to_fill = 0
        self.HeapArray = [None]*(2**(depth + 1) - 1)
        for x in a:
            self.Add(x)

    def GetMax(self):
        if len(self.HeapArray) == 0:
            return -1
        res = self.HeapArray[0]
        if res is None:
            return -1
        candidate_index = self._next_index_to_fill - 1
        if candidate_index == 0:
            self.HeapArray[0] = None
            self._next_index_to_fill = 0
            return res
        self._next_index_to_fill -= 1
        self.HeapArray[0] = self.HeapArray[self._next_index_to_fill]
        self.HeapArray[self._next_index_to_fill] = None
        # вернуть значение корня и перестроить кучу
        return res

    def Add(self, key) -> bool:
        index = self._next_index_to_fill
        if index >= len(self.HeapArray):
            return False
        self.HeapArray[index] = key
        self._next_index_to_fill += 1
        parent_index = self._parent_index(index)
        while parent_index >= 0:
            parent = self.HeapArray[parent_index]
            if parent > key:
                return True
            else:
                self.HeapArray[index] = parent
                self.HeapArray[parent_index] = key
            index = parent_index
            parent_index = self._parent_index(index)
        return True  # если куча вся заполнена

    def _parent_index(self, index: int) -> int:
        if (index - 1) < 0:
            return -1
        return int((index-1)/2)

    def _left_child_index(self, index: int) -> int:
        return int(2*index + 1)

    def _right_child_index(self, index: int) -> int:
        return int(2*index + 2)
