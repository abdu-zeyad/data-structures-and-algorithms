from python.code_challenges.tree_intersection.tree_intersection.tree_intersection import (
    tree_intersection,
    BinaryTree,
    Node,
)


def test_intersection():
    bt1 = BinaryTree()
    bt1.root = Node(3)
    bt1.root.left = Node(11)
    bt1.root.right = Node(5)
    bt1.root.left.left = Node(2)
    bt1.root.left.right = Node(6)
    bt1.root.right.right = Node(9)
    bt1.root.right.left = Node(5)

    bt2 = BinaryTree()
    bt2.root = Node(11)
    bt2.root.left = Node(8)
    bt2.root.right = Node(4)
    bt2.root.left.left = Node(3)
    bt2.root.left.right = Node(9)
    bt2.root.right.right = Node(5)
    bt2.root.right.left = Node(13)
    actual = tree_intersection(bt1, bt2)
    expected = [11, 3, 9, 5]
    assert actual == expected


def test_intersection2():
    bt1 = BinaryTree()
    bt1.root = Node(3)
    bt1.root.left = Node(2)
    bt1.root.right = Node(6)

    bt2 = BinaryTree()
    bt2.root = Node(2)
    bt2.root.left = Node(8)
    bt2.root.right = Node(6)
    bt2.root.left.left = Node(3)

    actual = tree_intersection(bt1, bt2)
    expected = [2, 3, 6]
    assert actual == expected


def test_intersection3():
    bt1 = BinaryTree()
    bt1.root = Node(98)
    bt1.root.left = Node(2)
    bt1.root.right = Node(1)

    bt2 = BinaryTree()
    bt2.root = Node(6)
    bt2.root.left = Node(5)
    bt2.root.right = Node(6)
    bt2.root.left.left = Node(3)

    actual = tree_intersection(bt1, bt2)
    expected = []
    assert actual == expected


def test_intersection4():
    bt1 = BinaryTree()
    bt1.root = Node(3)
    bt1.root.left = Node(2)
    bt1.root.right = Node(6)

    bt2 = BinaryTree()
    bt2.root = Node(2)
    bt2.root.left = Node(8)
    bt2.root.right = Node(-1)
    bt2.root.left.left = Node(3)

    actual = tree_intersection(bt1, bt2)
    expected = [2, 3]
    assert actual == expected
