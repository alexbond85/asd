from bst import BST, BSTFind, BSTNode


def test_add_key_value():
    bst = BST(None)
    f = bst.FindNodeByKey(10)
    assert f.Node is None
    assert bst.AddKeyValue(10, "a")

    f: BSTFind = bst.FindNodeByKey(10)
    assert f.Node.NodeKey == 10
    f: BSTFind = bst.FindNodeByKey(9)
    assert f.Node.NodeKey == 10
    assert not f.NodeHasKey
    assert f.ToLeft
    f: BSTFind = bst.FindNodeByKey(11)
    assert not f.NodeHasKey
    assert f.Node.NodeKey == 10
    assert not f.ToLeft

    bst = BST(None)
    assert bst.AddKeyValue(10, "a")
    assert bst.Count() == 1
    assert bst.Root is bst.FinMinMax(bst.Root, FindMax=True)
    assert bst.Root is bst.FinMinMax(bst.Root, FindMax=False)
    bst.AddKeyValue(9, "b")
    assert bst.Count() == 2
    bst.AddKeyValue(11, "c")
    assert bst.Count() == 3
    bst.AddKeyValue(12, "d")
    assert bst.Count() == 4
    bst.AddKeyValue(13, "e")
    assert bst.Count() == 5
    assert bst.FinMinMax(bst.Root, FindMax=False).NodeKey == 9
    assert bst.FinMinMax(bst.Root, FindMax=True).NodeKey == 13
    assert bst.FinMinMax(bst.Root.LeftChild, FindMax=False).NodeKey == 9
    assert bst.FinMinMax(bst.Root.LeftChild, FindMax=True).NodeKey == 9
    assert bst.FinMinMax(bst.Root.RightChild, FindMax=False).NodeKey == 11
    assert bst.FinMinMax(bst.Root.RightChild, FindMax=True).NodeKey == 13


def test1():
    bst = BST(None)
    bst.AddKeyValue(10, "a")
    assert not bst.DeleteNodeByKey(9)
    assert bst.DeleteNodeByKey(10)
    assert bst.Root is None


def test2():
    bst = BST(None)
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(9, "b")
    assert bst.DeleteNodeByKey(10)
    assert bst.Count() == 1
    assert bst.Root.LeftChild is None
    assert bst.Root.RightChild is None
    assert bst.Root.NodeKey == 9

    bst = BST(None)
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(9, "b")
    assert bst.DeleteNodeByKey(9)
    assert bst.Count() == 1
    assert bst.Root.LeftChild is None
    assert bst.Root.RightChild is None
    assert bst.Root.NodeKey == 10


def test3():
    bst = BST(None)
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(11, "b")
    assert bst.DeleteNodeByKey(10)
    assert bst.Count() == 1
    assert bst.Root.LeftChild is None
    assert bst.Root.RightChild is None
    assert bst.Root.NodeKey == 11

    bst = BST(None)
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(11, "b")
    assert bst.DeleteNodeByKey(11)
    assert bst.Count() == 1
    assert bst.Root.LeftChild is None
    assert bst.Root.RightChild is None
    assert bst.Root.NodeKey == 10


def test4():
    bst = BST(None)
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(9, "o")
    bst.AddKeyValue(11, "b")

    assert bst.DeleteNodeByKey(10)
    assert bst.Count() == 2
    assert bst.Root.NodeKey == 11
    assert bst.Root.LeftChild.NodeKey == 9
    assert bst.Root.RightChild is None

    bst = BST(None)
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(9, "o")
    bst.AddKeyValue(11, "b")

    assert bst.DeleteNodeByKey(9)
    assert bst.Count() == 2
    assert bst.Root.NodeKey == 10
    assert bst.Root.LeftChild is None
    assert bst.Root.RightChild.NodeKey == 11

    bst = BST(None)
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(9, "o")
    bst.AddKeyValue(11, "b")

    assert bst.DeleteNodeByKey(11)
    assert bst.Count() == 2
    assert bst.Root.NodeKey == 10
    assert bst.Root.LeftChild.NodeKey == 9
    assert bst.Root.RightChild is None


def test5():
    bst = BST(None)
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(5, "o")
    bst.AddKeyValue(15, "b")
    bst.AddKeyValue(3, "b")

    bst.DeleteNodeByKey(15)
    assert bst.Count() == 3
    assert bst.Root.NodeKey == 10
    assert bst.Root.RightChild is None
    assert bst.Root.LeftChild.NodeKey == 5
    assert bst.Root.LeftChild.LeftChild.NodeKey == 3


def test51():
    bst = BST(None)
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(5, "o")
    bst.AddKeyValue(15, "b")
    bst.AddKeyValue(6, "b")

    bst.DeleteNodeByKey(6)
    assert bst.Count() == 3


def test61():
    bst = BST(None)
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(5, "o")
    bst.AddKeyValue(15, "b")
    bst.AddKeyValue(2, "b")
    bst.AddKeyValue(6, "b")
    bst.AddKeyValue(12, "b")

    bst.DeleteNodeByKey(10)
    assert bst.Count() == 5


def test71():
    bst = BST(None)
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(5, "o")
    bst.AddKeyValue(15, "b")
    bst.AddKeyValue(2, "b")
    bst.AddKeyValue(6, "b")
    bst.AddKeyValue(16, "b")

    bst.DeleteNodeByKey(10)
    assert bst.Count() == 5


def test81():
    bst = BST(None)
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(5, "o")
    bst.AddKeyValue(15, "b")
    bst.AddKeyValue(3, "b")
    bst.AddKeyValue(7, "b")
    bst.AddKeyValue(8, "b")
    bst.AddKeyValue(2, "b")
    bst.AddKeyValue(4, "b")

    bst.DeleteNodeByKey(154)
    assert bst.Count() == 8


def test_remove_if_leaf():
    bst = BST(None)
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(15, "a")
    bst.DeleteNodeByKey(15)
    assert bst.Count() == 1


def test_remove_if_no_left_child():
    bst = BST(None)
    bst.AddKeyValue(15, "a")
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(20, "a")
    bst.AddKeyValue(8, "a")
    bst.DeleteNodeByKey(10)
    assert bst.Count() == 3


def test_node_head_leaf():
    bst = BST(None)
    bst.AddKeyValue(15, "a")
    bst.DeleteNodeByKey(15)
    assert bst.Count() == 0


def test_node_head_has_only_right():
    bst = BST(None)
    bst.AddKeyValue(15, "a")
    bst.AddKeyValue(20, "a")
    bst.DeleteNodeByKey(15)
    assert bst.Count() == 1


def test_node_head_has_only_left():
    bst = BST(None)
    bst.AddKeyValue(15, "a")
    bst.AddKeyValue(10, "a")
    bst.DeleteNodeByKey(15)
    assert bst.Count() == 1


def test_node_head_mmd_is_leaf():
    bst = BST(None)
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(8, "a")
    bst.AddKeyValue(11, "a")
    bst.DeleteNodeByKey(10)
    assert bst.Count() == 2


def test_node_head_mmd_is_not_leaf():
    bst = BST(None)
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(8, "a")
    bst.AddKeyValue(11, "a")
    bst.AddKeyValue(12, "a")
    bst.DeleteNodeByKey(10)
    assert bst.Count() == 3
    assert bst.Root.NodeKey == 11
    assert bst.Root.LeftChild.NodeKey == 8
    assert bst.Root.RightChild.NodeKey == 12


def test_delete_delete():
    bst = BST(None)
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(5, "a")
    bst.AddKeyValue(20, "a")
    bst.AddKeyValue(15, "a")
    bst.AddKeyValue(25, "a")
    bst.AddKeyValue(14, "a")
    bst.AddKeyValue(16, "a")
    bst.DeleteNodeByKey(15)
    assert bst.Count() == 6
    a = bst.FindNodeByKey(15)
    print()


def test_delete_4_nodes():
    bst = BST(None)
    bst.AddKeyValue(0, "a")
    bst.AddKeyValue(10, "a")
    bst.AddKeyValue(5, "a")
    bst.AddKeyValue(15, "a")
    bst.DeleteNodeByKey(10)
    print()
