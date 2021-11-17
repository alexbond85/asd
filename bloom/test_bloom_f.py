import collections
from bloom_f import BloomFilter
from array_vs_bitarray import BloomFilter2


data = []
d = collections.deque("0123456789")
for i in range(10):
    d.rotate(1)
    data.append("".join(list(d)))

def bitfield(n):
    return [1 if digit == '1' else 0 for digit in bin(n)[2:]]


def test_bloom():
    b1 = BloomFilter(32)
    b2 = BloomFilter2(32)
    for d in data:
        b1.add(d)
        b2.add(d)
        assert b1.is_value(d)
        assert b2.is_value(d)
        assert [1] + b2.bit_array == bitfield(b1.bit_array)
