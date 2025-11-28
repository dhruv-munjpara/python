class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def hello(self):
        print("hello",self.name)
    def get_marks(self):
        print("marks is :",self.marks)
s1=student("dhruv",80)
s1.hello()
s1.get_marks()

        