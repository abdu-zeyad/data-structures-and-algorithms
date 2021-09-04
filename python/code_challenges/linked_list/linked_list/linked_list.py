class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list:
    def __init__(self, head=None):

        self.head = head

    def insert(self, value):

        new_node = Node(value)

        if self.head:
            new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current_value = self.head
        while (current_value):
            if current_value.value == value:
                return True
            current_value = current_value.next
        return False

    def append(self, value):

        new_node = Node(value)
        current_value = self.head

        if current_value == None:
            current_value = new_node
        else:
            while current_value.next != None:
                current_value = current_value.next
        current_value.next = new_node

    def insert_before(self, value, new_value):
        node = Node(new_value)
        current_value_node = self.head
        if current_value_node.value == value:
            node.next = self.head
            self.head = node
        else:
            while current_value_node.next:
                if current_value_node.next.value == value:
                    node.next = current_value_node.next
                    current_value_node.next = node
                    break
                current_value_node = current_value_node.next

    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        current_value = self.head
        while current_value:
            if current_value.value == value:
                new_node.next = current_value.next
                current_value.next = new_node
                break
            current_value = current_value.next

    def __str__(self):

        string = ''
        current_value = self.head
        while (current_value):
            string = string + f"{ { current_value.value } } -> "
            current_value = current_value.next
        else:
            string = string + 'Null'
        return string


if __name__ == "__main__":

    linked_list = Linked_list()
    # linked_list.insert(('abd', 10))
    # linked_list.insert(('abd', 12))
    # linked_list.insert(('abd', 10))
    # print(linked_list)
