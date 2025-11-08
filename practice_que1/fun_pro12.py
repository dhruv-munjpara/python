# - Write a function that accepts a list of numbers and returns a new list with all the numbers that are divisible by both 2 and 3.
def div_2_or_3(lst):
    lst1=[]
    for i in lst:
        if i%2==0 or i%3==0:
            lst1.append(i)
    return lst1
lst=[1,2,3,4,5,6,7,8,9]
print(div_2_or_3(lst))