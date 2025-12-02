import time
def time_check(func):
    def wrapper():
        print("start at",time.time())
        func()
        print("ending",time.time())
    return wrapper
def count():
    for i in range(100):
        pass
