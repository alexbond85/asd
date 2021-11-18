from t import SimpleTree, SimpleTreeNode


def test_add_root():
    st = SimpleTree(root=None)
    root = SimpleTreeNode(val=1, parent=None)
    st.AddChild(None, root)
    assert st.Root == root


def test_add_child():
    st = SimpleTree(root=None)
    root = SimpleTreeNode(val=1, parent=None)
    st.AddChild(None, root)
    ch1 = SimpleTreeNode(val=2, parent=root)
    st.AddChild(ParentNode=root, NewChild=ch1)
    assert root.Children == [ch1]
    assert ch1.Parent == root
    assert ch1.Children == []
    ch2 = SimpleTreeNode(val=3, parent=root)
    st.AddChild(ParentNode=root, NewChild=ch2)
    assert root.Children == [ch1, ch2]
    assert ch2.Parent == root
    assert ch2.Children == []

    ch3 = SimpleTreeNode(val=3, parent=root)
    st.AddChild(ParentNode=ch2, NewChild=ch3)
    assert ch2.Children == [ch3]
    assert ch3.Parent == ch2


def test_delete_node():
    st = SimpleTree(root=None)
    root = SimpleTreeNode(val=1, parent=None)
    st.AddChild(None, root)
    st.DeleteNode(root)
    assert st.Root is None

    st = SimpleTree(root=None)
    root = SimpleTreeNode(val=1, parent=None)
    ch1 = SimpleTreeNode(val=2, parent=root)
    st.AddChild(None, root)
    st.AddChild(root, ch1)
    st.DeleteNode(ch1)
    assert root.Children == []
    assert ch1.Parent is None

    st = SimpleTree(root=None)
    root = SimpleTreeNode(val=1, parent=None)
    ch1 = SimpleTreeNode(val=2, parent=root)
    ch2 = SimpleTreeNode(val=3, parent=root)
    st.AddChild(None, root)
    st.AddChild(root, ch1)
    st.AddChild(ParentNode=ch1, NewChild=ch2)
    st.DeleteNode(ch1)
    assert root.Children == []
    assert ch1.Parent is None
    assert ch1.Children == []
    assert ch2.Parent is None
    assert ch2.Children == []

    st = SimpleTree(root=None)
    root = SimpleTreeNode(val=1, parent=None)
    ch1 = SimpleTreeNode(val=2, parent=root)
    ch2 = SimpleTreeNode(val=2, parent=root)
    ch3 = SimpleTreeNode(val=3, parent=root)
    ch4 = SimpleTreeNode(val=4, parent=root)
    st.AddChild(None, root)
    st.AddChild(root, ch1)
    st.AddChild(ParentNode=ch1, NewChild=ch2)
    st.AddChild(ParentNode=ch1, NewChild=ch3)
    st.AddChild(ParentNode=ch3, NewChild=ch4)
    st.DeleteNode(ch1)
    assert root.Children == []
    assert ch1.Parent is None
    assert ch1.Children == []
    assert ch2.Parent is None
    assert ch2.Children == []
    assert ch3.Parent is None
    assert ch3.Children == []
    assert ch4.Children == []
    assert ch4.Parent is None


def test_get_all_nodes():
    st = SimpleTree(root=None)
    assert st.GetAllNodes() == []
    assert st.Count() == 0
    assert st.LeafCount() == 0

    root = SimpleTreeNode(val=1, parent=None)
    st.AddChild(None, root)
    assert st.GetAllNodes() == [root]
    assert st.Count() == 1
    assert st.LeafCount() == 1
    assert st.FindNodesByValue(1) == [root]
    assert st.FindNodesByValue(0) == []

    st = SimpleTree(root=None)
    root = SimpleTreeNode(val=1, parent=None)
    st.AddChild(None, root)
    ch1 = SimpleTreeNode(val=2, parent=root)
    st.AddChild(ParentNode=root, NewChild=ch1)

    assert st.GetAllNodes() == [root, ch1]
    assert st.Count() == 2
    assert st.LeafCount() == 1
    assert st.FindNodesByValue(1) == [root]
    assert st.FindNodesByValue(2) == [ch1]
    assert st.FindNodesByValue(9) == []

    st = SimpleTree(root=None)
    root = SimpleTreeNode(val=1, parent=None)
    st.AddChild(None, root)
    ch1 = SimpleTreeNode(val=2, parent=root)
    ch2 = SimpleTreeNode(val=3, parent=root)
    st.AddChild(ParentNode=root, NewChild=ch1)
    st.AddChild(ParentNode=root, NewChild=ch2)

    assert st.GetAllNodes() == [root, ch1, ch2]
    assert st.Count() == 3
    assert st.LeafCount() == 2
    assert st.FindNodesByValue(1) == [root]
    assert st.FindNodesByValue(2) == [ch1]
    assert st.FindNodesByValue(3) == [ch2]
    assert st.FindNodesByValue(9) == []

    st = SimpleTree(root=None)
    root = SimpleTreeNode(val=1, parent=None)
    st.AddChild(None, root)
    ch1 = SimpleTreeNode(val=2, parent=root)
    ch2 = SimpleTreeNode(val=3, parent=root)
    st.AddChild(ParentNode=root, NewChild=ch1)
    st.AddChild(ParentNode=root, NewChild=ch2)

    ch4 = SimpleTreeNode(val=4, parent=root)
    ch5 = SimpleTreeNode(val=5, parent=root)
    ch6 = SimpleTreeNode(val=6, parent=root)
    ch11 = SimpleTreeNode(val=11, parent=root)

    st.AddChild(ParentNode=ch2, NewChild=ch11)
    st.AddChild(ParentNode=ch1, NewChild=ch4)
    st.AddChild(ParentNode=ch1, NewChild=ch5)
    st.AddChild(ParentNode=ch1, NewChild=ch6)

    assert set([id(s) for s in st.GetAllNodes()]) == set([id(s) for s in [root, ch1, ch2, ch4, ch5, ch6, ch11]])


def test_get_all_nodes2():
    st = SimpleTree(root=None)
    root = SimpleTreeNode(val=1, parent=None)
    st.AddChild(None, root)
    ch1 = SimpleTreeNode(val=2, parent=root)
    ch2 = SimpleTreeNode(val=3, parent=root)
    st.AddChild(ParentNode=root, NewChild=ch1)
    st.AddChild(ParentNode=root, NewChild=ch2)

    ch4 = SimpleTreeNode(val=4, parent=root)
    ch5 = SimpleTreeNode(val=5, parent=root)
    ch6 = SimpleTreeNode(val=6, parent=root)
    ch11 = SimpleTreeNode(val=11, parent=root)

    st.AddChild(ParentNode=ch2, NewChild=ch11)
    st.AddChild(ParentNode=ch1, NewChild=ch4)
    st.AddChild(ParentNode=ch1, NewChild=ch5)
    st.AddChild(ParentNode=ch1, NewChild=ch6)

    ch7 = SimpleTreeNode(val=7, parent=root)
    st.AddChild(ParentNode=ch4, NewChild=ch7)
    ch8 = SimpleTreeNode(val=8, parent=root)
    st.AddChild(ParentNode=ch6, NewChild=ch8)
    ch9 = SimpleTreeNode(val=9, parent=root)
    ch10 = SimpleTreeNode(val=10, parent=root)
    st.AddChild(ParentNode=ch8, NewChild=ch9)
    st.AddChild(ParentNode=ch8, NewChild=ch10)

    assert st.Count() == 11
    assert st.LeafCount() == 5


def test_move():
    st = SimpleTree(root=None)
    root = SimpleTreeNode(val=1, parent=None)
    st.AddChild(None, root)

    st.MoveNode(root, root)
    assert st.Count() == 1

    st = SimpleTree(root=None)
    root = SimpleTreeNode(val=0, parent=None)
    st.AddChild(None, root)
    ch1 = SimpleTreeNode(val=1, parent=root)
    ch2 = SimpleTreeNode(val=2, parent=root)
    ch3 = SimpleTreeNode(val=3, parent=root)
    st.AddChild(ParentNode=root, NewChild=ch1)
    st.AddChild(ParentNode=root, NewChild=ch2)
    st.AddChild(ParentNode=ch1, NewChild=ch3)
    st.MoveNode(ch1, ch2)
    assert st.Root.Children == [ch2]
    assert ch2.Children == [ch1]
    assert ch1.Children == [ch3]
    st.MoveNode(ch3, ch2)
    assert ch2.Children == [ch1, ch3]
    assert ch1.Parent == ch2
    assert ch3.Parent == ch2




