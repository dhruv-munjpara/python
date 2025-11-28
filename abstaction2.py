from abc import ABC,abstractmethod
class bank(ABC):
    @abstractmethod
    def calculateIntrest(self):
        return 0.0
class sbi(bank):
    def __init__(self,p,r,t):
        super().__init__()
        self.p=p
        self.r=r
        self.t=t
    def calculateIntrest(self):
        return (self.p*self.r*self.t)/100
class axis(bank):
    def __init__(self,p,r,t):
        super().__init__()
        self.p=p
        self.r=r
        self.t=t
    def calculateIntrest(self):
        return (self.p*self.r*self.t)/100
obj1=sbi(1000,5,2)
print(f"sbi intrest{obj1.calculateIntrest()}")
obj2=axis(2000,6,2)
print(f"axis intrest{obj2.calculateIntrest()}")

