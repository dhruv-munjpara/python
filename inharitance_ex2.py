class animal:
    def eat(self):
        print("eating")

class dog(animal):
    def bark(self):
        print("dog is barking")

class cat(animal):
    def meow(self):
        print("meow")

d=dog()
d.eat()
d.bark()