str="this is python class"
print(str[-4])
print(len(str))

name=input("enter name:")
for i in name:
    print(i)

for i in range(len(name)):
    print(f"{i}---->{name[i]}")