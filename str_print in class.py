class student:
    def __init__(self,name,marks,grade):
        self.name=name
        self.marks=marks
        self.grade=grade

    # def display(self):
    #     print(f"{self.name}-{self.marks}-{self.grade}")
    def __str__(self):
        return f"{self.name}-{self.marks}-{self.grade}"

s1=student("dhruv",99,"A+")
s2=student("romil",100,"A++")
print(s1)
print(s2)