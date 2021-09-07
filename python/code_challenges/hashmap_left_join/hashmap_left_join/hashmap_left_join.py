from python.code_challenges.hashtable.hashtable.hash_table import Hashtable


def left_join(ht1, ht2):
    array2 = []
    array1 = []
    for i in ht2.array:
        if i:
            array2.append(i.head.value)

    for i in ht1.array:
        if i:
            array1.append(i.head.value)

    print(array2)
    print(array1)
    for i in array1:
        for j in array2:
            if i[0] == j[0]:
                j.append(i[1])
    return array2


ht1 = Hashtable()
ht1.add("abd", 10)
ht1.add("ahmad", 12)
ht1.add("hasan", 18)
ht1.add("dab", 20)

ht2 = Hashtable()
ht2.add("khaled", 10)
ht2.add("asx", 12)
ht2.add("hasan", 18)
ht2.add("hasan", 20)

array = left_join(ht1, ht2)
print(array)


# //////////////////////////////////////////
