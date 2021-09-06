from python.code_challenges.tree.tree.tree import BinaryTree, Node


def tree_intersection(bt1, bt2):
    output = []
    output2 = []
    intersection = []

    def traversal(node):
        if node != None:
            traversal(node.left)
            output.append(node.value)
            traversal(node.right)
    traversal(bt1.root)

    def traversal2(node):
        if node != None:
            traversal2(node.left)
            output2.append(node.value)
            traversal2(node.right)
    traversal2(bt2.root)

    for i in output:
        if i in output2:
            if i not in intersection:
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
