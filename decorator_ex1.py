def decorate(func):
    def wrapper():
        print("function calling")
        func()
        print("function ending")
    return wrapper
@decorate
def greet():
    print("good maorning")
@decorate
def adition():
    print(12+23)
greet()
adition()
