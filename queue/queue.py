class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, item):
        self.arr.append(item)

    def dequeue(self):
        if self.size() == 0:
            return 0
        return self.arr.pop(0)

    def size(self):
        return len(self.arr)

    def _rotate(self, n):
        #
        l = self.arr[n:] + self.arr[:n]
        self.arr = l
