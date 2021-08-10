# from stack_and_queue import Queue
from stack_and_queue.stack_and_queue import Queue


class AnimalShelter:

    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()
        self.shelter = Queue()

    def enqueue(self, animal):
        if animal == "cat":
            self.cat.enqueue('cat')
            self.shelter.enqueue('cat')
            # print(self.cat.enqueue('cat'))

        elif animal == "dog":
            self.dog.enqueue('dog')
            self.shelter.enqueue('dog')

        else:
            return "Sorry! We do not accept animals that are not cat or dog"

    def dequeue(self, pref="shelter"):
        popped = ""
        if pref == "cat":
            popped = self.cat.dequeue()
            self.shelter.dequeue()

        elif pref == "dog":
            popped = self.dog.dequeue()
            self.shelter.dequeue()
        else:
            return 'NULL'
        return popped


if __name__ == "__main__":
    Animal_Shelter = AnimalShelter()
    Animal_Shelter.enqueue('cat')
    Animal_Shelter.enqueue('dog')
    print(Animal_Shelter)
