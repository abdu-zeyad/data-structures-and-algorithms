class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.pre_order(self.root, "")
        elif traversal_type == "inorder":
            return self.in_order(self.root, "")
        elif traversal_type == "postorder":
            return self.post_order(self.root, "")

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def pre_order(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.pre_order(start.left, traversal)
            traversal = self.pre_order(start.right, traversal)
        return traversal

    def in_order(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.in_order(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.in_order(start.right, traversal)
        return traversal

    def post_order(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.post_order(start.left, traversal)
            traversal = self.post_order(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal


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
    bt.root = Node(2)
    bt.root.right = Node(5)
    bt.root.left = Node(7)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)

    print(bt.print_tree("preorder"))
    print(bt.print_tree("inorder"))
    print(bt.print_tree("postorder"))
