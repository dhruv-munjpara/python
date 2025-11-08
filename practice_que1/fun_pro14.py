# - Write a function that accepts a list of integers and returns the second largest number in the list.
lst=[1,7,5,8,0,4,2]
def largest():
    lst.sort(reverse=True)
    return lst[1]
print(largest())