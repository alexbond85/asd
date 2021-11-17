class BloomFilter2:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_array = [0] * f_len

    def _hash_parametrized(self, str1, param: int):
        res1 = 0  # 17
        for c in str1:
            code = ord(c)
            res1 = ((res1 * param) + code) % self.filter_len
        return res1

    def hash1(self, str1):
        return self._hash_parametrized(str1, 17)

    def hash2(self, str1):
        return self._hash_parametrized(str1, 223)

    def add(self, str1):
        self.bit_array[self.hash1(str1)] = 1
        self.bit_array[self.hash2(str1)] = 1

    def is_value(self, str1):
        return self.bit_array[self.hash1(str1)] == 1 and self.bit_array[self.hash2(str1)] == 1
