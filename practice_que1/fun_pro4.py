# - Write a function that accepts a list of numbers and returns a new list with the squares of all the numbers in the list.
lst=[1,2,3,4,5]
lst1=[]
def squre_of_lst():
    for i in lst:
        lst1.append(i*i)
    return lst1
print(squre_of_lst())