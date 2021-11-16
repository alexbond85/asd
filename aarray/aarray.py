class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        return self.seek_slot(key)

    def _init_slot(self, key):
        res = 0
        for v in key:
            res += ord(v)
        return res % self.size

    def _next_hash(self, initial_slot):
        return (initial_slot + 1) % self.size

    def seek_slot(self, key):
        initial_slot = self._init_slot(key)
        counter = 1
        while counter <= self.size:
            if self.slots[initial_slot] is None:
                return initial_slot
            if self.slots[initial_slot] == key:
                return initial_slot
            else:
                counter += 1
                initial_slot = self._next_hash(initial_slot)
        return None

    def is_key(self, key):
        slot = self.seek_slot(key)
        if slot is None:
            return False
        else:
            return self.slots[slot] is not None

    def put(self, key, value):
        slot = self.hash_fun(key)
        self.slots[slot] = key
        self.values[slot] = value

    def get(self, key):
        if not self.is_key(key):
            return None
        else:
            return self.values[self.hash_fun(key)]
