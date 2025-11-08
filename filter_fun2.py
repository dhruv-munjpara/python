# squre of even number from list
lst_num=[1,2,4,6,7,9]
def even_num(num):
    if num%2==0:
        return num
even_nums=list(filter(even_num,lst_num))
print(even_nums)
def squre_even(num):
    return num*num
squre_even_nums=list(map(squre_even,even_nums))
print(squre_even_nums)