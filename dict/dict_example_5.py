dict1={1:"dhruv",2:"het",3:"romil"}
dict2={2:"het",4:"ashok"}
# merged=dict1.copy()
# for k,v in dict2.items():
#     if k not in merged or merged[k]!=v:
#         merged[k]=v
# print(merged)



# 1 method  
# merged = dict1 | dict2   #  | (pipe symbol)
# print(merged)


# 2 method
dict3={**dict1,**dict2}
print(dict3)