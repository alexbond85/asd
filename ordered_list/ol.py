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

    def _add_ascending(self, n: Node):
        to_insert_value = n.value
        if self.compare(to_insert_value, self.head.value) <= 0:
            self.head.prev = n
            n.next = self.head
            self.head = n
            return
        node = self.head
        while node is not None:
            current_value = node.value
            is_reached_tail = node.next is None
            if is_reached_tail:
                pass
            else:
                node_next: Node = node.next
                next_value = node_next.value
                if (self.compare(current_value, to_insert_value) <=0
                    and self.compare(to_insert_value, next_value) <=0):
                    pass

    def _add_descending(self, n: Node):
        to_insert_value = n.value
        if self.compare(to_insert_value, self.head.value) >= 0:
            self.head.prev = n
            n.next = self.head
            self.head = n

    def add(self, value):
        n = Node(value)
        if self.tail is None:
            self.head = n
            self.tail = n
            return
        if self.__ascending:
            self._add_ascending(n)
        else:
            self._add_descending(n)

    def find(self, val):
        return None  # здесь будет ваш код

    def delete(self, val):
        pass  # здесь будет ваш код

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None
        pass  # здесь будет ваш код

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
        # переопределённая версия для строк
        return 0
