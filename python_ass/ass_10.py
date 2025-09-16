#10.Write a Python program to get unique values from a list.

list1=[1,2,3,4,5,5,5,6,6,6,3,7,8,9]
unique_list=[]
 
for num in list1:
    if num  not  in unique_list:
        unique_list.append(num)

print("unique value:",unique_list)