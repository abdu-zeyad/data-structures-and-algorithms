from linked_list import __version__
import linked_list

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
    linked_list.insert_before(7,'before middle')
    linked_list.__str__()
    assert linked_list.__str__() == "{1} -> {4} -> {'before middle'} -> {7} -> {74} -> {66} -> Null"

def test_insert_before_first():
    linked_list = Linked_list()
    linked_list.insert(7)
    linked_list.insert(4)
    linked_list.insert(1)
    linked_list.append(74)
    linked_list.append(66)
    linked_list.insert_before(1,100)
    linked_list.__str__()
    assert linked_list.__str__() == "{100} -> {1} -> {4} -> {7} -> {74} -> {66} -> Null"


def test_insert_after_middle():
    linked_list = Linked_list()
    linked_list.insert(7)
    linked_list.insert(4)
    linked_list.insert(1)
    linked_list.append(74)
    linked_list.append(66)
    linked_list.insert_after(7,'after middle')
    linked_list.__str__()
    assert linked_list.__str__() == "{1} -> {4} -> {7} -> {'after middle'} -> {74} -> {66} -> Null"


def test_insert_after_end():
    linked_list = Linked_list()
    linked_list.insert(7)
    linked_list.insert(4)
    linked_list.insert(1)
    linked_list.append(74)
    linked_list.append(66)
    linked_list.insert_after(66,'after end')
    linked_list.__str__()
    assert linked_list.__str__() == "{1} -> {4} -> {7} -> {74} -> {66} -> {'after end'} -> Null"

######################################## code07

def test_k_greater():
    ll = Linked_list()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    actual = ll.kthFromEnd(10)
    excepted = 'out of index'
    assert actual == excepted

def test_k_same_length():
    ll = Linked_list()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    actual = ll.kthFromEnd(10)
    excepted = 'out of index'
    assert actual == excepted

def test_k__not_positive_int():
    ll = Linked_list()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    actual = ll.kthFromEnd(-1)
    assert actual == 'Negative number not acceptable'

def test_with_size_1_1():
    ll = Linked_list()
    ll.insert(1)
    actual = ll.kthFromEnd(0)
    excepted = 1
    assert actual == excepted

def test_happy_path():
    ll = Linked_list()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    actual = ll.kthFromEnd(2)
    excepted = 3
    assert actual == excepted

def test_zip_one():
    ll_one = Linked_list()
    ll_one.insert(1)
    ll_one.insert(5)
    ll_one.insert(7)
    ll_one.insert(9)

    ll_two = Linked_list()
    ll_two.insert('a')
    ll_two.insert('b')
    ll_two.insert('c')
    ll_two.insert('d')
    actual =Linked_list.zipLists(ll_one, ll_two)
    excepted = '{ 9 } -> { d } -> { 7 } -> { c } -> { 5 } -> { b } -> { 1 } -> { a } -> Null'
    assert actual == excepted