from stack_and_queue import __version__
from stack_and_queue.stack_and_queue import (Stack, Queue, Pseudo_queue)
from stack_and_queue.animal_shelter.Animal_shelter import AnimalShelter, Dog, Cat


def test_version():
    assert __version__ == '0.1.0'


# Can successfully push onto a stack
def test_push():
    stack = Stack()
    stack.push(22)
    excepted = stack.top.value
    assert excepted == 22


# Can successfully push multiple values onto a stack
def test_push2():
    stack = Stack()
    stack.push(22)
    stack.push(1)
    excepted = stack.top.value
    assert excepted == 1


# Can successfully pop off the stack
def test_pop():
    stack = Stack()
    stack.push(22)
    stack.push(1)
    actual = stack.pop()
    expected = 1
    assert actual == expected


# Can successfully empty a stack after multiple pops
def test_pop2():
    stack = Stack()
    stack.push(1)
    stack.push(20)
    stack.pop()
    stack.pop()
    actual = stack.top
    expected = None
    assert actual == expected


# Can successfully peek the next item on the stack
def test_peek():
    stack = Stack()
    stack.push(7)
    stack.push(5)
    expected = 5
    actual = stack.peek()
    assert actual == expected


# Can successfully instantiate an empty stack
def test_init_empty():
    stack = Stack()
    expected = None
    assert expected == stack.top


# Calling pop or peek on empty stack raises exception
def test_raise_stack():
    stack = Stack()
    expected = "This is empty stack"
    assert expected == stack.peek()


# Can successfully enqueue into a queue
def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    actual = queue.front.value
    expected = 1
    assert expected == actual


# Can successfully enqueue multiple values into a queue
def test_enqueue2():
    queue = Queue()
    queue.enqueue('niveen')
    queue.enqueue('nivee')
    actual = queue.front.next.value
    expected = 'nivee'
    assert expected == actual


# Can successfully dequeue out of a queue the expected value
def test_dequeue():
    queue = Queue()
    queue.enqueue(3)
    queue.enqueue(100)
    queue.dequeue()
    actual = queue.front.value
    expected = 100
    assert expected == actual


# Can successfully peek into a queue, seeing the expected value
def test_peek_dedueue():
    queue = Queue()
    queue.enqueue(51)
    queue.enqueue(11)
    expected = 51
    actual = queue.peek()
    assert actual == expected


# Can successfully empty a queue after multiple dequeues
def test_empty_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(20)
    queue.dequeue()
    queue.dequeue()
    actual = queue.front
    expected = None
    assert actual == expected


# Can successfully instantiate an empty queue
def test_init_empty_queue():
    queue = Queue()
    expected = None
    assert expected == queue.front


# Calling dequeue or peek on empty queue raises exception
def test_raise_queue():
    queue = Queue()
    expected = "This is Empty queue"
    assert expected == queue.peek()


def test_raise_queuea():
    pseudo = Pseudo_queue()
    pseudo.enqueue('3')
    pseudo.enqueue('4')
    pseudo.dequeue()
    expected = '4'
    actual = pseudo.rear
    assert expected == actual


def test_animal():
    shelter = AnimalShelter()
    ginger = Cat('ginger')
    shelter.enqueue(ginger)
    expected = 'ginger'
    actual = shelter.cat.front.value
    assert expected == actual


def test_animal2():
    shelter = AnimalShelter()
    pop = Dog('pop')
    shelter.enqueue(pop)
    expected = 'pop'
    actual = shelter.dog.front.value
    assert expected == actual


def test_animal2():
    shelter = AnimalShelter()
    pop = Dog('pop')
    shelter.enqueue(pop)
    shelter.dequeue('dog')
    expected = None
    actual = shelter.dog.front
