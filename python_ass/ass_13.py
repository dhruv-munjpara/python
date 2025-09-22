#13.Write a Python program to sort a dictionary (ascending /descending) by value
dict1={'a': 5, 'b': 2, 'c': 9, 'd': 1}

asc_sorted=dict(sorted(dict1.items(),key=lambda item:item[1]))
print("ascending order:",asc_sorted)

desc_sorted=dict(sorted(dict1.items(),key=lambda item:item[1],reverse=True))
print("descending order:",desc_sorted)
