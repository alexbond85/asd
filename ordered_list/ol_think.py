class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc: bool):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        res = 0
        if v1 < v2:
            res = -1
        if v1 > v2:
            res = 1
        return res

    def _add_ascending(self, value, previous_node, current_node: Node):
        if previous_node is None:
            if self.compare(value, current_node.value) <= 0:
                n = Node(value)
                n.next = self.head
                self.head.prev = n
                self.head = n
                return
            else:
                return self._add_ascending(value, self.head, self.head.next)
        if current_node is None:
            n = Node(value)
            previous_node.next = n
            n.prev = previous_node
            self.tail = n
            return
        if self.compare(previous_node.value, value) <= 0 and self.compare(value, current_node.value) <= 0:
            n = Node(value)
            previous_node.next = n
            n.prev = previous_node
            n.next = current_node
            current_node.prev = n
        else:
            return self._add_ascending(value, current_node, current_node.next)

    def _add_descending(self, value, previous_node, current_node):
        if current_node is None:
            if self.compare(previous_node.value, value) >= 0:
                n = Node(value)
                previous_node.next = n
                n.prev = previous_node
                self.tail = n
                return
            else:
                return self._add_descending(value, self.tail.prev, self.tail)
        if previous_node is None:
            n = Node(value)
            self.head = n
            current_node.prev = n
            n.next = current_node
            return
        if self.compare(value, previous_node.value) <= 0 and self.compare(current_node.value, value) <= 0:
            n = Node(value)
            current_node.prev = n
            previous_node.next = n
            n.next = current_node
            n.prev = previous_node
        else:
            return self._add_descending(value, previous_node.prev, previous_node)

    def add(self, value):
        if self.tail is None:
            n = Node(value)
            self.head = n
            self.tail = n
            return
        if self.__ascending:
            self._add_ascending(value, None, self.head)
        else:
            self._add_descending(value, self.tail, None)

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            if val < node.value and self.__ascending:
                return None
            if val > node.value and not self.__ascending:
                return None
            node = node.next
        return None  # здесь будет ваш код

    def delete(self, val):
        is_empty = self.head is None
        if is_empty:
            return False
        if self.head.value == val:
            h: Node = self.head
            self.head = h.next
            h.next = None
            h.prev = None
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            return
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
                return
            node = node.next

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        counter = 0
        node = self.head
        while node is not None:
            counter += 1
            node = node.next
        return counter

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = str(v1).strip()
        v2 = str(v2).strip()
        if v1 == v2:
            return 0
        if v1 > v2:
            return 1
        else:
            return -1
