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

    def _children(self, n: BSTNode):
        res = []
        if n.LeftChild is not None:
            res.append(n.LeftChild)
        if n.RightChild is not None:
            res.append(n.RightChild)
        return res

    def _all_nodes(self, node: BSTNode):
        if node is None:
            return []
        else:
            nodes = [node]
            nodes_children = self._children(node)
            while len(nodes_children) > 0:
                nodes += nodes_children
                all_children = []
                for n in nodes_children:
                    all_children += self._children(n)
                nodes_children = all_children
            return nodes

    def _max_depth(self, start_from: BSTNode):
        if start_from is None:
            return 0
        all_nodes = self._all_nodes(start_from)
        levels = [n.Level for n in all_nodes]
        if len(levels) > 0:
            return max(levels) + 1 - start_from.Level
        return 1

    def IsBalanced(self, root_node: BSTNode):
        if root_node is None:
            return True
        left_max_depth = self._max_depth(root_node.LeftChild)
        right_max_depth = self._max_depth(root_node.RightChild)
        if abs(left_max_depth - right_max_depth) <= 1:
            return True
        else:
            return False
