from code_challenges.linked_list.linked_list import __version__
from code_challenges.linked_list.linked_list.linked_list import Linked_list


def test_version():  # test 1
    assert __version__ == '0.1.0'


def test_linkedlist():  # test 2
    assert Linked_list()


def test_insert_1():  # test 3
    linked_list = Linked_list()
    linked_list.insert(6)
    assert linked_list.head.value == 6


def test_str():  # test 4
    ll = Linked_list()
    ll.insert('a')
    ll.insert(4)
    ll.insert(74)
    ll.__str__()
    assert ll.__str__() == "{74} -> {4} -> {'a'} -> Null"

########### for code challange 06: #############
########### linked-list-insertions #############


def test_append():
    linked_list = Linked_list()
    linked_list.insert(7)
    linked_list.insert(4)
    linked_list.append(74)
    linked_list.__str__()
    # actual = str(ll)
    # expected = '{10} -> {6} -> {3} -> {74} -> NULL'
    # assert actual == expected
    assert linked_list.__str__() == "{4} -> {7} -> {74} -> Null"


def test_multiple_append():
    linked_list = Linked_list()
    linked_list.insert(7)
    linked_list.insert(4)
    linked_list.append(74)
    linked_list.append(66)
    linked_list.__str__()
    assert linked_list.__str__() == "{4} -> {7} -> {74} -> {66} -> Null"


def test_insert_before_middle():
    linked_list = Linked_list()
    linked_list.insert(7)
    linked_list.insert(4)
    linked_list.insert(1)
    linked_list.append(74)
    linked_list.append(66)
    linked_list.insert_before(7, 'before middle')
    linked_list.__str__()
    assert linked_list.__str__(
    ) == "{1} -> {4} -> {'before middle'} -> {7} -> {74} -> {66} -> Null"


def test_insert_before_first():
    linked_list = Linked_list()
    linked_list.insert(7)
    linked_list.insert(4)
    linked_list.insert(1)
    linked_list.append(74)
    linked_list.append(66)
    linked_list.insert_before(1, 100)
    linked_list.__str__()
    assert linked_list.__str__(
    ) == "{100} -> {1} -> {4} -> {7} -> {74} -> {66} -> Null"


def test_insert_after_middle():
    linked_list = Linked_list()
    linked_list.insert(7)
    linked_list.insert(4)
    linked_list.insert(1)
    linked_list.append(74)
    linked_list.append(66)
    linked_list.insert_after(7, 'after middle')
    linked_list.__str__()
    assert linked_list.__str__(
    ) == "{1} -> {4} -> {7} -> {'after middle'} -> {74} -> {66} -> Null"


def test_insert_after_end():
    linked_list = Linked_list()
    linked_list.insert(7)
    linked_list.insert(4)
    linked_list.insert(1)
    linked_list.append(74)
    linked_list.append(66)
    linked_list.insert_after(66, 'after end')
    linked_list.__str__()
    assert linked_list.__str__(
    ) == "{1} -> {4} -> {7} -> {74} -> {66} -> {'after end'} -> Null"
