from typing import List, Optional


class Node:

    def __init__(self, v):
        self.value = v
        self.next: Optional["Node"] = None


class LinkedList:

    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val) -> Optional[Node]:
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val) -> List[Node]:
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
        node = self.head
        next_node = self.head.next
        while next_node is not None:
            if next_node.value == val:
                node.next = next_node.next
                next_node.next = None
                if self.tail == next_node:
                    self.tail = node
                return True
            node = next_node
            next_node = node.next
        return False

    def delete(self, val, all=False):
        if not all:
            self._delete_first(val)
        else:
            while self._delete_first(val):
                continue

    def _remove_head(self):
        h = self.head
        self.head = h.next
        h.next = None

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

    def _add_in_head(self, n: Node) -> None:
        is_ll_empty = self.head is None
        if is_ll_empty:
            self.add_in_tail(n)
        else:
            n.next = self.head
            self.head = n

    def insert(self, afterNode: Optional[Node], newNode: Node) -> None:
        add_in_head = afterNode is None
        if add_in_head:
            self._add_in_head(newNode)
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
            is_update_tail = self.tail == afterNode
            if is_update_tail:
                self.tail = newNode
