# add two lst
def add(num1,num2):
    return num1+num2
lst1=[2,3,4,5]
lst2=[1,6,7,8]
lst_ans=list(map(add,lst1,lst2))
print(lst_ans)


# power a base list
lst_base=[1,2,3,4]
lst_pow=[2,3,4,5]
lst_ans=list(map(pow,lst_base,lst_pow))
print(lst_ans)