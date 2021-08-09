class Node:
    def __init__(self, value):

        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        try:
            popped = self.top
            self.top = self.top.next
            self.size -= 1
            return popped.value
        except:
            return "The Stack is empty"

    def peek(self):
        try:
            return self.top.value
        except:
            return "The Stack is empty"

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False


class Queue:

    def __init__(self):
        self.front = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if self.front == None:
            self.front = node
        else:
            current = self.front
            while current.next != None:
                current = current.next
            current.next = node
            current = current.next
        self.size += 1

# x= (1,None)
# newnode = (2.none)
# x.next = newnode
# x = x.next

    def dequeue(self):
        try:
            removed = self.front
            self.front = self.front.next
            self.size -= 1
            return removed.value
        except:
            return "The Queue is empty"

    def peek(self):
        try:
            return self.front.value
        except:
            return "The Queue is empty"

    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False

    def printS(self):
        print(self.front.next.value)


class PseudoQueue():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, val):
        self.stack1.push(val)

    def dequeue(self):
        while range(0, self.stack1.size):
            self.stack2.push(self.stack1.pop())

        popped = self.stack2.pop()

        while range(0, self.stack2.size):
            self.stack1.push(self.stack2.pop())

        return popped


if __name__ == "__main__":
    q = PseudoQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    x = q.dequeue()
    print(x)
    y = q.dequeue()
    print(y)
    z = q.dequeue()
    print(z)
    n = q.dequeue()
    print(n)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(6)

    queue.printS()
