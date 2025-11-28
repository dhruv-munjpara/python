from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def calculateArea(self):
        return 0.0

class rectangle(shape):
    def __init__(self,l,b):
        super().__init__()
        self.l=l
        self.b=b
    def calculateArea(self):
        return self.l*self.b
obj1=rectangle(2,4)
print(f"area  of rextengle is {obj1.calculateArea()}")