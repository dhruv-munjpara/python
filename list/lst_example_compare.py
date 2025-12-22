lst_number=[1,2,9]
lst_new_number=[i**5 for i in lst_number]
print(lst_new_number)
#all string to uppercase
lst_city=["baroda","ahemdabad","limbdi"]
lst_upper_city=[i.upper() for i in lst_city if len(i)>5]
print(lst_upper_city)

lst_num=[1,2,3]
lst_num_ans=[(i,i**2,i**3) for i in lst_num]
print(lst_num_ans)

lst_num_sq=(i*i for i in lst_num)
print(list(lst_num_sq))