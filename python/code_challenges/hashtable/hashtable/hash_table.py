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
            return self.array[index]
        else:
            self.array[index].insert((key, value))
            return self.array[index]

    def get(self, key):
        index = self.hash(key)
        # print(self.array[index].head.value[0])
        current_value = self.array[index].head
        while (current_value):
            key_inside = current_value.value[0]
            if key_inside == key:
                return (current_value.value[1])

            current_value = current_value.next

    def contains(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            return False

        current_value = self.array[index].head
        while (current_value):
            key_inside = current_value.value[0]
            if key_inside == key:
                return True
            current_value = current_value.next
        return False

    def hash(self, key):
        value = 0
        for char in key:
            value += ord(char)
        index = (value * self.prime) % (self.size)
        return index


ht = Hashtable()
ht.add('abd', 10)
ht.add('adb', 12)
ht.add('dba', 18)
ht.add('dab', 20)
print(ht.get('adb'))

print(ht.contains('abd'))
