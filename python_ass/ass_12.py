#12.Write a Python program to convert a list of tuples into a dictionary
tuple_list=[(1,'apple'),(2,'banana'),(3,'cherry')]

result={}
for key ,Value in tuple_list:
    result[key]=Value
print(tuple_list)
print(result)

#2 
result1=dict(tuple_list)
print(result1)