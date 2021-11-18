class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey: int = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None

        self.NodeHasKey: bool = False
        self.ToLeft: bool = False


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

    def _attach_to_parent(self, parent_node: BSTNode, to_delete_node: BSTNode, new_node: BSTNode):
        if parent_node.LeftChild is to_delete_node:
            parent_node.LeftChild = new_node
            if new_node is not None:
                new_node.Parent = parent_node
        if parent_node.RightChild is to_delete_node:
            parent_node.RightChild = new_node
            if new_node is not None:
                new_node.Parent = parent_node
        to_delete_node.Parent = None
        to_delete_node.LeftChild = None
        to_delete_node.RightChild = None


    def _remove_if_leaf(self, node: BSTNode) -> bool:
        is_node_a_leaf = node.LeftChild is None and node.RightChild is None
        if is_node_a_leaf:
            is_root_node = node is self.Root
            if is_root_node:
                self.Root = None
                return True
            self._attach_to_parent(node.Parent, to_delete_node=node, new_node=None)
            return True
        else:
            return False

    def _remove_if_no_left_child(self, node: BSTNode) -> bool:
        if node.LeftChild is None:
            if node is self.Root:
                self.Root = node.RightChild
                return True
            else:
                self._attach_to_parent(node.Parent, to_delete_node=node, new_node=node.RightChild)
            return True
        return False

    def _remove_if_no_right_child(self, node: BSTNode) -> bool:
        if node.RightChild is None:
            if node is self.Root:
                self.Root = node.LeftChild
                return True
            else:
                self._attach_to_parent(node.Parent, to_delete_node=node, new_node=node.LeftChild)
                return True
        return False

    def DeleteNodeByKey(self, key) -> bool:
        f = self.FindNodeByKey(key)
        is_key_not_found = not f.NodeHasKey
        if is_key_not_found:
            return False
        node: BSTNode = f.Node
        if self._remove_if_leaf(node):
            return True
        if self._remove_if_no_left_child(node):
            return True
        if self._remove_if_no_right_child(node):
            return True
        is_node_a_head = self.Root == node
        left_child: BSTNode = node.LeftChild
        right_child: BSTNode = node.RightChild
        if is_node_a_head:
            self.Root = right_child
        min_max_node = self.FinMinMax(FromNode=right_child, FindMax=False)
        is_mnn_leaf = min_max_node.LeftChild is None and min_max_node.RightChild is None
        min_max_node.LeftChild = left_child
        if is_mnn_leaf:
            left_child.Parent = min_max_node
        else:
            mnd_right: BSTNode = min_max_node.RightChild
            mnd_right.LeftChild = min_max_node
            min_max_node.Parent = mnd_right
            self._attach_to_parent(node.Parent, node, new_node=mnd_right)
        return True

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