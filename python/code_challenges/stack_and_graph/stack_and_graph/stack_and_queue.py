class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

    def pop(self):
        try:
            deleted_value = self.top.value
            temp = self.top.next
            self.top = temp
            temp.next = None
            return deleted_value
        except:
            return "This is empty stack"

    def peek(self):
        try:
            return self.top.value
        except:
            return "This is empty stack"

    def isEmpty(self):
        if self.top == None:
            return False
        else:
            return True


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, value):
        node = Node(value)
        if self.front == None:
            self.front = node
            self.rear = node
            self.size += 1
        else:
            self.rear.next = node

            self.rear = node
            self.size += 1

    def dequeue(self):
        try:
            removed = self.front.value
            self.front = self.front.next
            self.size -= 1
            return removed
        except:
            return "The Queue is empty"

    def peek(self):
        try:
            return self.front.value
        except:
            return "This is Empty queue"

    def isEmpty(self):
        if self.front == None and self.rear == None:
            return True
        else:
            return False


if __name__ == "__main__":
    pass
    # q = Queue()
    # q.enqueue(1)

    # print(q.length())
    # print(q.dequeue())
    # q.enqueue(3)
    # q.enqueue(4)
    # q.enqueue(5)
    # q.enqueue(6)
    # print(q.front.value)
    # print(q.front.next.value)
    # print(q.rear.value)
