num=int(input("enter a number:"))
for i in range(num+1):
    ch=ord('A')
    for j in range(i):
        print(chr(ch),end=" ")
        ch+=1
    print()

