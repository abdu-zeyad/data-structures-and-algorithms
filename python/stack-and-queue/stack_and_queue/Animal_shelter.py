# from stack_and_queue import Queue
from stack_and_queue.stack_and_queue import Queue


class AnimalShelter:
    def __init__(self):
        self.catrear = None
        self.catinfront = None
        self.dogrear = None
        self.frontdog = None

    def enqueue(self, Animal):

        if Animal.type == "cat":

            if self.catinfront == None:
                self.catinfront = Animal
                self.catrear = Animal
            else:
                self.catrear.next = Animal
                self.catrear = Animal

        if Animal.type == "dog":

            if self.frontdog == None:
                self.frontdog = Animal
                self.dogrear = Animal
            else:
                self.dogrear.next = Animal
                self.dogrear = Animal

    def dequeue(self, pref):

        if pref == "cat" and self.catinfront != None:
            temp = self.catinfront
            self.catinfront = temp.next
            temp.next = None
            return temp.name

        elif pref == "dog" and self.frontdog != None:
            temp = self.frontdog
            self.frontdog = temp.next
            temp.next = None
            return temp.name
        else:
            return 'null'

    def __str__(self, pref):
        content = "Null"
        if pref == "cat":
            current = self.catrear
        elif pref == "dog":
            current = self.dogrear
        else:
            return content

        while current:
            content += f"-> {{{str(current.name)}}}"
            current = current.next
        return content


class Cat():
    def __init__(self, name):
        self.name = name
        self.type = 'cat'
        self.next = None


class Dog():
    def __init__(self, name):
        self.name = name
        self.type = 'dog'
        self.next = None


if __name__ == "__main__":
    gigner = Cat('gigner')
    bob = Dog('bob')
    Animal_shelter = AnimalShelter()
    Animal_shelter.enqueue(bob)
    Animal_shelter.enqueue(gigner)

    print(Animal_shelter.__str__("dog"))
    print(Animal_shelter.__str__("cat"))
