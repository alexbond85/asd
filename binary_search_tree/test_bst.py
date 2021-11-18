from bst import BSTNode, BSTFind, BST


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




