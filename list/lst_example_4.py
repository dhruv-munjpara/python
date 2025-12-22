lst_name=["romil","abhijit","dhruti"]
print(lst_name)
total_name=len(lst_name)
for i in range(total_name):
    print(lst_name[i])

print(lst_name[-2]) #if you start with last so it will start with 1
print(lst_name[2]) # if you start with start to 0 index
print("--------------------------------------")
for i in range(total_name-1,-1,-1):
    print(lst_name[i])