class aBST:

    def __init__(self, depth):
        depth = depth + 1
        tree_size = 2**depth - 1
        self.Tree = [None] * tree_size

    def _parent_index(self, index: int) -> int:
        return int((index-1)/2)

    def _left_child_index(self, index: int) -> int:
        return int(2*index + 1)

    def _right_child_index(self, index: int) -> int:
        return int(2*index + 2)

    def FindKeyIndex(self, key):
        index = 0
        while index <= len(self.Tree):
            if self.Tree[index] is None:
                return -index
            elif self.Tree[index] == key:
                return index
            elif self.Tree[index] < key:
                index = self._right_child_index(index)
            else:
                index = self._left_child_index(index)
        return None

    def AddKey(self, key):
        index = self.FindKeyIndex(key)
        if index is None:
            return -1
        if index <= 0:
            self.Tree[-index] = key
            return -index
