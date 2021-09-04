from python.code_challenges.hashtable.hashtable.hash_table import Hashtable


def test_hash():
    ht = Hashtable()
    actual = ht.hash('abd')
    excepted = 492
    assert actual == excepted


def test_add():
    ht = Hashtable()
    actual = ht.add('abd', 10).head.value
    excepted = ('abd', 10)
    assert actual == excepted


def test_get():
    ht = Hashtable()
    ht.add('abd', 10)
    actual = ht.get('abd')
    excepted = 10
    assert actual == excepted


def test_contains():
    ht = Hashtable()
    ht.add('abd', 10)
    actual = ht.contains('abd')
    excepted = True
    assert actual == excepted


def test_contains2():
    ht = Hashtable()
    ht.add('abd', 10)
    actual = ht.contains('s')
    excepted = False
    assert actual == excepted
