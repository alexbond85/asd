from pset import PowerSet


def test_put():
    p = PowerSet()
    p.put(2)
    assert p.size() == 1
    p.put(2)
    assert p.size() == 1
    assert p.get(2)
    assert not p.get(1)
    assert p.remove(2)
    assert not p.get(2)


def test_intersection():
    p1 = PowerSet()
    p2 = PowerSet()
    assert p1.intersection(p2).size() == 0
    p1 = PowerSet()
    p2 = PowerSet()
    p1.put(1)
    p2.put(2)
    assert p1.intersection(p2).size() == 0
    p1.put(2)
    assert p1.intersection(p2).size() == 1
    assert p1.intersection(p2).get(2)


def test_union():
    p1 = PowerSet()
    p2 = PowerSet()
    p2.put(1)
    p3 = p1.union(p2)
    assert p3.size() == 1
    p1 = PowerSet()
    p2 = PowerSet()
    p2.put(1)
    p1.put(1)
    p3 = p1.union(p2)
    assert p3.size() == 1
    p1 = PowerSet()
    p2 = PowerSet()
    p2.put(2)
    p1.put(1)
    p3 = p1.union(p2)
    assert p3.size() == 2


def test_diff():
    p1 = PowerSet()
    p2 = PowerSet()
    p3 = p1.difference(p2)
    assert p3.size() == 0
    p1 = PowerSet()
    p1.put(1)
    p2 = PowerSet()
    p2.put(2)
    p3 = p1.difference(p2)
    assert p3.size() == 1
    assert p3.get(1)
    assert not p3.get(2)
    p1 = PowerSet()
    p2 = PowerSet()
    p1.put(1)
    p2.put(1)
    p3 = p1.difference(p2)
    assert p3.size() == 0


def test_issubset():
    p1 = PowerSet()
    p2 = PowerSet()
    assert p1.issubset(p2)
    p1 = PowerSet()
    p2 = PowerSet()
    p1.put(1)
    p2.put(2)
    assert not p1.issubset(p2)
    p2.put(1)
    assert not p1.issubset(p2)
    p1 = PowerSet()
    p2 = PowerSet()
    p1.put(1)
    p2.put(1)
    assert p1.issubset(p2)
    p1.put(2)
    assert p1.issubset(p2)


def test_stress():
    p1 = PowerSet()
    p2 = PowerSet()
    p3 = PowerSet()
    for i in range(30000):
        p1.put(i)
        if i < 20000:
            p3.put(i)
    for j in range(15, 30015):
        p2.put(j)
    assert p1.intersection(p3).size() == 20000
    assert p1.issubset(p3)
    assert p1.difference(p3).size() == 10000
    assert p1.union(p2).size() == 30015
