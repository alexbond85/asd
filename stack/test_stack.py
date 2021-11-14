from stack import Stack


def test_push():
    s = Stack()
    s.push(1)
    assert s.stack == [1]
    assert s.pop() == 1
    assert s.stack == []
    s.push(1)
    s.push(2)
    assert s.stack == [2, 1]
    assert s.pop() == 2
    assert s.stack == [1]
    assert s.pop() == 1
    assert s.pop() is None


def test_peek():
    s = Stack()
    s.push(1)
    assert s.peek() == 1
    s.push(2)
    assert s.peek() == 2
    s.pop()
    assert s.peek() == 1
