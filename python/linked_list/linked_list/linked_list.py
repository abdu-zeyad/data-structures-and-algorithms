class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, value):

        node = Node(value)
        if self.head == None:
            self.head = node
            return self.head.value
        else:
            current = self.head
            self.head = node
            self.head.next = current
            return self.head.value

    def includes(self, value):
        if self.head:
            current = self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False
        else:
            raise Exception(
                "Sorry, this list is empty , so plz insert a value")

    def __str__(self):
        if self.head:
            data_str = ''
            current = self.head
            while current:
                data_str += '{'+str(current.value)+'}-> '
                current = current.next
            data_str += 'NULL'
            return data_str
        else:
            data_str = 'NULL'
            return data_str

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def insert_before(self, val, new_val):
        if self.head == None:
            self.head = Node(val)
        if self.head.value == val:
            self.insert(new_val)
        else:
            try:
                current = self.head
                while current.next:
                    if current.next.value == val:
                        saved_current_val = current.next
                        current.next = Node(new_val)
                        current.next.next = saved_current_val
                        return current.next
                    current = current.next
            except:
                raise Exception(f'{val} is not in linked list')

    def insertAfter(self, value, newVal):

        current = self.head

        while current is not None:
            if current.value == value:
                break
            current = current.next
        if current is None:
            raise Exception(" the value not exisit ")
        else:
            new_node = Node(newVal)
            new_node.next = current.next
            current.next = new_node

    def kthFromEnd(self, k):
        current = self.head
        length = 1
        while current.next:
            length += 1
            current = current.next
        current = self.head
        if k >= length:
            return 'Error! index out of range'
        elif k < 0:
            return "Error! k can't be negative number"
        else:
            count = length-k-1
            for i in range(length):
                if i == count:
                    return current.value
                current = current.next

    def kth(self, j):
        current = self.head
        val = []
        while current:
            val += [current.value]
            current = current.next
        val = val[::-1]

        for i in range(len(val)):
            if i == j:
                return val[j]


if __name__ == "__main__":
    List = Linkedlist()
    List.insert(3)
    List.append(7)
    List.append(13)
    List.append(23)
    print(list)
    y = Linkedlist.kthFromEnd(2, 3)
    print(y)
