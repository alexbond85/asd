from balanced_bst import BalancedBST, BSTNode


def test_generate_tree_empty():
    bbst = BalancedBST()
    bbst.GenerateTree([])


def test_generate_tree_one_node():
    bbst = BalancedBST()
    bbst.GenerateTree([1])
    assert bbst.Root.NodeKey == 1
    assert bbst.Root.Parent is None


def test_generate_less_than_four_nodes():
    bbst = BalancedBST()
    bbst.GenerateTree([1, 2, 3])
    assert bbst.Root.NodeKey == 2
    assert bbst.Root.Parent is None
    assert bbst.Root.LeftChild.NodeKey == 1
    assert bbst.Root.RightChild.NodeKey == 3
    assert bbst.Root.Level == 0
    assert bbst.Root.LeftChild.Level == 1
    assert bbst.Root.RightChild.Level == 1

    bbst = BalancedBST()
    bbst.GenerateTree([2, 3])
    assert bbst.Root.NodeKey == 3
    assert bbst.Root.Parent is None
    assert bbst.Root.LeftChild.NodeKey == 2
    assert bbst.Root.RightChild is None
    assert bbst.Root.Level == 0
    assert bbst.Root.LeftChild.Level == 1

    bbst = BalancedBST()
    bbst.GenerateTree([1, 2])
    assert bbst.Root.NodeKey == 2
    assert bbst.Root.Parent is None
    assert bbst.Root.LeftChild.NodeKey == 1
    assert bbst.Root.RightChild is None
    assert bbst.Root.Level == 0
    assert bbst.Root.LeftChild.Level == 1
