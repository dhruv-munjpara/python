# def check_even(num):
#     if num%2==0:
#         return num
# lst_num=[1,33,24,55,67,88]
# lst_even_num=list(filter(check_even,lst_num))
# print(lst_even_num)


# print even numbers from list with lambda
list1=[22,66,77,88,99,44,55]
lst_ans=list(filter(lambda i:i%2==0,list1))
print("list of even numbers",lst_ans)