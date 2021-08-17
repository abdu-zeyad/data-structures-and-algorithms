class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value=None):
        if value:
            self.root = Node(value)
        else:
            self.root = None

    def preOrder(self):
        output = []

        def traversal(node):
            if node != None:
                output.append(node.value)
                traversal(node.left)
                traversal(node.right)

        traversal(self.root)
        return output

    def inOrder(self):
        output = []

        def traversal(node):
            if node != None:
                traversal(node.left)
                output.append(node.value)
                traversal(node.right)

        traversal(self.root)
        return output

    def postOrder(self):
        output = []

        def traversal(node):
            if node != None:
                traversal(node.left)
                traversal(node.right)
                output.append(node.value)

        traversal(self.root)
        return output

    def max(self):
        if not self.root:
            return "Tree is Empty"
        self.max = self.root.value

        def tree(node):
            if node.value > self.max:
                self.max = node.value
            if node.left:
                tree(node.left)
            if node.right:
                tree(node.right)
            return self.max

        return tree(self.root)

    def breadth_first(self):
        values = []
        tree = self.root
        values.append(tree.value)
        # print(values)

        def walk(left, right):
            if left is not None:
                values.append(left.value)
                walk(left.left, left.right)

            if right is not None:
                values.append(right.value)
                walk(right.left, right.right)

        walk(tree.left, tree.right)
        return values


def fizz_buzz_tree(bt):
    fb = BinaryTree()

    def walk(node):
        if node != None:
            if node.value % 3 == 0 and node.value % 5 == 0:
                fb_node = Node("FizzBuzz")
            elif node.value % 3 == 0:
                fb_node = Node("Fizz")
            elif node.value % 5 == 0:
                fb_node = Node("Buzz")
            else:
                fb_node = Node(str(node.value))

            if node.left:
                fb_node.left = walk(node.left)
            if node.right:
                fb_node.right = walk(node.right)

            return fb_node

    fb.root = walk(bt.root)

    return fb


class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, cur_node):
        if cur_node.left is not None:
            cur_node.left = Node(value)
        elif cur_node.right is not None:
            cur_node.right = Node(value)

    def contains(self, value):
        if self.root:
            is_found = self._contains(value, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _contains(self, value, cur_node):
        if value > cur_node.value and cur_node.right:
            return self._contains(value, cur_node.right)
        if value < cur_node.value and cur_node.left:
            return self._contains(value, cur_node.left)
        if value == cur_node.value:
            return True


if __name__ == "__main__":
    bt = BinaryTree(1)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(15)
    # print(bt.breadth_first())
    print(bt.postOrder())
    print(bt.preOrder())
    print(bt.inOrder())

    fb = fizz_buzz_tree(bt)
    print(fb.preOrder())

    bst = BinarySearchTree()
    bst.add(5)
    bst.add(4)
    bst.add(6)
    bst.contains(5)
    print(bst.contains(5))
