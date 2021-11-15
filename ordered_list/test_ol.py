from ol_think import OrderedList


def test_ol_add_empty():
    ol = OrderedList(asc=True)
    assert ol.len() == 0
    assert [v.value for v in ol.get_all()] == []
    ol.add(2)
    assert [v.value for v in ol.get_all()] == [2]
    assert ol.len() == 1


def test_ol_add_list_one_element_asc():
    ol = OrderedList(asc=True)
    ol.add(1)
    ol.add(2)
    assert [v.value for v in ol.get_all()] == [1, 2]
    assert ol.head.value == 1
    assert ol.tail.value == 2
    assert ol.head.next == ol.tail
    assert ol.tail.next is None
    assert ol.tail.prev is ol.head
    ol = OrderedList(asc=True)
    ol.add(2)
    ol.add(1)
    assert [v.value for v in ol.get_all()] == [1, 2]
    assert ol.head.value == 1
    assert ol.tail.value == 2
    assert ol.head.next == ol.tail
    assert ol.tail.next is None
    assert ol.tail.prev is ol.head
    assert ol.len() == 2


def test_ol_asc_combinations():
    ol = OrderedList(asc=True)
    ol.add(1)
    ol.add(2)
    ol.add(3)
    assert [v.value for v in ol.get_all()] == [1, 2, 3]
    # ol = OrderedList(asc=True)
    ol.clean(asc=True)
    ol.add(1)
    ol.add(3)
    ol.add(2)
    assert [v.value for v in ol.get_all()] == [1, 2, 3]
    ol = OrderedList(asc=True)
    ol.add(2)
    ol.add(1)
    ol.add(3)
    assert [v.value for v in ol.get_all()] == [1, 2, 3]
    ol = OrderedList(asc=True)
    ol.add(2)
    ol.add(3)
    ol.add(1)
    assert [v.value for v in ol.get_all()] == [1, 2, 3]
    ol = OrderedList(asc=True)
    ol.add(3)
    ol.add(1)
    ol.add(2)
    assert [v.value for v in ol.get_all()] == [1, 2, 3]
    ol = OrderedList(asc=True)
    ol.add(3)
    ol.add(2)
    ol.add(1)
    assert [v.value for v in ol.get_all()] == [1, 2, 3]


def test_four_elem_list_asc():
    import itertools
    ol = OrderedList(asc=True)
    for el in list(itertools.permutations([1, 2, 3, 4])):
        a, b, c, d = el
        ol.clean(asc=True)
        ol.add(a)
        ol.add(b)
        ol.add(c)
        ol.add(d)
        assert [v.value for v in ol.get_all()] == [1, 2, 3, 4]
    for el in list(itertools.permutations([1, 1, 2])):
        a, b, c = el
        ol = OrderedList(asc=True)
        ol.add(a)
        ol.add(b)
        ol.add(c)
        assert [v.value for v in ol.get_all()] == [1, 1, 2]
    for el in list(itertools.permutations([2, 1, 2])):
        a, b, c = el
        ol = OrderedList(asc=True)
        ol.add(a)
        ol.add(b)
        ol.add(c)
        assert [v.value for v in ol.get_all()] == [1, 2, 2]


############

def test_ol_add_list_one_element_desc():
    ol = OrderedList(asc=False)
    ol.add(1)
    ol.add(2)
    assert [v.value for v in ol.get_all()] == [2, 1]
    assert ol.head.value == 2
    assert ol.tail.value == 1
    assert ol.head.next == ol.tail
    assert ol.tail.next is None
    assert ol.tail.prev is ol.head
    ol = OrderedList(asc=False)
    ol.add(2)
    ol.add(1)
    assert [v.value for v in ol.get_all()] == [2, 1]
    assert ol.head.value == 2
    assert ol.tail.value == 1
    assert ol.head.next == ol.tail
    assert ol.tail.next is None
    assert ol.tail.prev is ol.head


def test_ol_desc_combinations():
    ol = OrderedList(asc=False)
    ol.add(1)
    ol.add(2)
    ol.add(3)
    assert [v.value for v in ol.get_all()] == [3, 2, 1]
    ol.clean(asc=False)
    ol.add(1)
    ol.add(3)
    ol.add(2)
    assert [v.value for v in ol.get_all()] == [3, 2, 1]
    ol = OrderedList(asc=False)
    ol.add(2)
    ol.add(1)
    ol.add(3)
    assert [v.value for v in ol.get_all()] == [3, 2, 1]
    ol = OrderedList(asc=False)
    ol.add(2)
    ol.add(3)
    ol.add(1)
    assert [v.value for v in ol.get_all()] == [3, 2, 1]
    ol = OrderedList(asc=False)
    ol.add(3)
    ol.add(1)
    ol.add(2)
    assert [v.value for v in ol.get_all()] == [3, 2, 1]
    ol = OrderedList(asc=False)
    ol.add(3)
    ol.add(2)
    ol.add(1)
    assert [v.value for v in ol.get_all()] == [3, 2, 1]


def test_four_elem_list_desc():
    import itertools
    for el in list(itertools.permutations([4, 3, 2, 1])):
        a, b, c, d = el
        ol = OrderedList(asc=False)
        ol.add(a)
        ol.add(b)
        ol.add(c)
        ol.add(d)
        assert [v.value for v in ol.get_all()] == [4, 3, 2, 1]
        assert ol.len() == 4
    for el in list(itertools.permutations([1, 1, 2])):
        a, b, c = el
        ol = OrderedList(asc=False)
        ol.add(a)
        ol.add(b)
        ol.add(c)
        assert [v.value for v in ol.get_all()] == [2, 1, 1]
    for el in list(itertools.permutations([2, 1, 2])):
        a, b, c = el
        ol = OrderedList(asc=False)
        ol.add(a)
        ol.add(b)
        ol.add(c)
        assert [v.value for v in ol.get_all()] == [2, 2, 1]
        assert ol.len() == 3


def test_find():
    ol = OrderedList(asc=False)
    ol.add(2)
    assert ol.find(2).value == 2
    ol.add(4)
    assert ol.find(4).value == 4
    ol.add(2)
    assert ol.find(2).value == 2
    ol.add(1)
    assert ol.find(1).value == 1
    assert ol.find(0) is None


def test_delete_from_empty():
    ll = OrderedList(asc=True)
    ll.delete(val=1)
    assert ll.len() == 0


def test_delete_from_head():
    ll = OrderedList(asc=True)
    ll.add(1)
    ll.add(2)
    ll.delete(val=1)
    assert ll.len() == 1
    assert ll.head.value == 2
    assert ll.tail.value == 2
    assert ll.head.next is None
    assert ll.head.prev is None
    assert ll.tail.prev is None
    assert ll.tail.next is None
    assert [v.value for v in ll.get_all()] == [2]


def test_delete_from_head2():
    ll = OrderedList(asc=True)
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.delete(val=1)
    assert ll.len() == 2
    assert ll.head.value == 2
    assert ll.tail.value == 3
    assert [v.value for v in ll.get_all()] == [2, 3]


def test_delete_from_head_tail():
    ll = OrderedList(asc=False)
    ll.add(1)
    ll.delete(val=1)
    assert ll.head is None
    assert ll.tail is None
    assert ll.len() == 0
    assert [v.value for v in ll.get_all()] == []


def test_delete_from_between():
    ll = OrderedList(asc=False)
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.delete(2)
    assert ll.len() == 2
    assert ll.head.value == 3
    assert ll.tail.value == 1


def find_optimized():
    for flag in [True, False]:
        ll = OrderedList(asc=flag)
        ll.add(1)
        assert ll.find(0) is None
        ll = OrderedList(asc=flag)
        ll.add(1)
        assert ll.find(1).value == 1
        ll = OrderedList(asc=flag)
        ll.add(1)
        ll.add(2)
        assert ll.find(0) is None
        assert ll.find(2).value == 2
        assert ll.find(1).value == 1
        assert ll.find(3) is None
        ll.add(2)
        assert ll.find(2).value == 2
        ll.clean(asc=flag)
        ll.add(11)
        ll.add(21)
        ll.add(31)
        assert ll.find(21).value == 21
        assert ll.find(11).value == 11
        assert ll.find(31).value == 31


