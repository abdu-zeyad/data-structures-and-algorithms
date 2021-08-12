class Node:
    def __init__(self, value=None):
        self.left_child = None
        self.right_child = None
        self.value = value


class Binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self._insert(value, cur_node.left_node)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print('value already in the tree')


binary_tree = Binary_search_tree()
binary_tree.insert(5)
binary_tree.insert(8)
print(binary_tree.root.value)
print(binary_tree.root.right_child.value)
