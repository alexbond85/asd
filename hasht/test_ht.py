from ht import HashTable


def test_hash_fun():
    ht = HashTable(sz=1, stp=1)
    assert ht.hash_fun("1") == 0
    assert ht.hash_fun("2") == 0
    ht = HashTable(sz=2, stp=1)
    assert ht.hash_fun("a") == 1
    assert ht.hash_fun("b") == 0
    ht = HashTable(sz=3, stp=1)
    assert ht.hash_fun("a") == 1
    assert ht.hash_fun("b") == 2
    assert ht.hash_fun("c") == 0


def test_seek_slot_not_none():
    ht = HashTable(sz=1, stp=1)
    assert ht.seek_slot("1") == 0
    ht.put("1")
    assert ht.seek_slot("1") == 0
    assert ht.find("1") == 0
    assert ht.find("2") is None


def test_put():
    ht = HashTable(sz=1, stp=1)
    assert ht.put("a") == 0
    assert ht.put("a") == 0
    assert ht.put("b") is None
    ht = HashTable(sz=2, stp=1)
    assert ht.put("a") == 1
    assert ht.put("b") == 0
    ht = HashTable(sz=3, stp=1)
    assert ht.put("a") == 1
    assert ht.put("b") == 2
    assert ht.put("c") == 0
    ht = HashTable(sz=3, stp=2)
    assert ht.put("a") == 1
    assert ht.put("y") == 0
    assert ht.put("f") == 2
    ht = HashTable(sz=3, stp=1)
    assert ht.put("a") == 1
    assert ht.put("y") == 2
    assert ht.put("f") == 0
    ht = HashTable(sz=11, stp=2)
    for x in "qazwsxedcrf" + "vtgbyhnujjm":
        ht.put(x)
    slots = ht.slots
    for x in "qazwsxedcrf" + "vtgbyhnujjm":
        slot = ht.find(x)
        if x in "vtgbyhnujjm":
            assert slot is None
        if x not in "vtgbyhnujjm":
            assert slot is not None
            assert slots[slot] == x




