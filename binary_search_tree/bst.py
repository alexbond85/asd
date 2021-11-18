class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey: int = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey: bool = False  # True если узел найден
        self.ToLeft: bool = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def _key_exists(self, node) -> BSTFind:
        res = BSTFind()
        res.Node = node
        res.NodeHasKey = True
        return res

    def FindNodeByKey(self, key) -> BSTFind:
        if self.Root is None:
            return BSTFind()
        starting_node: BSTNode = self.Root
        while True:
            if starting_node.NodeKey == key:
                return self._key_exists(starting_node)
            if starting_node.NodeKey > key:
                if starting_node.LeftChild is None:
                    bst = BSTFind()
                    bst.Node = starting_node
                    bst.NodeHasKey = False
                    bst.ToLeft = True
                    return bst
                else:
                    starting_node = starting_node.LeftChild
                    continue
            else:
                if starting_node.RightChild is None:
                    bst = BSTFind()
                    bst.Node = starting_node
                    bst.NodeHasKey = False
                    bst.ToLeft = False
                    return bst
                else:
                    starting_node = starting_node.RightChild

    def AddKeyValue(self, key, val) -> bool:
        if self.Root is None:
            self.Root = BSTNode(key=key, val=val, parent=None)
            return True
        find_bst = self.FindNodeByKey(key)
        if find_bst.NodeHasKey:
            return False
        else:
            n_parent: BSTNode = find_bst.Node
            new_n = BSTNode(key=key, val=val, parent=n_parent)
            if find_bst.ToLeft:
                n_parent.LeftChild = new_n
            else:
                n_parent.RightChild = new_n
            return True

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool) -> BSTNode:
        if FromNode.LeftChild is None and FromNode.RightChild is None:
            return FromNode
        if FindMax:
            current_node = FromNode
            while True:
                if current_node.RightChild is None:
                    return current_node
                else:
                    current_node = current_node.RightChild
        else:
            current_node = FromNode
            while True:
                if current_node.LeftChild is None:
                    return current_node
                else:
                    current_node = current_node.LeftChild

    def DeleteNodeByKey(self, key) -> bool:
        # удаляем узел по ключу
        return False  # если узел не найден

    def Count(self) -> int:
        if self.Root is None:
            return 0
        nodes = [self.Root]
        c = 1
        tmp_nodes = [self.Root]
        while len(tmp_nodes) > 0:
            tmp_nodes = []
            for n in nodes:
                if n.LeftChild is not None:
                    c += 1
                    tmp_nodes.append(n.LeftChild)
                if n.RightChild is not None:
                    c += 1
                    tmp_nodes.append(n.RightChild)
            nodes = tmp_nodes
        return c