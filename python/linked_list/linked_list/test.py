class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            cur = self.head
            new = Node(value)
            while cur.next is not None:
                cur = cur.next
            cur.next = new

            # ////////////////
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new = Node(value)
            new.next = self.head
            self.head = new

    def insert_before(self, value, newValue):
        cur = self.head
        while cur.next:
            if cur.next.value == value:
                saved = cur.next
                cur.next = Node(newValue)
                cur.next.next = saved
                return cur.next
            cur = cur.next

    def insert_after(self, value, newValue):
        cur = self.head

        while cur is not None:
            if cur.value == value:
                break
            cur = cur.next

        else:
            new_node = Node(newValue)
            new_node.next = cur.next
            cur.next = new_node

    def kth_from_end(self, k):
        cur = self.head
        length = 1
        while cur.next:
            length += 1
            cur = cur.next
        cur = self.head
        # did nothing but cut count the length
        count = length-k
        for i in range(length):
            if i == count:
                print(cur.value)
                return cur.value
            cur = cur.next

    # def __str__(self) -> str:
    #     data = ''

    #     while self.head:
    #         data += str(self.head.value)
    #         self.head = self.head.next

    #     return data


def zipLists(list1, list2):
    temp = 'head -> '
    current1 = list1.head
    current2 = list2.head
    values = []
    while current1:
        values += [current1.value]
        current1 = current1.next
        if current2:
            values += [current2.value]
            current2 = current2.next

    if current1 == None and current2 != None:
        while current2:
            values += [current2.value]
            current2 = current2.next

    print(values)


ll = Linked_list()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.insert(0)
ll.insert_before(2, 9)
ll.insert_after(3, 9)
# ll.kth_from_end(3)
# print(ll)


ll2 = Linked_list()
ll2.append(1)
ll2.append(5)
ll2.append(8)
ll2.append(2)
# print(ll2)


zipLists(ll, ll2)
