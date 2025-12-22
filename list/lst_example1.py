lst=[12,34,56,76]

print("original list",lst)
lst.append(900)
print("after append",lst)
lst.append(450)
print("after append",lst)
lst1=[900,78,345]
lst.append(lst1)
print("after append",lst)
print(lst[6])

lst=["Ahemdabad","Baroda"]
lst1=["Udaipur","Jaipur"]

lst.extend(lst1)
print(lst)