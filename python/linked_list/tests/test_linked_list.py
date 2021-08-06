

from linked_list import __version__

from linked_list.linked_list import Linked_list

def test_version(): # test 1
    assert __version__ == '0.1.0'

def test_linkedlist(): # test 2
   assert Linked_list()

def test_insert_1(): # test 3
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