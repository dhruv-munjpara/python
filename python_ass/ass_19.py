# 19.Write a Python function that takes a list and returns a new list with unique
# elements of the first list

def unique_list(lst):
    return list(set(lst))

print(unique_list([1,2,2,3,4,4,5,1,6]))