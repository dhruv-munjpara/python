lst=['ahemdabad',345,567,345,67567,34234]
print(lst.count('test'))
print(lst.index(345,2))
print(lst)

print("BEFORE remove",lst)
lst.remove(345)
print("sfter remove",lst)
lst.reverse()
print("after rverse",lst)

lst1=[12,2,4,5,6,98,56]
lst1.sort(reverse=True)
print("sort",lst1)




lst2=[23,34,54,23,45,56,89,23,56,23]
print(lst2.index(23,4,8))

print("bofore pop",lst2)
lst2.pop()
lst2.pop()
lst2.pop()
lst2.pop(2)