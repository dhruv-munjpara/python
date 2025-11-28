from abc import ABC,abstractmethod
class class1(ABC):
    @abstractmethod
    def greet(self):
        pass
    def greet1(self):
        print("good morning")
class class2 (class1):
    def greet(self):
        print("have a nice day")
obj1=class2()
obj1.greet()
obj1.greet1()