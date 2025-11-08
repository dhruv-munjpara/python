def check_even(num):
    if num%2==0:
        return num
lst_num=[1,33,24,55,67,88]
lst_even_num=list(filter(check_even,lst_num))
print(lst_even_num)