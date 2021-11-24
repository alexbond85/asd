class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи
        self._next_index_to_fill = 0

    def MakeHeap(self, a, depth) -> None:
        self._next_index_to_fill = 0
        self.HeapArray = [None]*(2**(depth + 1) - 1)
        for x in a:
            self.Add(x)

    def _max(self, left_child, right_child):
        if left_child is None:
            return right_child
        if right_child is None:
            return left_child
        if left_child > right_child:
            return left_child
        return right_child

    def GetMax(self):
        if len(self.HeapArray) == 0:
            return -1
        root = self.HeapArray[0]
        if root is None:
            return -1
        if self._next_index_to_fill == 1:
            self.HeapArray[0] = None
            self._next_index_to_fill = 0
            return root
        # move to root
        self._next_index_to_fill -= 1
        self.HeapArray[0] = self.HeapArray[self._next_index_to_fill]
        self.HeapArray[self._next_index_to_fill] = None
        #
        current_index = 0

        while True:
            current_key = self.HeapArray[current_index]
            left_child_index = self._left_child_index(current_index)
            right_child_index = self._right_child_index(current_index)
            left_child = self.HeapArray[left_child_index] if left_child_index < len(self.HeapArray) else None
            right_child = self.HeapArray[right_child_index] if right_child_index < len(self.HeapArray) else None
            is_max_right = self._max(right_child, current_key) > current_key
            is_max_left = self._max(left_child, current_key) > current_key
            if is_max_left or is_max_right:
                if self._max(right_child, left_child) == right_child:
                    self.HeapArray[current_index] = right_child
                    self.HeapArray[self._right_child_index(current_index)] = current_key
                    current_index = self._right_child_index(current_index)
                if self._max(right_child, left_child) == left_child:
                    self.HeapArray[current_index] = left_child
                    self.HeapArray[self._left_child_index(current_index)] = current_key
                    current_index = self._left_child_index(current_index)
            else:
                return root

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
