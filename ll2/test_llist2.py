from ll2.llist2 import LinkedList2, Node


def test_add_in_head_empty_list():
    ll = LinkedList2()
    n = Node(1)
    ll.add_in_head(n)
    assert ll.head == n
    assert ll.tail == n


def test_len_empty():
    ll = LinkedList2()
    assert ll.len() == 0


def test_len_non_empty():
    ll = LinkedList2()
    n1 = Node(1)
    n2 = Node(2)

    ll.add_in_tail(n1)
    assert ll.len() == 1
    ll.add_in_tail(n2)
    assert ll.len() == 2

    ll.clean()

    ll.insert(afterNode=None, newNode=n1)
    assert ll.len() == 1

    ll.insert(afterNode=None, newNode=n2)
    assert ll.len() == 2


def test_add_in_head_non_empty_list():
    ll = LinkedList2()
    n1 = Node(1)
    n2 = Node(2)
    ll.add_in_tail(n2)
    ll.add_in_head(n1)
    assert ll.head == n1
    assert ll.tail == n2
    assert n1.next == n2
    assert n1.prev is None
    assert n2.prev == n1
    assert n2.next is None
    n0 = Node(0)
    ll.add_in_head(n0)
    assert ll.head == n0
    assert ll.len() == 3


def test_clean():
    ll = LinkedList2()
    n1 = Node(v=1)
    ll.add_in_tail(n1)
    ll.clean()

    assert ll.len() == 0
    assert ll.head is None
    assert ll.tail is None

    ll = LinkedList2()
    n1 = Node(v=1)
    n2 = Node(v=2)
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.clean()
    assert ll.len() == 0
    assert ll.head is None
    assert ll.tail is None
    assert n1.next is None
    assert n2.next is None


def test_insert_no_after_node():
    ll = LinkedList2()
    n1 = Node(v=1)
    ll.insert(None, n1)
    assert ll.len() == 1
    assert ll.head == n1
    assert ll.tail == n1

    n2 = Node(v=2)
    ll.insert(None, n2)
    assert ll.len() == 2
    assert ll.head == n1
    assert ll.tail == n2
    assert n1.prev is None
    assert n1.next == n2
    assert n2.prev == n1
    assert n2.next is None


def test_insert():
    ll = LinkedList2()
    n1 = Node(v=1)
    ll.add_in_tail(n1)
    n2 = Node(v=2)
    ll.insert(afterNode=n1, newNode=n2)

    assert ll.len() == 2
    assert ll.head == n1
    assert ll.tail == n2
    assert n2.prev == n1
    assert n2.next is None
    assert n1.next is n2

    ll = LinkedList2()
    n1 = Node(v=1)
    n3 = Node(v=2)
    ll.add_in_tail(n1)
    ll.add_in_tail(n3)
    n2 = Node(v=2)

    ll.insert(afterNode=n1, newNode=n2)
    assert ll.len() == 3
    assert ll.head == n1
    assert ll.tail == n3
    assert n1.next == n2
    assert n3.prev == n2
    assert n2.prev == n1
    assert n2.next == n3


def test_find_all():
    ll = LinkedList2()
    assert ll.find_all(val=1) == []
    n1 = Node(v=1)
    ll.insert(afterNode=None, newNode=n1)
    assert ll.find_all(val=1) == [n1]
    n2 = Node(v=1)
    ll.insert(afterNode=n1, newNode=n2)
    assert ll.find_all(val=1) == [n1, n2]
    assert ll.find_all(val=0) == []
    n3 = Node(v=1)
    ll.add_in_tail(n3)
    assert ll.len() == 3
    assert ll.find_all(val=1) == [n1, n2, n3]


def test_delete_from_empty():
    ll = LinkedList2()
    ll.delete(val=1, all=False)
    assert ll.len() == 0


def test_delete_from_head():
    ll = LinkedList2()
    n1 = Node(v=1)
    n2 = Node(v=2)
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.delete(val=1, all=False)
    assert ll.head == n2
    assert ll.tail == n2
    assert n2.next is None
    assert ll.len() == 1
    assert n1.next is None
    assert n1.prev is None
    assert n2.next is None
    assert n2.prev is None


def test_delete_from_tail():
    ll = LinkedList2()
    n1 = Node(v=1)
    n2 = Node(v=2)
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.delete(val=2, all=False)
    assert ll.head == n1
    assert ll.tail == n1
    assert n1.next is None
    assert ll.len() == 1
    assert n1.prev is None
    assert n2.prev is None
    assert n2.next is None


def test_delete_from_head_tail():
    ll = LinkedList2()
    n1 = Node(v=1)
    ll.add_in_tail(n1)
    ll.delete(val=1, all=False)
    assert ll.head is None
    assert ll.tail is None
    assert ll.len() == 0


def test_delete_from_between():
    ll = LinkedList2()
    n1 = Node(v=1)
    n2 = Node(v=2)
    n3 = Node(v=3)
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.delete(2, all=False)
    assert ll.len() == 2
    assert ll.head == n1
    assert ll.tail == n3
    assert n2.next is None
    assert n1.next == n3


def test_delete_all_head_tail():
    ll = LinkedList2()
    n1 = Node(v=1)
    n2 = Node(v=1)
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.delete(1, all=True)
    assert ll.len() == 0


def test_delete_all_in_between():
    ll = LinkedList2()
    ll.add_in_tail(Node(v=1))
    ll.add_in_tail(Node(v=1))
    ll.add_in_tail(Node(v=2))
    ll.add_in_tail(Node(v=2))
    ll.add_in_tail(Node(v=1))
    ll.add_in_tail(Node(v=1))
    ll.delete(2, all=True)
    assert ll.len() == 4

    ll = LinkedList2()
    ll.add_in_tail(Node(v=1))
    ll.add_in_tail(Node(v=1))
    ll.add_in_tail(Node(v=2))
    ll.add_in_tail(Node(v=3))
    ll.add_in_tail(Node(v=1))
    ll.add_in_tail(Node(v=1))
    ll.delete(1, all=True)
    assert ll.len() == 2
    ll.delete(0, all=True)
    assert ll.len() == 2
