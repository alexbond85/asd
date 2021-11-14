import pytest

from dynarray import DynArray


def test_insert_into_empty():
    da = DynArray()
    da.insert(0, 123)
    assert da[0] == 123


def test_insert_at_end():
    da = DynArray()
    da.insert(0, 1)
    da.insert(1, 2)
    assert da[0] == 1
    assert da[1] == 2


def test_insert_at_beginning():
    da = DynArray()
    da.insert(0, 1)
    da.insert(0, 2)
    assert da[0] == 2
    assert da[1] == 1


def test_insert_between():
    da = DynArray()
    da.insert(0, 1)
    da.insert(1, 2)
    da.insert(2, 4)
    da.insert(2, 3)

    assert da[0] == 1
    assert da[1] == 2
    assert da[2] == 3
    assert da[3] == 4


def test_insert_capacity_unchanged():
    da = DynArray()
    capacity_before_insert = da.capacity
    for i in range(16):
        da.insert(i, i + 1)
    assert da.capacity == capacity_before_insert


def test_insert_capacity_changed():
    da = DynArray()
    capacity_before_insert = da.capacity
    for i in range(17):
        da.insert(i, i + 1)
    assert da.capacity == 2*capacity_before_insert


def test_wrong_index_insert():
    da = DynArray()
    with pytest.raises(IndexError):
        da.insert(123, 1)


def test_wrong_index_delete():
    da = DynArray()
    with pytest.raises(IndexError):
        da.delete(0)
    da.append(123)
    with pytest.raises(IndexError):
        da.delete(1)


def test_delete_beginning():
    da = DynArray()
    da.append(1)
    da.delete(0)
    assert da.count == 0
    da.append(1)
    da.append(2)
    da.append(3)
    da.delete(0)
    assert da.count == 2
    assert da[0] == 2
    assert da[1] == 3


def test_delete_end():
    da = DynArray()
    da.append(1)
    da.append(2)
    da.append(3)
    da.delete(2)
    assert da.count == 2
    assert da[0] == 1
    assert da[1] == 2
    da.delete(1)
    assert da.count == 1
    assert da[0] == 1


def test_resize_after_delete():
    da = DynArray()
    for i in range(17):
        da.append(i)
    assert da.capacity == 32
    assert da.count == 17
    da.delete(16)
    assert da.capacity == 32
    da.delete(15)
    assert da.capacity == 21
    da.delete(14)
    da.delete(13)
    da.delete(12)
    da.delete(11)
    da.delete(10)
    assert da.count == 10
    assert da.capacity == 16

