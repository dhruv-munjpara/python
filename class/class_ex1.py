class  employee:
    def __init__(self,name):
        self.name=name

    def greet(self,name):
        print(f"Good morning {name}")

dhruv=employee("dhruv")
dhruv.greet("dhruv")        