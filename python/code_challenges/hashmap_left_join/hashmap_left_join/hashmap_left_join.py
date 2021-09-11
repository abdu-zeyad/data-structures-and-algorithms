from python.code_challenges.hashtable.hashtable.hash_table import Hashtable


def left_join(ht1, ht2):
    lj_output = []
    for i in ht1.array:
        if i:
            lj = []
            current_value = i.head
            while current_value:
                lj.append(current_value.value[0])
                lj.append(current_value.value[1])
                if ht2.contains(current_value.value[0]):
                    lj.append(ht2.get(current_value.value[0]))
                else:
                    lj.append(None)
                current_value = current_value.next

            lj_output.append(lj)
    return lj_output


ht1 = Hashtable()
ht1.add("abd", 10)
ht1.add("ahmad", 12)
ht1.add("hasan", 18)
ht1.add("dab", 20)

ht2 = Hashtable()
ht2.add("abd", 10)
ht2.add("asx", 12)
ht2.add("ahmad", 18)
ht2.add("hasan", 20)
actual = left_join(ht1, ht2)
print(actual)


# //////////////////////////////////////////
