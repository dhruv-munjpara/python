#11.Write a Python program to unzip a list of tuples into individual lists.
tuple_list=[(1,'a'),(2,'b'),(3,'c')]
list1,list2=zip(*tuple_list)

list1=list(list1)
list2=list(list2)

print("original list of tuple:",tuple_list)
print("list1",list1)
print("list2",list2)

