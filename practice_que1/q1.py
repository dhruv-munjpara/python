# Write a program to remove all items from a list that are less then 5 e.g [12,3,4,5,67,0] output [12,5,67]
lst=[12,3,4,5,67,0]
for i in lst[:]:
    if i<5:
        lst.remove(i)
print(lst)
# its is give all indexes show which index is remove




# lst=[12,3,4,5,67,0]
# lst=[i for i in lst if i>5]
# print(lst)
