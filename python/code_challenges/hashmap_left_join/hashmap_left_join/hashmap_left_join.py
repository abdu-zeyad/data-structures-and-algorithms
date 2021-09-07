from python.code_challenges.hashtable.hashtable.hash_table import Hashtable


def left_join(ht1, ht2):
    pass


ht1 = Hashtable()
ht1.add("abd", 10)
ht1.add("adb", 12)
ht1.add("dba", 18)
ht1.add("dab", 20)

ht2 = Hashtable()
ht2.add("abd", 10)
ht2.add("adb", 12)
ht2.add("dba", 18)
ht2.add("dab", 20)

array = left_join(ht1, ht2)
print(array)
