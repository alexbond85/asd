from aarray import NativeDictionary


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
