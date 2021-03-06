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
        self.Root = node

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
        if parent_node is None:
            self.Root = new_node
            self.Root.Parent = None
            return
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

    def _remove_if_n1_is_none(self, node, n1, n2):
        if n1 is None:
            if node is self.Root:
                self.Root = n2
                self.Root.Parent = None
                return True
            else:
                self._attach_to_parent(node.Parent, to_delete_node=node, new_node=n2)
            return True
        return False

    def _remove_if_no_left_child(self, node: BSTNode) -> bool:
        return self._remove_if_n1_is_none(node, node.LeftChild, node.RightChild)

    def _remove_if_no_right_child(self, node: BSTNode) -> bool:
        return self._remove_if_n1_is_none(node, node.RightChild, node.LeftChild)

    def _is_key_not_found(self, key) -> bool:
        f = self.FindNodeByKey(key)
        is_key_not_found = not f.NodeHasKey
        return is_key_not_found

    def DeleteNodeByKey(self, key) -> bool:
        if self._is_key_not_found(key):
            return False
        node: BSTNode = self.FindNodeByKey(key).Node
        if self._remove_if_leaf(node):
            return True
        if self._remove_if_no_left_child(node):
            return True
        if self._remove_if_no_right_child(node):
            return True

        left_child: BSTNode = node.LeftChild
        right_child: BSTNode = node.RightChild
        min_max_node = self.FinMinMax(FromNode=right_child, FindMax=False)
        # if min_max_node is None:
        #     min_max_node = right_child
        is_node_a_head = self.Root == node
        is_mmn_leaf = min_max_node.LeftChild is None and min_max_node.RightChild is None
        is_mmn_right_child = min_max_node is right_child

        if is_mmn_leaf:
            min_max_node.LeftChild = left_child
            left_child.Parent = min_max_node
            if not is_mmn_right_child:
                min_max_node.Parent.LeftChild = None
                min_max_node.RightChild = right_child
                right_child.Parent = min_max_node
                if not is_node_a_head:
                    min_max_node.Parent = node.Parent
                    if node is node.Parent.LeftChild:
                        node.Parent.LeftChild = min_max_node
                    if node is node.Parent.RightChild:
                        node.Parent.RightChild = min_max_node
                else:
                    self.Root = min_max_node
                    self.Root.Parent = None
            else:
                if not is_node_a_head:
                    right_child.Parent = node.Parent
                    if node is node.Parent.LeftChild:
                        node.Parent.LeftChild = right_child
                    if node is node.Parent.RightChild:
                        node.Parent.RightChild = right_child
                else:
                    self.Root = right_child
                    self.Root.Parent = None
        else:
            min_max_node.LeftChild = left_child
            left_child.Parent = min_max_node
            if is_mmn_right_child:
                if not is_node_a_head:
                    min_max_node.Parent = node.Parent
                    if node.Parent.LeftChild is node:
                        node.Parent.LeftChild = min_max_node
                    if node.Parent.RightChild is node:
                        node.Parent.LeftChild = min_max_node
                else:
                    self.Root = min_max_node
                    self.Root.Parent = None
            else:
                min_max_node.RightChild.Parent = min_max_node.Parent
                to_move = min_max_node.RightChild
                if min_max_node.Parent.RightChild == min_max_node:
                    min_max_node.Parent.RightChild = to_move
                if min_max_node.Parent.LeftChild == min_max_node:
                    min_max_node.Parent.LeftChild = to_move
                min_max_node.RightChild = right_child
                right_child.Parent = min_max_node
                if not is_node_a_head:
                    min_max_node.Parent = node.Parent
                    if node.Parent.LeftChild is node:
                        node.Parent.LeftChild = min_max_node
                    if node.Parent.RightChild is node:
                        node.Parent.LeftChild = min_max_node
                else:
                    self.Root = min_max_node
                    self.Root.Parent = None
        node.Parent = None
        node.RightChild = None
        node.LeftChild = None
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