class student:
    collage_name="ABC collage"
    name="anonymous"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=student("dhruv",50)
print(s1.name,s1.marks)