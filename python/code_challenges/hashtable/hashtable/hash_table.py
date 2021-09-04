from python.code_challenges.linked_list.linked_list.linked_list import Linked_list


class Hashtable(Linked_list):
    def __init__(self, size=1024, prime=564):
        self.size = size
        self.array = [None] * size
        self.prime = prime

    def add(self, key, value):
        index = self.hash(key)

        if self.array[index] is None:
            self.array[index] = Linked_list()
            self.array[index].insert((key, value))
        else:
            self.array[index].insert((key, value))
            print(self.array[index])

    def get(self, key):
        pass

    def contains(self, key):
        pass

    def hash(self, key):
        value = 0
        for char in key:
            value += ord(char)
        index = (value * self.prime) % (self.size)
        return index


ht = Hashtable()
ht.add('abd', 10)
ht.add('abd', 12)
# ht.add('abd', 10)
