class info:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"name{self.name} and age is {self.age}")

    @staticmethod
    def print_message():
        print("hello everyone")

i1=info("dhruv",25)
i1.display()
i1.print_message()
        