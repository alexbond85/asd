from deque import Deque


def test_remove_front():
    d = Deque()
    assert d.removeFront() is None
    d.addFront(1)
    assert d.removeFront() == 1
    d.addFront(1)
    d.addFront(2)
    assert d.size() == 2
    assert d.removeFront() == 2


def test_remove_tail():
    d = Deque()
    assert d.removeTail() is None
    d.addTail(1)
    assert d.removeTail() == 1
    d.addTail(1)
    d.addTail(2)
    assert d.size() == 2
    assert d.removeTail() == 2
    assert d.size() == 1
    assert d.removeTail() == 1
    assert d.removeTail() is None


def test_size():
    d = Deque()
    assert d.size() == 0
    d.addTail(1)
    assert d.size() == 1
    d.addTail(2)
    d.addTail(3)
    assert d.size() == 3
    d.removeFront()
    assert d.size() == 2
    d.removeFront()
    d.removeFront()
    assert d.size() == 0
    d.removeFront()
    assert d.size() == 0

