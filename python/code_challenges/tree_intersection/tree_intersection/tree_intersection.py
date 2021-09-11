from python.code_challenges.hashtable.hashtable.hash_table import Hashtable
from python.code_challenges.tree.tree.tree import BinaryTree, Node


def tree_intersection(bt1, bt2):

    intersection = []

    ht = Hashtable()

    def traversal(node):
        if node != None:
            ht.add(f"{node.value}", 0)
            traversal(node.left)
            traversal(node.right)

    traversal(bt1.root)
    for i in bt2.preOrder():
        if ht.contains(f"{i}"):
            intersection.append(i)

    return intersection


if __name__ == "__main__":

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

    array = tree_intersection(bt1, bt2)
    print(array)
