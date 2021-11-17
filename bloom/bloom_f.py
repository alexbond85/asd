class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_array = 1 << f_len

    def _hash_parametrized(self, str1, param: int):
        res = 0
        zeros_mask = 1 << self.filter_len
        for c in str1:
            code = ord(c)
            res = ((res * param) + code) % self.filter_len
        res = res + 1
        res = (1 << (self.filter_len - res) | zeros_mask)
        return res

    def hash1(self, str1):
        return self._hash_parametrized(str1, 17)

    def hash2(self, str1):
        return self._hash_parametrized(str1, 223)

    def add(self, str1):
        self.bit_array = self.bit_array | self.hash1(str1) | self.hash2(str1)

    def is_value(self, str1):
        elem = self.hash1(str1) | self.hash2(str1)
        return elem & self.bit_array == elem
