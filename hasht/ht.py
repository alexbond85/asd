class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        res = 0
        for v in value:
            res += ord(v)
        return res % self.size

    def _next_hash(self, initial_slot):
        return (initial_slot + self.step) % self.size

    def seek_slot(self, value):
        initial_slot = self.hash_fun(value)
        counter = 1
        while counter <= self.size:
            if self.slots[initial_slot] is None:
                return initial_slot
            if self.slots[initial_slot] == value:
                return initial_slot
            else:
                counter += 1
                initial_slot = self._next_hash(initial_slot)
        return None

    def put(self, value):
        slot_number = self.seek_slot(value)
        if slot_number is None:
            return None
        else:
            self.slots[slot_number] = value
            return slot_number

    def find(self, value):
        slot = self.seek_slot(value)
        if slot is None:
            return
        if self.slots[slot] is not None:
            return slot
        return None
