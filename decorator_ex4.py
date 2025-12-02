from functools import wraps
import logging
logging.basicConfig(level=logging.INFO)

def log_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        logging.info(f"calling:{func.__name__}")
        logging.info(f"args:{args},kwargs:{kwargs}")
        result=func(*args,**kwargs)
        logging.info(f"returned:{result}")
        return result
    return wrapper
@log_decorator
def count(num):
    c=0
    for i in range(1,num):
        c+=1
@log_decorator
def greet(name,msg):
    print(f"{msg}--{name}")

greet(name="dhruv",msg="have a nice day")
count(20)