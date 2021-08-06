class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list:
    def __init__(self, head=None):

        self.head = head

    def insert(self, value):
        # take the value main and excute it in node
        new_node = Node(value)
        #  define the node value and the next value
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def includes(self, value):

        current_node = self.head

        while (current_node):
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def __str__(self):

        string = ''
        current_node = self.head
        while (current_node):
            string = string + f"{ { current_node.value } } -> "
            current_node = current_node.next
        else:
            string = string + 'Null'
        return string


if __name__ == "__main__":

    linked_list = Linked_list()
    linked_list.insert('c')
    linked_list.insert('b')
    linked_list.insert('a')
    print(linked_list)
