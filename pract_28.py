num=int(input("how many number you want:"))
a,b=0,1
sum=0

while sum<num:
    print(a,end=" ")
    a,b=b,a+b
    sum+=1

