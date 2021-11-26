from even_trees import SimpleTreeNode, SimpleTree


def test_even_trees():
    st = SimpleTree(root=None)
    root = SimpleTreeNode(val=0, parent=None)
    st.AddChild(None, root)
    assert st.EvenTrees() == []
    ch1 = SimpleTreeNode(val=1, parent=root)
    st.AddChild(ParentNode=root, NewChild=ch1)
    assert st.EvenTrees() == []
    ch2 = SimpleTreeNode(val=2, parent=root)
    st.AddChild(ParentNode=root, NewChild=ch2)
    assert st.EvenTrees() == []
    ch3 = SimpleTreeNode(val=3, parent=root)
    st.AddChild(ParentNode=root, NewChild=ch3)
    assert st.EvenTrees() == []


def test_even_trees_first_level():
    st = SimpleTree(root=None)
    root = SimpleTreeNode(val=0, parent=None)
    st.AddChild(None, root)
    ch1 = SimpleTreeNode(val=1, parent=root)
    ch2 = SimpleTreeNode(val=2, parent=root)
    ch3 = SimpleTreeNode(val=3, parent=root)
    ch4 = SimpleTreeNode(val=4, parent=ch2)
    ch5 = SimpleTreeNode(val=5, parent=ch3)

    st.AddChild(ParentNode=root, NewChild=ch1)
    st.AddChild(ParentNode=root, NewChild=ch2)
    st.AddChild(ParentNode=root, NewChild=ch3)
    st.AddChild(ParentNode=ch2, NewChild=ch4)
    st.AddChild(ParentNode=ch3, NewChild=ch5)
    assert st.EvenTrees() == [root, ch2, root, ch3]


def test_even_trees_second_level():
    st = SimpleTree(root=None)
    root = SimpleTreeNode(val=0, parent=None)
    st.AddChild(None, root)
    ch1 = SimpleTreeNode(val=1, parent=root)
    ch2 = SimpleTreeNode(val=2, parent=root)
    ch3 = SimpleTreeNode(val=3, parent=root)
    ch4 = SimpleTreeNode(val=4, parent=ch2)
    ch5 = SimpleTreeNode(val=5, parent=ch3)
    ch6 = SimpleTreeNode(val=4, parent=ch1)
    ch7 = SimpleTreeNode(val=5, parent=ch6)


    st.AddChild(ParentNode=root, NewChild=ch1)
    st.AddChild(ParentNode=root, NewChild=ch2)
    st.AddChild(ParentNode=root, NewChild=ch3)
    st.AddChild(ParentNode=ch2, NewChild=ch4)
    st.AddChild(ParentNode=ch3, NewChild=ch5)
    st.AddChild(ParentNode=ch1, NewChild=ch6)
    st.AddChild(ParentNode=ch6, NewChild=ch7)

    assert st.EvenTrees() == [root, ch2, root, ch3, ch1, ch6]


def test_even_trees_example():
    st = SimpleTree(root=None)
    root = SimpleTreeNode(val=1, parent=None)
    st.AddChild(None, root)
    ch2 = SimpleTreeNode(val=2, parent=root)
    ch3 = SimpleTreeNode(val=3, parent=root)
    ch6 = SimpleTreeNode(val=6, parent=root)

    ch5 = SimpleTreeNode(val=5, parent=ch2)
    ch7 = SimpleTreeNode(val=7, parent=ch2)

    ch4 = SimpleTreeNode(val=4, parent=ch3)

    ch8 = SimpleTreeNode(val=8, parent=ch6)
    ch9 = SimpleTreeNode(val=9, parent=ch8)
    ch10 = SimpleTreeNode(val=10, parent=ch8)


    st.AddChild(ParentNode=root, NewChild=ch2)
    st.AddChild(ParentNode=root, NewChild=ch3)
    st.AddChild(ParentNode=root, NewChild=ch6)

    st.AddChild(ParentNode=ch2, NewChild=ch5)
    st.AddChild(ParentNode=ch2, NewChild=ch7)

    st.AddChild(ParentNode=ch3, NewChild=ch4)

    st.AddChild(ParentNode=ch6, NewChild=ch8)

    st.AddChild(ParentNode=ch8, NewChild=ch9)
    st.AddChild(ParentNode=ch8, NewChild=ch10)


    assert st.EvenTrees() == [root, ch3, root, ch6]
