from bst_traverse import BST


def _tree_keys(nodes):
    return tuple(x.NodeKey for x in nodes)


def test_empty():
    bst = BST(None)
    assert bst.WideAllNodes() == ()
    assert bst.DeepAllNodes(0) == ()
    assert bst.DeepAllNodes(1) == ()
    assert bst.DeepAllNodes(2) == ()


def test_one_node():
    bst = BST(None)
    bst.AddKeyValue(10, 10)
    assert _tree_keys(bst.WideAllNodes()) == (10,)
    assert _tree_keys(bst.DeepAllNodes(0)) == (10,)
    assert _tree_keys(bst.DeepAllNodes(1)) == (10,)
    assert _tree_keys(bst.DeepAllNodes(2)) == (10,)


def test_two_nodes():
    bst = BST(None)
    bst.AddKeyValue(10, 10)
    bst.AddKeyValue(9, 9)
    assert _tree_keys(bst.WideAllNodes()) == (10, 9)
    assert _tree_keys(bst.DeepAllNodes(0)) == (9, 10,)
    assert _tree_keys(bst.DeepAllNodes(1)) == (9, 10,)
    assert _tree_keys(bst.DeepAllNodes(2)) == (10, 9)

    bst = BST(None)
    bst.AddKeyValue(10, 10)
    bst.AddKeyValue(11, 11)
    assert _tree_keys(bst.WideAllNodes()) == (10, 11)
    assert _tree_keys(bst.DeepAllNodes(0)) == (10, 11)
    assert _tree_keys(bst.DeepAllNodes(1)) == (11, 10)
    assert _tree_keys(bst.DeepAllNodes(2)) == (10, 11)


def test_three_nodes():
    bst = BST(None)
    bst.AddKeyValue(10, 10)
    bst.AddKeyValue(9, 9)
    bst.AddKeyValue(11, 11)
    assert _tree_keys(bst.WideAllNodes()) == (10, 9, 11)
    assert _tree_keys(bst.DeepAllNodes(0)) == (9, 10, 11)
    assert _tree_keys(bst.DeepAllNodes(1)) == (9, 11, 10)
    assert _tree_keys(bst.DeepAllNodes(2)) == (10, 9, 11)


def test_five_nodes():
    bst = BST(None)
    bst.AddKeyValue(10, 10)
    bst.AddKeyValue(5, 5)
    bst.AddKeyValue(15, 15)
    bst.AddKeyValue(6, 6)
    bst.AddKeyValue(12, 12)
    assert _tree_keys(bst.WideAllNodes()) == (10, 5, 15, 6, 12)
    assert _tree_keys(bst.DeepAllNodes(0)) == (5, 6, 10, 12, 15)
    assert _tree_keys(bst.DeepAllNodes(1)) == (6, 5, 12, 15, 10)
    assert _tree_keys(bst.DeepAllNodes(2)) == (10, 5, 6, 15, 12)
