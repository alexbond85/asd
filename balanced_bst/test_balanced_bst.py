from balanced_bst import BalancedBST, BSTNode


def test_generate_tree_empty():
    bbst = BalancedBST()
    bbst.GenerateTree([])
    bbst.IsBalanced(bbst.Root)


def test_generate_tree_one_node():
    bbst = BalancedBST()
    bbst.GenerateTree([1])
    assert bbst.Root.NodeKey == 1
    assert bbst.Root.Parent is None
    assert bbst.IsBalanced(bbst.Root)


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
    assert bbst.IsBalanced(bbst.Root)

    bbst = BalancedBST()
    bbst.GenerateTree([2, 3])
    assert bbst.Root.NodeKey == 3
    assert bbst.Root.Parent is None
    assert bbst.Root.LeftChild.NodeKey == 2
    assert bbst.Root.RightChild is None
    assert bbst.Root.Level == 0
    assert bbst.Root.LeftChild.Level == 1
    assert bbst.IsBalanced(bbst.Root)


    bbst = BalancedBST()
    bbst.GenerateTree([1, 2])
    assert bbst.Root.NodeKey == 2
    assert bbst.Root.Parent is None
    assert bbst.Root.LeftChild.NodeKey == 1
    assert bbst.Root.RightChild is None
    assert bbst.Root.Level == 0
    assert bbst.Root.LeftChild.Level == 1
    assert bbst.IsBalanced(bbst.Root)


def test_generate_more_than_three_nodes():
    bbst = BalancedBST()
    bbst.GenerateTree([1, 2, 3, 7, 5, 6, 4])
    assert bbst.Root.NodeKey == 4
    assert bbst.Root.Parent is None
    assert bbst.Root.LeftChild.NodeKey == 2
    assert bbst.Root.RightChild.NodeKey == 6
    assert bbst.Root.LeftChild.Parent == bbst.Root
    assert bbst.Root.RightChild.Parent == bbst.Root
    assert bbst.Root.LeftChild.LeftChild.NodeKey == 1
    assert bbst.Root.LeftChild.RightChild.NodeKey == 3
    assert bbst.Root.RightChild.LeftChild.NodeKey == 5
    assert bbst.Root.RightChild.RightChild.NodeKey == 7
    assert bbst.IsBalanced(bbst.Root)


def test_generate_more_than_three_nodes():
    bbst = BalancedBST()

    bbst.GenerateTree([10])
    root = bbst.Root
    n1 = BSTNode(key=9, parent=root)
    root.LeftChild = n1
    n1.Level = 1
    n2 = BSTNode(key=8, parent=n1)
    n1.LeftChild = n2
    n2.Level = 2
    assert not bbst.IsBalanced(bbst.Root)
    assert bbst.IsBalanced(bbst.Root.LeftChild)
    assert bbst.IsBalanced(bbst.Root.LeftChild.LeftChild)


def test_max_depth():
    bbst = BalancedBST()
    arr = list(range(0, 2**8))
    bbst.GenerateTree(arr)
    assert bbst._max_depth(bbst.Root) == 9
