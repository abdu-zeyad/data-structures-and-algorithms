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

    for i in range(len(values)):
        temp += '{'+f'{values[i]}'+'} '+'-> '
    temp += 'NULL'
    return temp
