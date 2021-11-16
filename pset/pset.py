class PowerSet:

    def __init__(self):
        self.storage = {}

    def size(self):
        return len(self.storage)

    def put(self, value) -> None:
        self.storage[value] = value

    def get(self, value) -> bool:
        return self.storage.get(value, None) is not None

    def remove(self, value) -> bool:
        if self.get(value):
            self.storage.pop(value)
            return True
        return False

    def intersection(self, set2):
        s = self.storage
        st = {s: s for s in s.keys() if set2.storage.get(s, None) is not None}
        p = PowerSet()
        p.storage = st
        return p

    def union(self, set2):
        s = self.storage.copy()
        s.update(set2.storage)
        p = PowerSet()
        p.storage = s
        return p

    def difference(self, set2):
        s = self.storage
        st = {s: s for s in s.keys() if set2.storage.get(s, None) is None}
        p = PowerSet()
        p.storage = st
        return p

    def issubset(self, set2):
        for x in set2.storage.keys():
            if self.storage.get(x, None) is None:
                return False
        return True

