class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new = Node(value)
            cur = self.head
            new.next = cur
            self.head = new

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new = Node(value)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new

    # def insert_after(self,value,newvalue):
    #     cur = self.head
    #     while cur

    def __str__(self) -> str:
        cur = self.head
        string = ''
        while cur is not None:
            string += str(cur.value)
            cur = cur.next
        return string


ll = LinkedList()
ll.insert(1)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.append(1)
ll.append(8)
ll.append(7)
ll.append(6)


print(ll)
