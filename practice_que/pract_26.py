rows=int(input("enter a the hight of  the diamond:"))

for i in range(1,rows+1):
    print(" "*(rows-i),end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(rows-1,0,-1):
    print(" "*(rows-i),end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
