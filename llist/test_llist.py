from llist import LinkedList, Node


def test_insert_into_empty_list():
    ll = LinkedList()
    n = Node(v=1)
    ll.insert(afterNode=None, newNode=n)
    assert ll.head == n
    assert n.next is None
    assert ll.tail == ll.head


def test_insert_after_tail():
    ll = LinkedList()
    n1 = Node(v=1)
    ll.insert(afterNode=None, newNode=n1)
    assert ll.head == n1
    assert ll.tail == n1
    n2 = Node(v=2)
    ll.insert(afterNode=n1, newNode=n2)
    assert ll.head == n1
    assert ll.tail == n2
    assert n1.next == n2


def test_add_head_non_empty():
    ll = LinkedList()
    n1 = Node(v=1)
    n2 = Node(v=2)
    ll.insert(afterNode=None, newNode=n2)
    ll.insert(afterNode=None, newNode=n1)
    assert ll.head == n1
    assert n1.next == n2
    assert ll.tail == n2
    assert n2.next is None


def test_insert():
    ll = LinkedList()
    n1 = Node(v=1)
    n2 = Node(v=2)
    n3 = Node(v=3)
    ll.insert(afterNode=None, newNode=n1)
    ll.insert(afterNode=n1, newNode=n2)
    ll.insert(afterNode=n1, newNode=n3)
    assert ll.head == n1
    assert ll.tail == n2
    assert n1.next == n3
    assert n3.next == n2


def test_clean():
    ll = LinkedList()
    n1 = Node(v=1)
    ll.add_in_tail(n1)
    ll.clean()

    assert ll.len() == 0
    assert ll.head is None
    assert ll.tail is None

    ll = LinkedList()
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


def test_delete_from_empty():
    ll = LinkedList()
    ll.delete(val=1, all=False)
    assert ll.len() == 0


def test_delete_from_head():
    ll = LinkedList()
    n1 = Node(v=1)
    n2 = Node(v=2)
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.delete(val=1, all=False)
    assert ll.head == n2
    assert ll.tail == n2
    assert n2.next is None
    assert ll.len() == 1


def test_delete_from_tail():
    ll = LinkedList()
    n1 = Node(v=1)
    n2 = Node(v=2)
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.delete(val=2, all=False)
    assert ll.head == n1
    assert ll.tail == n1
    assert n1.next is None
    assert ll.len() == 1


def test_delete_from_head_tail():
    ll = LinkedList()
    n1 = Node(v=1)
    ll.add_in_tail(n1)
    ll.delete(val=1, all=False)
    assert ll.head is None
    assert ll.tail is None
    assert ll.len() == 0


def test_delete_from_between():
    ll = LinkedList()
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
    ll = LinkedList()
    n1 = Node(v=1)
    n2 = Node(v=1)
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.delete(1, all=True)
    assert ll.len() == 0


def test_delete_all_in_between():
    ll = LinkedList()
    ll.add_in_tail(Node(v=1))
    ll.add_in_tail(Node(v=1))
    ll.add_in_tail(Node(v=2))
    ll.add_in_tail(Node(v=2))
    ll.add_in_tail(Node(v=1))
    ll.add_in_tail(Node(v=1))
    ll.delete(2, all=True)
    assert ll.len() == 4

    ll = LinkedList()
    ll.add_in_tail(Node(v=1))
    ll.add_in_tail(Node(v=1))
    ll.add_in_tail(Node(v=2))
    ll.add_in_tail(Node(v=3))
    ll.add_in_tail(Node(v=1))
    ll.add_in_tail(Node(v=1))
    ll.delete(1, all=True)
    assert ll.len() == 2


def test_find_all():
    ll = LinkedList()
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


def test_len_empty():
    ll = LinkedList()
    assert ll.len() == 0


def test_len_non_empty():
    ll = LinkedList()
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
