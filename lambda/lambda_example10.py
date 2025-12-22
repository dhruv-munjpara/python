# # squre of even number from list
# lst_num=[1,2,4,6,7,9]
# def even_num(num):
#     if num%2==0:
#         return num
# even_nums=list(filter(even_num,lst_num))
# print(even_nums)
# def squre_even(num):
#     return num*num
# squre_even_nums=list(map(squre_even,even_nums))
# print(squre_even_nums)



# squre of even number from list with lambda

list_num1=[1,2,4,6,7,9]
even_num=list(filter(lambda i:i%2==0,list_num1))
print("even_nums:",even_num)
squre_even_num=list(map(lambda i:i*i,even_num))
print("squre_even_num:",squre_even_num)