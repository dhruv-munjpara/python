# - Write a function that accepts a list of numbers and returns the average of the numbers, excluding any zero values
lst=[0,1,2,0,3,4,5,0]
def avg():
    num=0
    for i in lst:
        if i>0:
            num+=i
    print("total=",num)
    print("avg=",num/len(lst))

avg()