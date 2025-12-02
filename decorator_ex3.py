def decorator_parameter(func):
    def wrapper(*args,**krgs):
        print(args)
        print(krgs)
        result=func(*args,**krgs)
        return result
    return wrapper
@decorator_parameter
def greet(name,age,address):
    print(f"good morning {name}-->{age}-->{address}")
greet("dhruv",20,"c g road")