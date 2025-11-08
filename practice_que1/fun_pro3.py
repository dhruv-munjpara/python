#  - Write a function that accepts a list of numbers and returns a new list with only the numbers that are divisible by 3.
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lst1=[]
def divisible_by_3():
    for i in lst:
        if i%3==0:
            lst1.append(i)
    return lst1

print(divisible_by_3())