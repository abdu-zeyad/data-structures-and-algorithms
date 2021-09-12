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
        while current_value:
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

        string = ""
        current_value = self.head
        while current_value:
            string = string + f"{ { current_value.value } } -> "
            current_value = current_value.next
        else:
            string = string + "Null"
        return string

    def remove_dublciate(self):
        array = []
        temp = self.head
        if not temp:
            return
        while temp:
            if temp.value not in array:
                array.append(temp.value)
            else:
                temp.value = temp.next.value
                temp.next = temp.next.next

            temp = temp.next
        return temp


if __name__ == "__main__":

    linked_list = Linked_list()
    linked_list.insert(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(3)
    linked_list.append(6)
    linked_list.append(7)
    linked_list.append(5)
    linked_list.append(8)
    print(linked_list)
    print(linked_list.remove_dublciate())
    print(linked_list)
