from aarray import NativeDictionary


def test_hash_fun():
    d = NativeDictionary(3)
    assert d.hash_fun("a") == 1
    d.put("a", 123)
    assert d.hash_fun("d") == 2
    d.put("d", 234)
    d.put("a", 1)
    assert d.get("a") == 1
    assert d.hash_fun("h") == 0
    d.put("h", 345)
    assert d.hash_fun("w") is None
    assert d.is_key("a")
    assert d.is_key("d")
    assert d.is_key("h")
    assert not d.is_key("w")
    print(d.slots)
    print(d.values)


def test_put():
    d = NativeDictionary(3)
    d.put("a", 123)
    assert "a" in d.slots
    assert 123 in d.values
    assert d.is_key("a")
    assert not d.is_key("b")
    assert d.get("a") == 123
    assert d.get("b") is None
    d = NativeDictionary(3)
    d.put("a", 123)
    d.put("b", 456)
    d.put("c", 789)
    print(d.slots)
    print(d.values)
