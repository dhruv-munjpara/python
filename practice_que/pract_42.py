num=int(input("enter a number"))
for n in range(2,num):
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            break
    else:
        print(n,end=" ")
