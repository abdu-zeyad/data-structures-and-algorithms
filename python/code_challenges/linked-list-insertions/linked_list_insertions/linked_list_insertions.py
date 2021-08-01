class Node :
    def __init__(self,value):
        self.value=value
        self.next=None


class Linked_list:
    def __init__(self,head=None):

        self.head=head


    def insert(self,value):

        new_node=Node(value)

        if self.head:
            new_node.next=self.head

        self.head = new_node

    def includes(self, value):
   

        current = self.head

        while (current) :
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):

        new_node = Node(value)
        current = self.head

        if current == None:
           current = new_node
        else:
            while current.next != None:
                current = current.next
        current.next = new_node


    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        current = self.head
        if current.value == value:
            new_node.next = current
            current = new_node

        while current.next:
            if current.next.value == value:
                new_node.next = current.next
                current.next = new_node
                break
            else:
                current = current.next

    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        current = self.head
        while current:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def __str__(self):

        string = ''
        current = self.head
        while (current):
            string = string + f"{ { current.value } } -> "
            current = current.next
        else:
            string = string + 'Null'
        return string

if __name__ == "__main__":

    linked_list = Linked_list()
    linked_list.insert(3)
    linked_list.insert(2)
    linked_list.insert(1)
    linked_list.append(11)
    linked_list.insert_before(11,8)
    linked_list.insert_after(11,8)
    print(linked_list)