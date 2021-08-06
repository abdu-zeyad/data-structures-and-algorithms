

from linked_list import __version__

from linked_list.linked_list import Linked_list


def test_version():
    assert __version__ == '0.1.0'


def test_linkedlist():
    assert Linked_list()


def test_insert_1():
    linked_list = Linked_list()
    linked_list.insert(4)
    assert linked_list.head.value == 4


def test_str():
    ll = Linked_list()
    ll.insert('zar')
    ll.insert(-4)
    ll.insert(12)
    ll.__str__()
    assert ll.__str__() == "{12} -> {-4} -> {'zar'} -> Null"
