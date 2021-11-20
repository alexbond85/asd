from abst import aBST


def test_find_key_index_empty():
    tree = aBST(depth=0)
    assert tree.FindKeyIndex(5) == 0
    tree.AddKey(5)
    assert tree.Tree == [5]
    tree.AddKey(5)
    assert tree.Tree == [5]
    assert tree.AddKey(6) == -1
    assert tree.Tree == [5]


def test_find_key_index_three_nodes():
    tree = aBST(depth=1)
    assert tree.FindKeyIndex(2) == 0
    tree.AddKey(5)
    assert tree.Tree == [5, None, None]
    tree.AddKey(5)
    assert tree.Tree == [5, None, None]
    assert tree.AddKey(6) == 2
    assert tree.Tree == [5, None, 6]
    assert tree.AddKey(7) == -1
    assert tree.Tree == [5, None, 6]
    assert tree.AddKey(4) == 1
    assert tree.Tree == [5, 4, 6]
    assert tree.FindKeyIndex(4) == 1
    assert tree.FindKeyIndex(6) == 2


def test_find_key_index_seven_nodes():
    tree = aBST(depth=2)
    tree.AddKey(50)
    assert tree.FindKeyIndex(30) == -1
    assert tree.FindKeyIndex(70) == -2
    tree.AddKey(30)
    tree.AddKey(70)
    assert tree.Tree == [50, 30, 70, None, None, None, None]
    tree.AddKey(80)
    assert tree.Tree == [50, 30, 70, None, None, None, 80]
    tree.AddKey(10)
    assert tree.Tree == [50, 30, 70, 10, None, None, 80]
    tree.AddKey(40)
    assert tree.Tree == [50, 30, 70, 10, 40, None, 80]
    tree.AddKey(60)
    assert tree.Tree == [50, 30, 70, 10, 40, 60, 80]
    assert tree.FindKeyIndex(34) is None

