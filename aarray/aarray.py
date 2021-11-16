class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        res = 0
        for v in key:
            res += ord(v)
        return res % self.size

    def is_key(self, key):
        return self.slots[self.hash_fun(key)] is not None

    def put(self, key, value):
        slot = self.hash_fun(key)
        self.slots[slot] = key
        self.values[slot] = value

    def get(self, key):
        if not self.is_key(key):
            return None
        else:
            return self.values[self.hash_fun(key)]
