class car:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def start():
        print("start")

    @staticmethod
    def stop():
        print("stop")


class toyota(car):
    def __init__(self, name, var):
        super().__init__(name)   # call parent constructor
        self.var = var


class fortuner(toyota):
    def __init__(self, name, var, type):
        super().__init__(name, var)   # call toyota constructor
        self.type = type

    def display(self):
        print(f"Name: {self.name}")
        print(f"Var: {self.var}")
        print(f"Type: {self.type}")


car1 = fortuner("Fortuner", "Toyota Company", "Diesel")
car1.display()
car1.start()
