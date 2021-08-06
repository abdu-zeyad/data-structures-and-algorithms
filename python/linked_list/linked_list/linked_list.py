class Node :
    def __init__(self,value):
        self.value=value
        self.next=None


class Linked_list:
    def __init__(self,head=None):

        self.head=head


    def insert(self,value):

        # creating a new node in front of the Linked List
        new_node=Node(value)

        # node that comes next will become the head
        if self.head:
            new_node.next=self.head

        #Assign new_node to self.head
        self.head = new_node

    def includes(self, value):
        # define the head, which is the current variable
        # Return T/F if value is in the linked list or not

        current = self.head

        while (current) :
            if current.value == value:
                return True
            current = current.next
        return False

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
    print(linked_list)