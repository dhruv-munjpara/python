num=int(input("enter no:"))
temp=1
for i in range(2,num):
    if num%i==0:
        temp=1
        break
    else:
        temp=0
 
if temp==1:
    print(f"{num} is not prime number")
else:
    print(f"{num} is  prime number") 