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


class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.front == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        try:
            self.front.value
        except:
            return "This is Empty queue"
        else:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value

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


class Pseudo_queue():
    def __init__(self):
        self.first_stack = Stack()
        self.secand_stack = Stack()
        self.rear = None
        self.front = None

    def enqueue(self, value):
        self.first_stack.push(value)
        self.rear = self.first_stack.top.value

    def dequeue(self):
        if self.first_stack.top:
            stack1 = self.first_stack
            while not stack1.isEmpty():
                self.secand_stack.push(stack1.pop())

            poped = self.secand_stack.pop()
            self.front = self.secand_stack.top
            self.first_stack = Stack()
            stack2 = self.secand_stack
            while not stack2.isEmpty():
                self.first_stack.push(stack2.pop())
            return poped

    def __str__(self):
        content = ''
        current = self.first_stack.top
        while current:
            content += f"{{{str(current.value)}}} -> "
            current = current.next
        content += " Null"
        return content


if __name__ == "__main__":
    queue = Pseudo_queue()
    queue.enqueue(5)
    print(queue.__str__())
    queue.enqueue(7)
    print(queue.__str__())
    queue.enqueue(9)
    print(queue.__str__())
    queue.dequeue()
    print(queue.__str__())
    queue.dequeue()
    print(queue.__str__())
    queue.dequeue()
    print(queue.__str__())
