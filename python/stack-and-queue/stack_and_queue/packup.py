import re
from stack_and_queue import Stack, Queue


def validate_brackets(in_str):

    st = [*re.findall(r'[\[\]\(\)\{\}]', in_str)]
    print(st)
    opening = ["[", "(", "{"]
    closing = ["]", ")", "}"]
    for i in range(3):
        x = True
        if st.count(opening[i]) == st.count(closing[i]):
            continue
        else:
            x = False
            break

    print(x)


s = '({[]})'
x = validate_brackets(s)
# print(x)
