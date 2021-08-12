class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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


class Dog:
    def __init__(self, name):
        self.kind = "dog"
        self.name = name
        self.next = None


class Cat:
    def __init__(self, name):
        self.kind = "cat"
        self.name = name
        self.next = None


class AnimalShelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self, animal):
        if animal.kind == 'dog':
            self.dog.enqueue(animal.name)

        elif animal.kind == 'cat':
            self.cat.enqueue(animal.name)

    def dequeue(self, pref):

        if pref == "cat":
            self.cat.dequeue()

        elif pref == "dog":
            self.dog.dequeue()

        else:
            return 'Null'


shelter = AnimalShelter()
ginger = Cat('ginger')
shelter.enqueue(ginger)
shelter.dequeue('cat')

print(shelter.cat.front)
