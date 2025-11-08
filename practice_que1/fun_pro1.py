# -  Write a function that accepts a list of numbers and returns the average of the numbers.
lst=[1,2,3,4,5]
def avg():
    num=0
    for i in lst:
        num+=i
    print("total=",num)
    print("avg=",num/len(lst))

avg()