#find avg from dict
from functools import reduce
data1=[{"name":"eee","age":23},{"name":"ddd","age":21},{"name":"fff","age":24}]
def add(x,y):
    return x+y
def get_avg(p):
    return p['age']
age=list(map(get_avg,data1))
print(age)
avg_age=reduce(add,age)/len(age)
print(avg_age)

    
