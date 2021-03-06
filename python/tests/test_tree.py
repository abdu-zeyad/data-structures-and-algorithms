from code_challenges.tree.tree import __version__
from code_challenges.tree.tree.tree import BinaryTree, BinarySearchTree, Node, fizz_buzz_tree


def test_version():
    assert __version__ == '0.1.0'


def test_empty_tree():
    bt = BinaryTree()
    actual = bt.root
    expected = None
    assert actual == expected


def test_single_node():
    bt = BinaryTree()
    bt.root = Node(1)
    actual = bt.root.value
    excepted = 1
    assert actual == excepted


def test_print_tree_pre_order():
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    actual = bt.preOrder()
    excepted = [1, 7, 2, 6, 5, 11, 5, 9, 4]
    assert actual == excepted


def test_print_tree_in_order():
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    actual = bt.inOrder()
    excepted = [2, 7, 5, 6, 11, 1, 5, 4, 9]
    assert actual == excepted


def test_print_tree_post_order():
    bt = BinaryTree()
    bt.root = Node(1)

    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    actual = bt.postOrder()
    excepted = [2, 5, 11, 6, 7, 4, 9, 5, 1]
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
    tree.root = Node(1)

    tree.root.left = Node(7)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.left = Node(11)
    tree.root.right = Node(15)

    actual = tree.max()
    expected = 15
    assert actual == expected


def test_breadth_first():
    bt = BinaryTree()
    bt.root = Node(1)

    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    actual = bt.breadth_first()
    expected = [1, 2, 4, 5, 3]
    assert actual == expected


def test_fizz_buzz_tree():
    bt = BinaryTree()
    bt.root = Node(1)

    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(15)
    fb = fizz_buzz_tree(bt)
    actual = fb.preOrder()
    expected = ['1', '7', '2', 'Fizz', 'Buzz',
                '11', 'Buzz', 'Fizz', 'FizzBuzz']
    assert actual == expected
