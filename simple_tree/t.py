class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def _add_root(self, n: SimpleTreeNode):
        self.Root = n

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode):
        if ParentNode is None:
            self._add_root(NewChild)
        else:
            ParentNode.Children.append(NewChild)
            NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete: SimpleTreeNode):
        n = NodeToDelete
        n_parent: SimpleTreeNode = n.Parent
        if n_parent is None:
            self.Root = None
        else:
            n_parent.Children = [c for c in n_parent.Children if c != n]
            all_nodes = self._get_all_nodes_subtree(n)
            for n in all_nodes:
                n.Parent = None
                n.Children = []

    def _get_all_nodes_subtree(self, starting_node: SimpleTreeNode):
        node: SimpleTreeNode = starting_node
        nodes = [node]
        tmp_nodes = node.Children
        while len(tmp_nodes) > 0:
            nodes += tmp_nodes
            all_children = []
            for n in tmp_nodes:
                all_children += n.Children
            tmp_nodes = all_children
        return nodes

    def GetAllNodes(self):
        nodes = []
        if self.Root is None:
            return nodes
        return self._get_all_nodes_subtree(starting_node=self.Root)

    def FindNodesByValue(self, val):
        all_nodes = [n for n in self.GetAllNodes() if n.NodeValue == val]
        return all_nodes

    def MoveNode(self, OriginalNode: SimpleTreeNode, NewParent: SimpleTreeNode):
        if OriginalNode == NewParent:
            return
        if OriginalNode.Parent is not None:
            p: SimpleTreeNode = OriginalNode.Parent
            p.Children = [c for c in p.Children if c!= OriginalNode]
        NewParent.Children.append(OriginalNode)

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        nodes = self.GetAllNodes()
        leafs = [n for n in nodes if n.Children == []]
        return len(leafs)

    def _all_values(self):
        return [n.NodeValue for n in self.GetAllNodes()]
