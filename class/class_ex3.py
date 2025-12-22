class person:
    def __init__(self,name,c_no):
        self.name=name
        self.c_no=c_no
    def display(self):
        print(f"{self.name}-{self.c_no}")

class employee(person):
    def __init__(self, name, c_no,salary):
        super().__init__(name, c_no)
        self.salary=salary
    def displayemp(self):
        print(f"{self.name}-{self.c_no}-{self.salary}")

p1=person("dhruv",2345)
p1.display()
emp1=employee("ram",23456,9309843)
emp1.display()
emp1.displayemp()