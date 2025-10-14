# Write a program to find common among 2 lists. eg. lst_numbers = [1,2,34,33,21] lst_numbers2=[11,2,33,45] output [2,33]
# lst_numbers = [1,2,34,33,21]
# lst_numbers2=[11,2,33,45]
# lst=[]
# for num in lst_numbers:
#     if num in lst_numbers2:
#         lst.append(num)
# print(lst)




lst_numbers = [1,2,34,33,21]
lst_numbers2=[11,2,33,45]
lst=[i for i in lst_numbers if i in lst_numbers2]
print(lst)