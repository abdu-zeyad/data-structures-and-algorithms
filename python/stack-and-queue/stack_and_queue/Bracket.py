import re
from stack_and_queue import Stack, Queue


def validate_brackets(in_str):

    checker = Stack()
    st = [*re.findall(r'[\[\]\(\)\{\}]', in_str)]
    print(st)
    opening = ["[", "(", "{"]
    closing = ["]", ")", "}"]

    for x in st:
        y = ""
        if x in opening:
            index = opening.index(x)
            y = closing[index]
        elif x in closing:
            index = closing.index(x)
            y = opening[index]
            #  find the index and the define y as close bracket for it

        if checker.top == None:
            checker.push(x)
        elif y == checker.top.value:
            checker.pop()
        else:
            checker.push(x)

    current = checker.top

    while current != None:
        print("X = ", current.value)
        current = current.next

    if checker.top == None:
        return True
    else:
        return False


s = '[asdasd()]'
x = validate_brackets(s)
print(x)
