class student:
    def __init__(self,name,marks,grade):
        self.name=name
        self.marks=marks
        self.grade=grade

    def display(self):
        print(f"{self.name}-{self.marks}-{self.grade}")


s1=student("dhruv",99,"A+")
s2=student("romil",100,"A++")

s1.display()
s2.display()