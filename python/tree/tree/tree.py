class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = Node(root)

    def print_tree(self, trav_type):
        if trav_type == "pre_order":
            return self.pre_order(self.root, "")
        elif trav_type == "in_order":
            return self.post_order(self.root, "")
        elif trav_type == "post_order":
            return self.in_order(self.root, "")

    def pre_order(self, start, trav):
        if start:
            trav += (str(start.value) + "-")
            trav = self.pre_order(start.left, trav)
            trav = self.pre_order(start.right, trav)

        return trav

    def in_order(self, start, trav):
        if start:
            trav = self.in_order(start.left, trav)
            trav += (str(start.value) + "-")
            trav = self.in_order(start.right, trav)
        return trav

    def post_order(self, start, trav):
        if start:
            trav = self.post_order(start.left, trav)
            trav = self.post_order(start.right, trav)
            trav += (str(start.value) + "-")
        return trav

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


class BinarySearchTree:
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
    bt = BinaryTree()
    bt.root.value = 4
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)

    print(bt.print_tree("pre_order"))
    print(bt.print_tree("post_order"))
    print(bt.print_tree("in_order"))
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(4)
    bst.add(6)
    bst.contains(5)
    print(bst.contains(5))
