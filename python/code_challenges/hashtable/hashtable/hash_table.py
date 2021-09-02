x = {"abood": 5}
y = {"ahmad": 4}


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


class Hashtable(Linked_list):
    def __init__(self, size=1024, prime=564):
        self.size = size
        self.array = [None] * size
        self.prime = prime

    def add(self, obj):
        key = list(obj.keys())[0]
        value = 0
        for char in key:
            value += ord(char)
        index = (value * self.prime) % (self.size)
        self.array[index] = obj
        self.insert(obj)


obj = {"khaled": 5}
ht = Hashtable()
ht.add(obj)


ll = Linked_list()
ll.insert(obj)
print(ll.head.value)
