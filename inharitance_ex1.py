class car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped")

class toyota(car):
    def __init__(self,name):
        self.name=name

car1=toyota("fortuner") 
car2=toyota("camry")

print(car1.name)
car1.start()

print(car2.name)
car2.start()
