from c import NativeCache
# proof by picture


def test_remove_least_used():
    n = NativeCache(3)
    n.put("a", 1)
    n.put("b", 2)
    n.put("c", 3)
    n.get("b")
    n.get("c")
    n.put("d", 4)
    assert not n.is_key("a")
