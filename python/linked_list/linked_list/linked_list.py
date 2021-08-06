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

    def append(self, value):

        new_node = Node(value)
        current = self.head

        if current == None:
           current = new_node
        else:
            while current.next != None:
                current = current.next
        current.next = new_node


    def insert_before(self,value,new_value):
        node = Node(new_value)
        current_node=self.head
        if current_node.value==value:
             node.next = self.head
             self.head = node
        else:
            while current_node.next:
                if current_node.next.value==value:
                    node.next=current_node.next
                    current_node.next=node
                    break
                current_node=current_node.next

    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        current = self.head
        while current:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def kthFromEnd(self,k):
        current = self.head
        if current == None:
            return ("Empty List")

        if k <= -1:
           return("Negative number not acceptable")
        values=[]
        while current:
            values =values+ [current.value]
            current = current.next
        print(values)
        try:

            return values[::-1][k]
        except IndexError:
            return ("out of index")



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

    # linked_list = Linked_list()
    # linked_list.insert(3)
    # linked_list.insert(2)
    # linked_list.insert(1)
    # linked_list.append(11)
    # linked_list.insert_before(11,8)
    # linked_list.insert_after(11,8)
    # linked_list.insert_after(1,8)
    # linked_list.insert_before(1,8)
    # # linked_list.kthFromEnd(2)
    # print(linked_list)
    ll = Linked_list()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    print(ll.kthFromEnd(2))
    print(ll.kthFromEnd(-1))
    print(ll.kthFromEnd(8))
    print(ll.kthFromEnd(4))