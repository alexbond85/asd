from h import Heap


def test_make_heap_empty():
    h = Heap()
    h.MakeHeap([], 2)


def test_make_heap_one_element():
    h = Heap()
    h.MakeHeap([1], 1)
    assert h.HeapArray == [1, None, None]


