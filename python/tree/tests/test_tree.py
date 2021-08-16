from tree import __version__
from tree.tree import BinaryTree, BinarySearchTree, Node


def test_version():
    assert __version__ == '0.1.0'


def test_empty_tree():
    bt = BinaryTree()
    bt.root.right = Node(5)
    actual = bt.root.right.value
    expected = 5
    assert actual == expected


def test_single_node():
    bt = BinaryTree()
    bt.root.value = 1
    actual = bt.root.value
    excepted = 1
    assert actual == excepted


def test_print_tree_pre_order():
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    actual = bt.print_tree("pre_order")
    excepted = '2-7-2-6-5-11-5-9-4-'
    assert actual == excepted


def test_print_tree_in_order():
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    actual = bt.print_tree("in_order")
    excepted = '2-5-11-6-7-4-9-5-2-'
    assert actual == excepted


def test_print_tree_post_order():
    bt = BinaryTree()
    bt.root = Node(2)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    actual = bt.print_tree("post_order")
    excepted = '2-7-5-6-11-2-5-4-9-'
    assert actual == excepted


def test_print_tree_contain():
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(4)
    bst.add(6)
    actual = bst.contains(5)
    excepted = True
    assert actual == excepted


def test_max_val():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.left = Node(11)
    tree.root.right = Node(15)

    actual = tree.max()
    expected = 15
    assert actual == expected
