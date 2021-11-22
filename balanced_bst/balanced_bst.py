class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0


class BalancedBST:

    def __init__(self):
        self.Root = None

    def F(self, parent: BSTNode, arr) -> BSTNode:
        start = 0
        stop = len(arr)
        index = int((stop - start) / 2)
        n = BSTNode(key=arr[index], parent=parent)
        if parent is None:
            self.Root = n
        else:
            n.Parent = parent
        return n

    def GenerateTree(self, a):
        if len(a) == 0:
            return
        input_array = sorted(a)
        queue = [(self.F(None, input_array), input_array)]
        level = 0
        while len(queue) > 0:
            next_level = []
            for q in queue:
                parent, array = q
                parent.Level = level
                left, right = self._left_right_array(array)
                if len(left) > 0:
                    left_child = self.F(parent, left)
                    parent.LeftChild = left_child
                    next_level.append((left_child, left))
                if len(right) > 0:
                    right_child = self.F(parent, right)
                    parent.RightChild = right_child
                    next_level.append((right_child, right))
            queue = next_level
            level += 1

    def _left_right_array(self, arr):
        start = 0
        stop = len(arr)
        index = int((stop - start) / 2)
        left = arr[start: index]
        right = arr[index + 1:]
        return left, right


    # создаём дерево с нуля из неотсортированного массива a
    # ...

    def IsBalanced(self, root_node):
        return False  # сбалансировано ли дерево с корнем root_node
