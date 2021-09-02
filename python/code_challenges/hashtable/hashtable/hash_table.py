
x = {"abood": 5}
y = {"ahmad": 4}


class Hashtable():
    def __init__(self, size=1024, prime=564):
        self.size = size
        self.array = []
        self.prime = prime

    def add(self, obj):
        key = list(obj.keys())[0]
        value = 0
        for char in key:
            value += ord(char)
        print(value)
        index = (value * self.prime) % (self.size)
        print(index)
        # if self.array[index] is True:
        #     print('hi')
        # else:
        #     print(index)


obj = {"khaled": 5}
ht = Hashtable()
ht.add(obj)
