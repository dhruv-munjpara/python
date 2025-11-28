# encapsulation means wraping a data and function into  single unit(object)\
#encapsulation=wraping data+method into single unit

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"{self.name}--->{self.age}")

s1=student("dhruv",22)
s1.display()