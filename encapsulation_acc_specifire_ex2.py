class class1:
    def __init__(self,no1,no2,no3):
        self.no1=no1
        self.no2=no2 
        self.__no3=no3 
    def display(self):
        print(f"{self.no1}--{self.no2}--{self.__no3}")

class class2(class1):
    def display(self):
        print(self.__no2)
        print(self.no1)

c1=class1(1000,2000,3000)      
c1.display()
c2=class1(22,33,44)
c2.display()
