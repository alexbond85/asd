class Deque:
    def __init__(self):
        self.arr = []

    def addFront(self, item):
        self.arr.insert(0, item)

    def addTail(self, item):
        self.arr.append(item)

    def removeFront(self):
        if self.size() == 0:
            return None
        return self.arr.pop(0)

    def removeTail(self):
        if self.size() == 0:
            return None
        return self.arr.pop()

    def size(self):
        return len(self.arr)
