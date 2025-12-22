class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print(f"name:{self.name} and average score is:{sum/3}")

s1=student("dhruv",[90,91,92])
s1.display_avg()

s1.name="kajal"
s1.marks=[25,45,66]
s1.display_avg()


        