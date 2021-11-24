from h import Heap


def test_make_heap_empty():
    h = Heap()
    h.MakeHeap([], 2)


def test_make_heap_one_element():
    h = Heap()
    h.MakeHeap([1], 1)
    assert h.HeapArray == [1, None, None]


def test_make_heap_two_elements():
    h = Heap()
    h.MakeHeap([1, 2], 1)
    assert h.HeapArray == [2, 1, None]

    h = Heap()
    h.MakeHeap([3, 2], 1)
    assert h.HeapArray == [3, 2, None]


def test_make_heap_three_elements():
    h = Heap()
    h.MakeHeap([1, 2, 3], 1)
    assert h.HeapArray == [3, 1, 2]

    h = Heap()
    h.MakeHeap([3, 2, 1], 1)
    assert h.HeapArray == [3, 2, 1]


def test_make_heap_more_than_three_elements():
    h = Heap()
    h.MakeHeap([1, 2, 3, 4], 2)
    assert h.HeapArray == [4, 3, 2, 1, None, None, None]

    h = Heap()
    h.MakeHeap([3, 2, 1, 4, 5], 2)
    assert h.HeapArray == [5, 4, 1, 2, 3, None, None]

    h = Heap()
    h.MakeHeap([3, 2, 1, 4, 5, 6], 2)
    assert h.HeapArray == [6, 4, 5, 2, 3, 1, None]

    h = Heap()
    h.MakeHeap([3, 2, 1, 4, 5, 6, 7], 2)
    assert h.HeapArray == [7, 4, 6, 2, 3, 1, 5]
