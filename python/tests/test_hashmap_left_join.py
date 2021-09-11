from python.code_challenges.hashmap_left_join.hashmap_left_join.hashmap_left_join import (
    left_join,
    Hashtable,
)


def test_left():
    ht1 = Hashtable()
    ht1.add("abd", 10)
    ht1.add("ahmad", 12)
    ht1.add("hasan", 18)
    ht1.add("dab", 20)

    ht2 = Hashtable()
    ht2.add("abd", 10)
    ht2.add("asx", 12)
    ht2.add("ahmad", 18)
    ht2.add("hasan", 20)
    actual = left_join(ht1, ht2)
    expected = [["hasan", 20, 18], ["ahmad", 18, 12], ["abd", 10], ["asx", 12]]
    assert actual == expected


def test_left():
    ht1 = Hashtable()
    ht1.add("abd", 10)
    ht1.add("ahmad", 12)
    ht1.add("hasan", 18)
    ht1.add("dab", 20)

    ht2 = Hashtable()
    ht2.add("khaled", 10)
    ht2.add("asx", 12)
    ht2.add("hasan", 18)
    ht2.add("hasan", 20)
    actual = left_join(ht1, ht2)
    expected = [["hasan", 20, 18], ["khaled", 10], ["asx", 12]]
    assert actual == expected
