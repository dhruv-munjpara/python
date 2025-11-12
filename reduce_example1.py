from functools import reduce
def add(num1,num2):
    return num1+num2
lst1=[1,2,3,4]
ans1=reduce(add,lst1)
print(ans1)

