from linked_list import __version__
from linked_list.linked_list import Linkedlist
from linked_list.zipLists import zipLists


def test_version():
    assert __version__ == '0.1.0'


def test_instantiate():
    List = Linkedlist()
    actual = List.head
    expected = None
    assert actual == expected


def test_insert():
    List = Linkedlist()
    List.insert(6)
    actual = List.head.value
    expected = 6
    assert actual == expected


def test_head():
    List = Linkedlist()
    List.insert(10)
    assert List.head.value == 10


def test_find_value():
    List = Linkedlist()
    List.insert(1)
    List.append(5)
    List.append(10)
    assert List.includes(10) == True


def test_find_notExist_value():
    List = Linkedlist()
    List.insert(1)
    List.append(5)
    List.append(10)
    assert List.includes(4) == False


def test_str():
    List = Linkedlist()
    List.insert(1)
    List.append(2)
    List.append(3)
    assert List.__str__() == '{1}-> {2}-> {3}-> NULL'


def lists():
    List = Linkedlist()
    List.insert(1)
    List.append(2)
    List.append(3)
    List.append(4)
    List.append(5)
    List.append(6)
    List.append(7)
    List.append(8)
    List.append(9)
    List.append(10)
    return List


def test_inseartBefor():
    List = lists()
    List.insert_before(1, 13)
    List.insert_before(2, 22)
    List.insert_before(3, 42)
    List.insert_before(6, 18)
    actual = List.__str__()
    expected = '{13}-> {1}-> {22}-> {2}-> {42}-> {3}-> {4}-> {5}-> {18}-> {6}-> {7}-> {8}-> {9}-> {10}-> NULL'
    assert actual == expected


def test_insert_node_before_the_first_node():
    lnk_lst = Linkedlist()
    lnk_lst.insert(13)
    lnk_lst.append(23)
    lnk_lst.insert_before(13, 3)
    excepted = '{3}-> {13}-> {23}-> NULL'
    actual = lnk_lst.__str__()
    assert excepted == actual


def test_inseartAfter():
    List = lists()
    List.insertAfter(2, 22)
    List.insertAfter(3, 42)
    List.insertAfter(6, 72)
    actual = List.__str__()
    expected = '{1}-> {2}-> {22}-> {3}-> {42}-> {4}-> {5}-> {6}-> {72}-> {7}-> {8}-> {9}-> {10}-> NULL'
    assert actual == expected


def test_insert_node_after_the_last_node():
    List = lists()
    List.insertAfter(1, 13)
    List.insertAfter(2, 22)
    List.insertAfter(3, 42)
    List.insertAfter(6, 72)
    List.insertAfter(10, 93)
    actual = List.__str__()
    expected = '{1}-> {13}-> {2}-> {22}-> {3}-> {42}-> {4}-> {5}-> {6}-> {72}-> {7}-> {8}-> {9}-> {10}-> {93}-> NULL'
    assert actual == expected


def test_append():
    actual = ''
    List = Linkedlist()
    List.insert(18)
    List.append(6)
    List.append(3)
    List.append(15)
    List.append(16)
    while List.head:
        actual += f'{List.head.value},'
        List.head = List.head.next
    expected = '18,6,3,15,16,'
    assert actual == expected


def test_k_greater_than_L_list_length():
    lnk_lst = Linkedlist()
    lnk_lst.append(8)
    lnk_lst.append(3)
    lnk_lst.insertAfter(8, 'a')
    excepted = 'Error! index out of range'
    actual = lnk_lst.kthFromEnd(4)
    assert excepted == actual


def test_k_and_length_of_list_the_same():
    lnk_lst = Linkedlist()
    lnk_lst.append(8)
    lnk_lst.append(3)
    lnk_lst.insertAfter(8, 'a')
    excepted = 'Error! index out of range'
    actual = lnk_lst.kthFromEnd(3)
    assert excepted == actual


def test_k_not_positive_integer():
    lnk_lst = Linkedlist()
    lnk_lst.append(8)
    lnk_lst.append(3)
    lnk_lst.insertAfter(8, 'a')
    excepted = "Error! k can't be negative number"
    actual = lnk_lst.kthFromEnd(-3)
    assert excepted == actual


def test_linked_list_of_size_1():
    lnk_lst = Linkedlist()
    lnk_lst.append(8)
    excepted = 8
    actual = lnk_lst.kthFromEnd(0)
    assert excepted == actual


def test_happy_path():
    lnk_lst = Linkedlist()
    lnk_lst.append(8)
    lnk_lst.append(3)
    lnk_lst.insertAfter(8, 'a')
    excepted = 'a'
    actual = lnk_lst.kthFromEnd(1)
    assert excepted == actual


def test_ll_zip_l1_less_than_l2():
    lnk_lst1 = Linkedlist()
    lnk_lst1.append(8)
    lnk_lst1.append(3)

    lnk_lst2 = Linkedlist()
    lnk_lst2.append(4)
    lnk_lst2.append(7)
    lnk_lst2.append(5)
    lnk_lst2.append(6)

    actual = zipLists(lnk_lst1, lnk_lst2)
    expected = 'head -> {8} -> {4} -> {3} -> {7} -> {5} -> {6} -> NULL'
    assert expected == actual


def test_ll_zip_l1_greater_than_l2():
    lnk_lst1 = Linkedlist()
    lnk_lst1.append(8)
    lnk_lst1.append(3)
    lnk_lst1.append(5)
    lnk_lst1.append(6)

    lnk_lst2 = Linkedlist()
    lnk_lst2.append(4)
    lnk_lst2.append(7)

    actual = zipLists(lnk_lst1, lnk_lst2)
    expected = 'head -> {8} -> {4} -> {3} -> {7} -> {5} -> {6} -> NULL'
    assert expected == actual


def test_ll_zip_l1_equal_l2():
    lnk_lst1 = Linkedlist()
    lnk_lst1.append(8)
    lnk_lst1.append(3)

    lnk_lst2 = Linkedlist()
    lnk_lst2.append(4)
    lnk_lst2.append(7)

    actual = zipLists(lnk_lst1, lnk_lst2)
    expected = 'head -> {8} -> {4} -> {3} -> {7} -> NULL'
    assert expected == actual


def test_ll_zip_l1_empty():
    lnk_lst1 = Linkedlist()

    lnk_lst2 = Linkedlist()
    lnk_lst2.append(4)
    lnk_lst2.append(7)
    actual = zipLists(lnk_lst1, lnk_lst2)
    expected = 'head -> {4} -> {7} -> NULL'
    assert expected == actual


def test_ll_zip_l2_empty():
    lnk_lst1 = Linkedlist()
    lnk_lst1.append(8)
    lnk_lst1.append(3)

    lnk_lst2 = Linkedlist()

    actual = zipLists(lnk_lst1, lnk_lst2)
    expected = 'head -> {8} -> {3} -> NULL'
    assert expected == actual
