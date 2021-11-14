class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        res = []
        ll = self
        while (n := ll.find(val)) is not None:
            res.append(n)
            ll = self.__class__()
            ll.head = n.next
            ll.tail = self.tail
        return res

    def _delete_first(self, val) -> bool:
        is_empty = self.head is None
        if is_empty:
            return False
        if self.head.value == val:
            self._remove_head()
            is_remove_tail = self.head is None
            if is_remove_tail:
                self.tail = None
            return True
        node = self.head.next
        while node is not None:
            if node.value == val:
                if node == self.tail:
                    self.tail = node.prev
                    node.prev.next = None
                    node.prev = None
                else:
                    pr = node.prev
                    nxt = node.next
                    pr.next = nxt
                    nxt.prev = pr
                    node.next = None
                    node.prev = None
                return True
            node = node.next
        return False


    def delete(self, val, all=False):
        if not all:
            self._delete_first(val)
        else:
            while self._delete_first(val):
                continue

    def _remove_head(self):
        h: Node = self.head
        self.head = h.next
        h.next = None
        h.prev = None

    def clean(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self._remove_head()
            return self.clean()

    def len(self):
        counter = 0
        node = self.head
        while node is not None:
            counter += 1
            node = node.next
        return counter

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)
            return
        if afterNode == self.tail:
            self.add_in_tail(newNode)
        else:
            next_after_node = afterNode.next
            next_after_node.prev = newNode
            newNode.next = next_after_node
            newNode.prev = afterNode
            afterNode.next = newNode

    def add_in_head(self, newNode: Node):
        is_empty = self.head is None
        if is_empty:
            self.add_in_tail(newNode)
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
